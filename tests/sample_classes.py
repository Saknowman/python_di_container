class A:
    pass


class B(A):
    pass


class S(str):
    pass


class Animal:
    pass


class Person(Animal):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class PersonAndStr:
    def __init__(self, person_a: Person, st: str):
        self.person_a = person_a
        self.st = st


class DefaultValueClass:
    def __init__(self, person: Person, name: str = "Annie", age: int = 55):
        self.person = person
        self.name = name
        self.age = age
