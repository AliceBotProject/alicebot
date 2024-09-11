"""Telegram 适配器内部使用的实用工具。"""


def snake_to_camel_case(snake_str: str) -> str:
    """将 snake_case 转换为 CamelCase。

    Args:
        snake_str: snake_case 字符串。

    Returns:
        CamelCase 字符串。
    """
    return "".join(x.capitalize() for x in snake_str.lower().split("_"))


def snake_to_lower_camel_case(snake_str: str) -> str:
    """将 snake_case 转换为 lowerCamelCase。

    Args:
        snake_str: snake_case 字符串。

    Returns:
        lowerCamelCase 字符串。
    """
    camel_string = snake_to_camel_case(snake_str)
    return snake_str[0].lower() + camel_string[1:]


def camel_to_snake_case(camel_case: str) -> str:
    """将 CamelCase 转换为 snake_case。

    Args:
        camel_case: CamelCase 字符串。

    Returns:
        snake_case 字符串。
    """
    return lower_camel_to_snake_case(camel_case[0].lower() + camel_case[1:])


def lower_camel_to_snake_case(lower_camel_case: str) -> str:
    """将 lowerCamelCase 转换为 snake_case。

    Args:
        lower_camel_case: lowerCamelCase 字符串。

    Returns:
        snake_case 字符串。
    """
    snake_case = ""
    for s in lower_camel_case:
        if s.isupper():
            snake_case += "_"
        snake_case += s.lower()
    return snake_case
