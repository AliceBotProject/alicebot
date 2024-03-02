import pytest
from fake_message import FakeMessage, FakeMessageSegment
from pydantic import TypeAdapter, ValidationError


def test_get_message_segment_init() -> None:
    msg_seg = FakeMessageSegment(type="text", data={"text": "Hello"})
    assert msg_seg.type == "text"
    assert msg_seg.data == {"text": "Hello"}


def test_get_message_segment_eq() -> None:
    msg_seg = FakeMessageSegment(type="text", data={"text": "Hello"})
    other_msg_seg = FakeMessageSegment.text("Hello")
    assert msg_seg == other_msg_seg

    other_msg_seg = FakeMessageSegment.text("test")
    assert msg_seg != other_msg_seg

    other_msg_seg = FakeMessageSegment(type="image", data={"text": "Hello"})
    assert msg_seg != other_msg_seg

    class NewFakeMessageSegment(FakeMessageSegment):
        pass

    other_msg_seg = NewFakeMessageSegment.text("Hello")
    assert msg_seg != other_msg_seg


def test_get_message_segment_str() -> None:
    msg_seg = FakeMessageSegment.text("Hello")
    assert str(msg_seg) == "Hello"

    msg_seg = FakeMessageSegment(type="image", data={"text": "Hello"})
    assert str(msg_seg) == "{'text': 'Hello'}"


def test_message_segment_add() -> None:
    msg = FakeMessageSegment.text("a") + FakeMessageSegment.text("b")
    assert isinstance(msg, FakeMessage)
    assert str(msg) == "ab"

    msg = FakeMessageSegment.text("a") + "b"
    assert isinstance(msg, FakeMessage)
    assert str(msg) == "ab"

    msg = "a" + FakeMessageSegment.text("b")
    assert isinstance(msg, FakeMessage)
    assert str(msg) == "ab"


def test_message_segment_data() -> None:
    msg_seg = FakeMessageSegment.text("Hello")
    assert "text" in msg_seg
    assert msg_seg["text"] == "Hello"
    assert msg_seg.get("text") == "Hello"
    assert msg_seg.get("no_such_field") is None
    assert len(msg_seg) == 1
    assert list(msg_seg.keys()) == ["text"]
    assert list(msg_seg.values()) == ["Hello"]
    assert list(msg_seg.items()) == [("text", "Hello")]

    msg_seg["temp"] = "test"
    assert "temp" in msg_seg
    assert msg_seg["temp"] == "test"
    assert len(msg_seg) == 2
    assert list(msg_seg.keys()) == ["text", "temp"]
    assert list(msg_seg.values()) == ["Hello", "test"]
    assert list(msg_seg.items()) == [("text", "Hello"), ("temp", "test")]

    del msg_seg["temp"]
    assert "temp" not in msg_seg
    assert len(msg_seg) == 1

    assert list(msg_seg) == ["text"]


def test_is_text() -> None:
    msg_seg = FakeMessageSegment(type="text")
    assert msg_seg.is_text()
    msg_seg = FakeMessageSegment(type="image")
    assert not msg_seg.is_text()


def test_message_init() -> None:
    msg = FakeMessage()
    assert len(msg) == 0

    msg_seg = FakeMessageSegment.text("Hello")
    msg = FakeMessage(msg_seg)
    assert len(msg) == 1
    assert msg[0] == msg_seg

    msg = FakeMessage({"type": "text", "data": {"text": "Hello"}})
    assert len(msg) == 1
    assert msg[0] == msg_seg

    msg = FakeMessage("Hello")
    assert len(msg) == 1
    assert msg[0] == msg_seg

    msg = FakeMessage("Hello", "test")
    assert len(msg) == 2

    msg = FakeMessage("Hello", msg_seg)
    assert len(msg) == 2

    msg = FakeMessage(msg)
    assert len(msg) == 2

    with pytest.raises(TypeError):
        FakeMessage(1)  # type: ignore


def test_message_model() -> None:
    ta = TypeAdapter(FakeMessage)

    res = ta.validate_python([])
    assert isinstance(res, FakeMessage)
    assert res == []

    res = ta.validate_python([{"type": "text", "data": {"text": "Hello"}}])
    assert isinstance(res, FakeMessage)
    assert res == FakeMessage("Hello")

    with pytest.raises(ValidationError):
        ta.validate_python([{"data": {"text": "Hello"}}])


def test_message_str() -> None:
    msg = FakeMessage("Hello")
    assert str(msg) == "Hello"

    msg = FakeMessage("Hello", "test")
    assert str(msg) == "Hello" + "test"

    msg = FakeMessage("Hello", "test")
    assert (
        repr(msg)
        == "Message:["
        + repr(FakeMessageSegment.text("Hello"))
        + ","
        + repr(FakeMessageSegment.text("test"))
        + "]"
    )


