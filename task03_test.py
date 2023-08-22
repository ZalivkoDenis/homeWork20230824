import pytest
from task03 import *


@pytest.fixture
def text() -> str:
    return "Раз два три. Четыре пять шесть! Сем, восемь, девять... Десять?"


def test_task_3_1(text):
    """3.1. Вывести количество предложений в тексте;"""
    assert task_3_1(text) == 4


def test_task_3_2(text):
    """3.2. Вывести количество слов в тексте;"""
    assert task_3_2(text) == 10


def test_task_3_3(text):
    """3.3. Вывести 3 самых больших слова."""
    assert task_3_3(text) == ['четыре', 'восемь', 'девять']