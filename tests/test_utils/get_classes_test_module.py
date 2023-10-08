from abc import ABC


class SuperClass:
    pass


class SubClass1(SuperClass):
    pass


class SubClass2(SuperClass):
    pass


class AnotherClass:
    pass


class AbstractClass(ABC, SuperClass):
    pass