def test_message_text() -> None:
    msg = FakeMessage("Hello")
    assert msg.is_text()
    assert msg.get_plain_text() == "Hello"

    msg = FakeMessage("Hello", "test")
    assert msg.is_text()
    assert msg.get_plain_text() == "Hello" + "test"

    msg = FakeMessage("Hello", FakeMessageSegment(type="image", data={}))
    assert not msg.is_text()
    assert msg.get_plain_text() == "Hello"


def test_message_contains() -> None:
    msg = FakeMessage("Hello", "test")
    assert FakeMessageSegment.text("Hello") in msg
    assert FakeMessageSegment.text("test") in msg
    assert FakeMessageSegment.text("xxx") not in msg
    assert "Hello" in msg
    assert "He" in msg


def test_message_add() -> None:
    msg = FakeMessage()

    assert len(msg) == 0

    msg_seg = FakeMessageSegment.text("Hello")
    msg = FakeMessage() + msg_seg

    assert len(msg) == 1
    assert msg[0] == msg_seg

    msg = FakeMessage() + "test"

    assert len(msg) == 1
    assert msg[0] == FakeMessageSegment.text("test")

    msg = FakeMessage() + {"type": "text", "data": {"text": "temp"}}

    assert len(msg) == 1
    assert msg[0] == FakeMessageSegment.text("temp")

    msg = {"type": "text", "data": {"text": "temp"}} + FakeMessage()

    assert len(msg) == 1
    assert msg[0] == FakeMessageSegment.text("temp")

    with pytest.raises(TypeError):
        FakeMessage() + 1  # type: ignore


def test_message_copy() -> None:
    msg = FakeMessage()
    copied_msg = msg.copy()
    assert copied_msg == msg
    assert copied_msg is not msg


def test_message_startswith() -> None:
    msg_seg_1 = FakeMessageSegment.text("test")
    msg_seg_2 = FakeMessageSegment.text("abc")
    msg = FakeMessage(msg_seg_1, msg_seg_2)
    assert msg.startswith(msg_seg_1)
    assert msg.startswith("t")

    assert not msg.startswith(msg_seg_2)
    assert not msg.startswith("a")

    assert FakeMessage().startswith("")
    assert not FakeMessage().startswith(FakeMessageSegment.text(""))

    with pytest.raises(TypeError):
        FakeMessage().startswith(1)  # type: ignore


def test_message_endswith() -> None:
    msg_seg_1 = FakeMessageSegment.text("test")
    msg_seg_2 = FakeMessageSegment.text("abc")
    msg = FakeMessage(msg_seg_1, msg_seg_2)
    assert msg.endswith(msg_seg_2)
    assert msg.endswith("c")

    assert not msg.endswith(msg_seg_1)
    assert not msg.endswith("t")

    assert FakeMessage().endswith("")
    assert not FakeMessage().endswith(FakeMessageSegment.text(""))

    with pytest.raises(TypeError):
        FakeMessage().endswith(1)  # type: ignore


def test_message_replace() -> None:
    msg_seg_1 = FakeMessageSegment.text("test")
    msg_seg_2 = FakeMessageSegment.text("abc")
    msg = FakeMessage(msg_seg_1, msg_seg_1, msg_seg_2)
    assert msg.replace(msg_seg_1, msg_seg_2) == FakeMessage(
        msg_seg_2, msg_seg_2, msg_seg_2
    )
    assert msg.replace(msg_seg_1, msg_seg_2, count=1) == FakeMessage(
        msg_seg_2, msg_seg_1, msg_seg_2
    )
    assert msg.replace(msg_seg_1, None) == FakeMessage(msg_seg_2)
    assert msg.replace(msg_seg_1, None, count=1) == FakeMessage(msg_seg_1, msg_seg_2)

    with pytest.raises(TypeError):
        msg.replace(1, msg_seg_2)  # type: ignore

    with pytest.raises(TypeError):
        msg.replace(msg_seg_1, "")  # type: ignore

    with pytest.raises(TypeError):
        msg.replace("", msg_seg_2)  # type: ignore

    assert msg.replace("abc", "xyz") == FakeMessage(
        msg_seg_1, msg_seg_1, FakeMessageSegment.text("xyz")
    )
    assert msg.replace("test", "xyz") == FakeMessage(
        FakeMessageSegment.text("xyz"), FakeMessageSegment.text("xyz"), msg_seg_2
    )
    assert msg.replace("a", "x") == FakeMessage(
        msg_seg_1, msg_seg_1, FakeMessageSegment.text("xbc")
    )
    assert msg.replace("st", "xt") == FakeMessage(
        FakeMessageSegment.text("text"), FakeMessageSegment.text("text"), msg_seg_2
    )
    assert msg.replace("st", "xt", count=1) == FakeMessage(
        FakeMessageSegment.text("text"), msg_seg_1, msg_seg_2
    )
