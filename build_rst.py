import os
import shutil
import pathlib
import pkgutil

module_name = 'alicebot'
docs_build_folder = 'docs_build'
source_working_dir = os.getcwd()


def clean_docs_build_folder(folder):
    for i in os.listdir(folder):
        t = os.path.join(folder, i)
        if os.path.isfile(t):
            if pathlib.Path(t).suffix == '.rst':
                os.remove(t)
        elif os.path.isdir(t):
            clean_docs_build_folder(t)
        else:
            raise OSError
    if not os.listdir(folder):
        os.rmdir(folder)


def build_rst(folder):
    os.makedirs(os.path.join(source_working_dir, folder.replace(module_name, docs_build_folder)), exist_ok=True)
    result = []
    for module_info in pkgutil.iter_modules([os.path.join(os.getcwd(), folder)]):
        if module_info.ispkg:
            if list(pkgutil.iter_modules([os.path.join(folder, module_info.name)])):
                build_rst(os.path.join(folder, module_info.name))
            else:
                result.append(module_info.name)
        else:
            result.append(module_info.name)
    with open(os.path.join(source_working_dir, folder.replace(module_name, docs_build_folder), 'README.rst'), 'w',
              encoding='utf8') as f:
        f.write('{}\n==========================================\n\n.. automodule:: {}\n   :members:\n'
                .format(*[folder.replace('/', '.')] * 2))
    for i in result:
        with open(os.path.join(source_working_dir, folder.replace(module_name, docs_build_folder), i + '.rst'), 'w',
                  encoding='utf8') as f:
            f.write('{}\n==========================================\n\n.. automodule:: {}\n   :members:\n'
                    .format(*[os.path.join(folder, i).replace('/', '.')] * 2))

    print(''.join(["{title: '" + os.path.join(folder, i).replace('/', '.') +
                   "', path: '" + os.path.join(*folder.split('/')[1:], i) + "'},\n"
                   for i in result]), end='')
    print("{title: '" + folder.replace('/', '.') + "', path: '" + os.path.join(*folder.split('/')[1:], '') + "'}\n\n")


if __name__ == '__main__':
    if os.path.isdir(os.path.join(docs_build_folder, '_build')):
        shutil.rmtree(os.path.join(docs_build_folder, '_build'))
    clean_docs_build_folder(docs_build_folder)
    build_rst(module_name)

    # 处理 packages
    with os.scandir(os.path.abspath('packages')) as it:
        entry: os.DirEntry
        for entry in it:
            if not entry.name.startswith('.') and entry.is_dir():
                os.chdir(entry.path)
                build_rst(os.path.join('alicebot', 'adapter'))

    os.chdir(source_working_dir)
    # 针对 mirai.event 的特殊操作
    with open(os.path.join(docs_build_folder, 'adapter', 'mirai', 'event', 'README.rst'), 'r') as fp:
        rst_str = fp.read()
    with os.scandir(os.path.join(docs_build_folder, 'adapter', 'mirai', 'event')) as it:
        entry: os.DirEntry
        for entry in it:
            if entry.name != 'README.rst' and entry.is_file():
                with open(entry.path, 'r') as fp:
                    rst_str += fp.read()
    shutil.rmtree(os.path.join(docs_build_folder, 'adapter', 'mirai', 'event'))
    with open(os.path.join(docs_build_folder, 'adapter', 'mirai', 'event.rst'), 'w') as fp:
        fp.write(rst_str)

    print('Done!')
