"""
============
CQHTTP 消息
============
"""
from typing import Literal, Optional, TypeVar, Union

from alicebot.message import Message, MessageSegment

T_CQHTTPMessage = TypeVar('T_CQHTTPMessage', bound='CQHTTPMessage')
T_CQHTTPMessageSegment = TypeVar('T_CQHTTPMessageSegment', bound='CQHTTPMessageSegment')


class CQHTTPMessage(Message):
    """CQHTTP 消息"""

    def _set_message_segment_class(self):
        self._message_segment_class = CQHTTPMessageSegment

    def _str_to_message_segment(self, msg) -> T_CQHTTPMessageSegment:
        return CQHTTPMessageSegment.text(msg)

    def is_text(self) -> bool:
        """
        :return: 是否是纯文本消息。
        """
        for ms in self:
            if not ms.is_text():
                return False
        return True

    def get_plain_text(self) -> str:
        """
        获取消息中的纯文本部分。

        :return: 消息中的纯文本部分。
        :rtype: str
        """
        return ''.join(map(lambda x: str(x), filter(lambda x: x.is_text(), self)))


class CQHTTPMessageSegment(MessageSegment):
    """CQHTTP 消息字段"""

    def _set_message_class(self):
        self._message_class = CQHTTPMessage

    def __str__(self) -> str:
        if self.type == 'text':
            return self.data.get('text', '')
        return self.get_cqcode()

    def is_text(self) -> bool:
        """
        :return: 是否是纯文本消息字段。
        :rtype: bool
        """
        return self.type == 'text'

    def get_cqcode(self) -> str:
        """
        :return: 此消息字段的 CQ 码形式。
        :rtype: str
        """
        if self.type == 'text':
            return escape(self.data.get('text', ''), escape_comma=False)

        params = ','.join([f'{k}={escape(str(v))}' for k, v in self.data.items() if v is not None])
        return f'[CQ:{self.type}{"," if params else ""}{params}]'

    @classmethod
    def text(cls, text: str) -> T_CQHTTPMessageSegment:
        """纯文本"""
        return cls(type='text', data={'text': text})

    @classmethod
    def face(cls, id_: int) -> T_CQHTTPMessageSegment:
        """QQ 表情"""
        return cls(type='face', data={'id': str(id_)})

    @classmethod
    def image(cls,
              file: str,
              type_: Optional[Literal['flash']] = None,
              cache: bool = True,
              proxy: bool = True,
              timeout: Optional[int] = None) -> T_CQHTTPMessageSegment:
        """图片"""
        return cls(type='image', data={'file': file, 'type': type_, 'cache': cache, 'proxy': proxy, 'timeout': timeout})

    @classmethod
    def record(cls,
               file: str,
               magic: bool = False,
               cache: bool = True,
               proxy: bool = True,
               timeout: Optional[int] = None) -> T_CQHTTPMessageSegment:
        """语音"""
        return cls(type='record',
                   data={'file': file, 'magic': magic, 'cache': cache, 'proxy': proxy, 'timeout': timeout})

    @classmethod
    def video(cls,
              file: str,
              cache: bool = True,
              proxy: bool = True,
              timeout: Optional[int] = None) -> T_CQHTTPMessageSegment:
        """短视频"""
        return cls(type='video', data={'file': file, 'cache': cache, 'proxy': proxy, "timeout": timeout})

    @classmethod
    def at(cls, qq: Union[int, Literal['all']]) -> T_CQHTTPMessageSegment:
        """@某人"""
        return cls(type='at', data={'qq': str(qq)})

    @classmethod
    def rps(cls) -> T_CQHTTPMessageSegment:
        """猜拳魔法表情"""
        return cls(type='rps', data={})

    @classmethod
    def dice(cls) -> T_CQHTTPMessageSegment:
        """掷骰子魔法表情"""
        return cls(type='dice', data={})

    @classmethod
    def shake(cls) -> T_CQHTTPMessageSegment:
        """窗口抖动（戳一戳）"""
        return cls(type='shake', data={})

    @classmethod
    def poke(cls, type_: str, id_: int) -> T_CQHTTPMessageSegment:
        """戳一戳"""
        return cls(type='poke', data={'type': type_, 'id': str(id_)})

    @classmethod
    def anonymous(cls, ignore: Optional[bool] = None) -> T_CQHTTPMessageSegment:
        """匿名发消息"""
        return cls(type='anonymous', data={'ignore': ignore})

    @classmethod
    def share(cls,
              url: str,
              title: str,
              content: Optional[str] = None,
              image: Optional[str] = None) -> T_CQHTTPMessageSegment:
        """链接分享"""
        return cls(type='share', data={'url': url, 'title': title, 'content': content, 'image': image})

    @classmethod
    def contact(cls, type_: Literal['qq', 'group'], id_: int) -> T_CQHTTPMessageSegment:
        """推荐好友/推荐群"""
        return cls(type='contact', data={'type': type_, 'id': str(id_)})

    @classmethod
    def contact_friend(cls, id_: int) -> T_CQHTTPMessageSegment:
        """推荐好友"""
        return cls(type='contact', data={'type': 'qq', 'id': str(id_)})

    @classmethod
    def contact_group(cls, id_: int) -> T_CQHTTPMessageSegment:
        """推荐好友"""
        return cls(type='contact', data={'type': 'group', 'id': str(id_)})

    @classmethod
    def location(cls,
                 lat: float,
                 lon: float,
                 title: Optional[str],
                 content: Optional[str] = None) -> T_CQHTTPMessageSegment:
        """位置"""
        return cls(type='location', data={'lat': str(lat), 'lon': str(lon), 'title': title, 'content': content})

    @classmethod
    def music(cls, type_: Literal['qq', '163', 'xm'], id_: int) -> T_CQHTTPMessageSegment:
        """音乐分享"""
        return cls(type='music', data={'type': type_, 'id': str(id_)})

    @classmethod
    def music_custom(cls,
                     url: str,
                     audio: str,
                     title: str,
                     content: Optional[str] = None,
                     image: Optional[str] = None) -> T_CQHTTPMessageSegment:
        """音乐自定义分享"""
        return cls(type='music', data={'type': 'custom', 'url': url, 'audio': audio, 'title': title, 'content': content,
                                       'image': image})

    @classmethod
    def reply(cls, id_: int) -> T_CQHTTPMessageSegment:
        """回复"""
        return cls(type='reply', data={'id': str(id_)})

    @classmethod
    def node(cls, id_: int) -> T_CQHTTPMessageSegment:
        """合并转发节点"""
        return cls(type='node', data={'id': str(id_)})

    @classmethod
    def node_custom(cls, user_id: int, nickname, content: T_CQHTTPMessage) -> T_CQHTTPMessageSegment:
        """合并转发自定义节点"""
        return cls(type='node', data={'user_id': str(user_id), 'nickname': str(nickname), 'content': content})

    @classmethod
    def xml_message(cls, data: str) -> T_CQHTTPMessageSegment:
        """XML 消息"""
        return cls(type='xml', data={'data': data})

    @classmethod
    def json_message(cls, data: str) -> T_CQHTTPMessageSegment:
        """JSON 消息"""
        return cls(type='json', data={'data': data})


def escape(s: str, *, escape_comma: bool = True) -> str:
    """
    对 CQ 码中的特殊字符进行转义。

    :param s: 待转义的字符串。
    :param escape_comma: 是否转义 ``,``。
    :return: 转义后的字符串。
    :rtype: str
    """
    s = s.replace('&', '&amp;') \
        .replace('[', '&#91;') \
        .replace(']', '&#93;')
    if escape_comma:
        s = s.replace(',', '&#44;')
    return s
