# python_di_container
This repository provide simple python DI Container.

## Usage
Just register concrete class or register singleton.
Then resolve class, you can get instance.

## DEMO

```python
from di_container import di

class Animal:
    def __init__(self, kind: str, name: str):
        self.kind = kind
        self.name = name

    def __str__(self):
        return "I am {kind}. My name is {name}".format(kind=self.kind, name=self.name)


class Cat(Animal):
    def __init__(self, name: str = "Cathy"):
        super().__init__('Cat', name)


di.register(Animal, Cat)
print(di.resolve(Animal))
# > I am Cat. My name is Cathy.


class Person:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def __str__(self):
        return "I am {name}. My role is {role}.".format(name=self.name, role=self.role)

nukumizu = Person('Nukumizu', 'Actor')
di.register_singleton(Person, nukumizu)
print(di.resolve(Person))
# > I am Nukumizu. My role is Actor.
```