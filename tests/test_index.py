import importlib
import math

import pytest


MODULE_NAME = "index"


def get_student_function(function_name):
    try:
        module = importlib.import_module(MODULE_NAME)
    except ModuleNotFoundError:
        pytest.fail(
            "Не найден файл index.py или модуль index недоступен для импорта."
        )
    except SyntaxError as error:
        pytest.fail(f"В index.py есть синтаксическая ошибка: {error}")
    except Exception as error:
        pytest.fail(f"Не удалось импортировать index.py: {error}")

    function = getattr(module, function_name, None)
    if function is None:
        pytest.fail(f"Функция {function_name} не найдена в index.py")

    return function


def test_step1():
    update_profile = get_student_function("update_profile")

    assert update_profile(105, role="admin", is_verified=True, theme="dark") == {
        "id": 105,
        "updated_fields": {
            "role": "admin",
            "is_verified": True,
            "theme": "dark",
        },
    }
    assert update_profile(7) == {"id": 7, "updated_fields": {}}


def test_step2():
    get_domains = get_student_function("get_domains")

    emails = ["user123@gmail.com", "admin@mail.ru", "support@yandex.ru"]
    domains = get_domains(emails)
    assert list(domains) == ["gmail.com", "mail.ru", "yandex.ru"]
    assert list(get_domains(["boss@company.org"])) == ["company.org"]


def test_step3():
    filter_target_audience = get_student_function("filter_target_audience")

    users = [
        {"username": "alex", "age": 17, "is_premium": True},
        {"username": "maria", "age": 22, "is_premium": False},
        {"username": "ivan", "age": 25, "is_premium": True},
        {"username": "anna", "age": 19, "is_premium": True},
    ]
    result = list(filter_target_audience(users))
    assert result == [
        {"username": "ivan", "age": 25, "is_premium": True},
        {"username": "anna", "age": 19, "is_premium": True},
    ]
    assert list(filter_target_audience([])) == []


def test_step4():
    build_response = get_student_function("build_response")

    assert build_response(200, user_id=404, token="abc123xyz") == {
        "status": 200,
        "errors": (),
        "data": {"user_id": 404, "token": "abc123xyz"},
    }
    assert build_response(
        400,
        "Invalid email format",
        "Password too short",
        attempt=3,
    ) == {
        "status": 400,
        "errors": ("Invalid email format", "Password too short"),
        "data": {"attempt": 3},
    }


def test_step5():
    calculate_total_spent = get_student_function("calculate_total_spent")

    transactions = [
        {"trx_id": "A1", "amount": 1500.00},
        {"trx_id": "A2", "amount": 350.50},
        {"trx_id": "B1", "amount": 2100.00},
    ]
    assert math.isclose(calculate_total_spent(transactions), 3950.5)
    assert math.isclose(calculate_total_spent([]), 0.0)