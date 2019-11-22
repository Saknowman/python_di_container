from container import DIContainer
from resolver import Resolver


class DI:
    def __init__(self):
        self.container = DIContainer()
        self.resolver = Resolver(self.container)

    def register_singleton(self, t: type, instance: object):
        self.container.register_singleton(t, instance)

    def register(self, base_cls: type, concrete_cls: type):
        self.container.register(base_cls, concrete_cls)

    def resolve(self, t: type):
        return self.resolver.resolve(t)

    def clear(self):
        self.container.clear()

