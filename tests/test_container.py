import unittest
from container import DIContainer
from tests.sample_classes import *


class ContainerTestCase(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.container = DIContainer()

    def tearDown(self):
        self.container.clear()

    def test_register_singleton___correct_type_instance_registered___success_registered(self):
        data = [
            (str, 'aa'),
            (int, 12),
            (int, 2),
            (bool, True),
            (bool, False),
            (Person, Person('john', 22)),
            (A, A()),
            (Animal, Person('aa', 33))
        ]

        for t, instance in data:
            with self.subTest(t=t, instance=instance):
                self.container.register_singleton(t, instance)
                self.assertTrue(True)

    def test_register_singleton___not_correct_type_instance_registered___raise_type_exception(self):
        data = [
            (str, 1),
            (int, 'aa'),
            (int, 'bb'),
            (bool, 1),
            (bool, 'aa'),
            (Person, 2),
            (A, 'a'),
            (Person, Animal())
        ]

        for t, instance in data:
            with self.subTest(t=t, instance=instance):
                self.assertRaises(TypeError, self.container.register_singleton, t, instance)

    def test_register_type___concrete_classes_extended_base_class_are_registered___success(self):
        data = [
            (str, S),
            (A, B),
            (Animal, Person)
        ]

        for base_cls, concrete_cls in data:
            with self.subTest(key=base_cls, concrete_type=concrete_cls):
                self.container.register(base_cls, concrete_cls)
                self.assertTrue(True)

    def test_register_type___concrete_classes_not_extended_base_class_are_registered___raise_type_exception(self):
        data = [
            (int, S),
            (str, bool),
            (Person, Animal),
            (B, A)
        ]

        for base_cls, concrete_cls in data:
            with self.subTest(key=base_cls, concrete_type=concrete_cls):
                self.assertRaises(TypeError, self.container.register, base_cls, concrete_cls)

    def test_get___registered___return_concrete_class(self):
        data = [
            (str, S),
            (A, B),
            (Animal, Person)
        ]

        for base_cls, concrete_cls in data:
            with self.subTest(key=base_cls, concrete_type=concrete_cls):
                self.container.register(base_cls, concrete_cls)
                result = self.container.get(base_cls)
                self.assertTrue(concrete_cls, result)

    def test_get___not_registered___return_concrete_class(self):
        data = [str, A, Person]

        for target_cls in data:
            with self.subTest(target_cls=target_cls):
                result = self.container.get(target_cls)
                self.assertTrue(target_cls, result)
