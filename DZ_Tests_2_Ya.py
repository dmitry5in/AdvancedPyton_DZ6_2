from unittest import TestCase
from Yandex import create_dir


class TestYandex(TestCase):
    # Проверка создания новой папки
    def test_create_dir_1(self):
        self.assertEqual(create_dir('Test'), 201)

    # Проверка на наличие папки
    def test_dir_exists(self):
        self.assertEqual(create_dir('Test'), 409)

    # Проверка авторизации пользователя
    def test_dir_auth(self):
        self.assertEqual(create_dir('Test'), 401)