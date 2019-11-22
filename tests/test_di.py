import unittest

from di import DI

from .sample_classes import *


class DISingletonTestCase(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.di = DI()

    def tearDown(self):
        self.di.clear()

    def test_resolve_some_types___register_singleton___return_registered_values(self):
        # Arrange
        data = [
            (int, 1),
            (int, 2),
            (int, 3),
            (str, 'a'),
            (str, 'b'),
            (Person, Person('Mike', 24))
        ]

        for t, expect_value in data:
            with self.subTest(t=t, expect_value=expect_value):
                self.di.register_singleton(t, expect_value)
                # Act
                result = self.di.resolve(t)
                # Assert
                self.assertEqual(expect_value, result)

    def test_resolve_person_class___register_str_is_John_int_is_21___return_person_name_is_John_age_is_21(self):
        # Arrange
        self.di.register_singleton(str, 'John')
        self.di.register_singleton(int, 21)
        # Act
        result = self.di.resolve(Person)
        # Assert
        self.assertEqual('John', result.name)
        self.assertEqual(21, result.age)

    def test_resolve_class___with_no_init_method___resolve(self):
        # Act
        result = self.di.resolve(A)
        # Assert
        self.assertEqual(A, type(result))

    def test_resolve_PersonAndStr___cls_args_in_class___resolve_even_arg_type_is_custom_class(self):
        # Arrange
        self.di.register_singleton(str, 'AAA')
        self.di.register_singleton(int, 21)
        # Act
        result = self.di.resolve(PersonAndStr)
        # Assert
        self.assertEqual('AAA', result.person_a.name)
        self.assertEqual(21, result.person_a.age)
        self.assertEqual('AAA', result.st)


class DIConcreteTestCase(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.di = DI()

    def tearDown(self):
        self.di.clear()

    def test_resolve___some_concrete_type_registered___return_registered_concrete_type_instance(self):
        # Arrange
        data = [
            (int, int),
            (str, str),
            (bool, bool),
            (Animal, Person),
            (A, B),
        ]
        for base_cls, concrete_cls in data:
            with self.subTest(base_cls=base_cls, concrete_cls=concrete_cls):
                self.di.register(base_cls, concrete_cls)
                # Act
                result = self.di.resolve(base_cls)
                # Assert
                self.assertEqual(concrete_cls, type(result))

    def test_resolve___not_registered___return_same_type_instance(self):
        data = [int, str, bool, Animal, A]
        for cls in data:
            with self.subTest(cls=cls):
                result = self.di.resolve(cls)
                self.assertEqual(cls, type(result))

    def test_resolve___cls_init_args_has_default___return_instance_initialized_by_default_value(self):
        result = self.di.resolve(DefaultValueClass)
        # Assert
        self.assertEqual('', result.person.name)
        self.assertEqual(0, result.person.age)
        self.assertEqual('Annie', result.name)
        self.assertEqual(55, result.age)
