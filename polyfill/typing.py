# -*- coding:utf-8 -*-


class TypingMeta(type):
    def __getitem__(cls, item):
        """
        클래스 자체를 Subscriptable하게 만든다.
        파이썬 3.5부터 존재하는 `__class_getitem__`과 같은 일을 한다.

        지원하는 패턴은 다음과 같다.
        - `class MyClass(Generic[T])`
        - `MyClass[T]`
        - `Union[int, str]`
        """
        return cls


class TypingBase:  # pylint: disable=too-few-public-methods
    __metaclass__ = TypingMeta


class TypingFake:  # pylint: disable=too-few-public-methods
    def __init__(self, *args, **kwargs):
        """
        아무 파라미터를 제공하여 인스턴스 생성을 가능하게 만든다.

        지원하는 패턴은 다음과 같다.
        - `T = TypeVar("T", bound=MyClass)`
        """


# 그대로 쓰이는 값들
Any = None  # pylint: disable=invalid-name

# `[]`로 탐색되는 값들
Optional = TypingBase
Union = TypingBase
Callable = TypingBase
Generator = TypingBase
Generic = TypingBase
Type = TypingBase

# `()`로 호출되는 값들
TypeVar = TypingFake
