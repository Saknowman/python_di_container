class DIContainer:
    concrete_table = {}
    singleton_table = {}

    def register(self, base_cls: type, concrete_cls: type):
        if not issubclass(concrete_cls, base_cls):
            raise TypeError('Concrete class is required {} not {}.'.format(base_cls, concrete_cls))
        self.concrete_table[base_cls] = concrete_cls

    def register_singleton(self, t: type, instance: object):
        if not isinstance(instance, t):
            raise TypeError('Instance type is required {} not {}.'.format(t, type(instance)))
        self.singleton_table[t] = instance

    def get(self, t: type):
        if self.is_registered_concrete(t):
            return self.concrete_table[t]
        return t

    def get_singleton(self, t: type):
        if self.is_registered_singleton(t):
            return self.singleton_table[t]

        raise KeyError('{} is not registered as singleton.'.format(t))

    def is_registered_singleton(self, t: type):
        return t in self.singleton_table.keys()

    def is_registered_concrete(self, t: type):
        return t in self.concrete_table.keys()

    def is_registered(self, t: type):
        return self.is_registered_concrete(t) or self.is_registered_singleton(t)

    def clear(self):
        self.concrete_table.clear()
        self.singleton_table.clear()
