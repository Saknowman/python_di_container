from container import DIContainer


class Resolver:
    def __init__(self, container: DIContainer):
        self.container = container

    def resolve(self, cls: type):
        if self.container.is_registered_singleton(cls):
            return self.container.get_singleton(cls)
        cls = self.container.get(cls)
        init_args = self.resolve_init_args(cls)
        return cls(**init_args)

    def resolve_init_args(self, cls: type):
        init_args_annotations = get_init_args_annotations(cls)
        defaults = get_init_default_values(cls)
        result = {}
        args_count = len(init_args_annotations)
        for key, t in init_args_annotations.items():
            if self.container.is_registered(t) or len(defaults) < args_count:
                result[key] = self.resolve(t)
            else:
                result[key] = defaults[len(defaults) - args_count]
            args_count -= 1

        return result


def get_init_args_annotations(cls: type):
    if hasattr(cls.__init__, '__annotations__'):
        return cls.__init__.__annotations__
    return {}


def get_init_default_values(cls: type):
    if hasattr(cls.__init__, '__defaults__'):
        result = cls.__init__.__defaults__
        return [] if result is None else result
    return []
