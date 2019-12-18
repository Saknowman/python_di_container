from .di import DI


class Animal:
    def __init__(self, kind: str, name: str):
        self.kind = kind
        self.name = name

    def __str__(self):
        return "I am {kind}. My name is {name}".format(kind=self.kind, name=self.name)


class Cat(Animal):
    def __init__(self, name: str = "Cathy"):
        super().__init__('Cat', name)


class Person:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def __str__(self):
        return "I am {name}. My role is {role}.".format(name=self.name, role=self.role)


print(Person.__init__.__annotations__)


class Request:
    def __init__(self, user: Person):
        self.user = user

    def __str__(self):
        return "This is requested by {user}.".format(user=self.user.name)


class DB:
    def __init__(self, user: Person, db_name: str):
        self.user = user
        self.db_name = db_name

    def __str__(self):
        return "DB: {db}, USER: {user}".format(db=self.db_name, user=self.user.name)


class Controller:
    def __init__(self, db: DB, request: Request):
        self.db = db
        self.request = request

    def info(self):
        print('Controller INFO:')
        print(self.request)
        print(self.db)


di = DI()
di.register(Animal, Cat)
print(di.resolve(Animal))
print()

nukumizu = Person('Nukumizu', 'Actor')
di.register_singleton(Person, nukumizu)
print(di.resolve(Person))
print()

di.register_singleton(DB, DB(Person('DB_USER', 'DEVELOPER'), 'DBDBDBDB'))
controller = di.resolve(Controller)
controller.info()
