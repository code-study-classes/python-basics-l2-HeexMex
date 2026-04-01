# Контрольная точка №2: Обработка пользовательских данных (Функции и ФВП)

## Правила и регламент

- Работайте в файле `index.py`.
- Не изменяйте тесты и служебные файлы проекта.
- Перед отправкой запускайте локальные проверки: `make lint`, `make test` или `make check`.

---

## 1 задача: Динамическое обновление профиля

Вам необходимо написать функцию `update_profile()`, которая имитирует обработку PATCH-запроса на обновление данных пользователя. У каждого пользователя есть обязательный ID, но набор обновляемых полей (имя, возраст, статус, тема оформления) может быть любым.

**Функции и аргументы**

- Функция `update_profile()`
- Обязательный аргумент `user_id`
- Аргумент для упаковки произвольного числа параметров

**Пример использования**

```python
result = update_profile(105, role="admin", is_verified=True, theme="dark")
print(result)
# {'id': 105, 'updated_fields': {'role': 'admin', 'is_verified': True, 'theme': 'dark'}}
```

---

## 2 задача: Парсинг почтовых доменов

Вам необходимо написать функцию `get_domains()`, которая обрабатывает список email-адресов пользователей для аналитики. Нужно извлечь только доменную часть из каждого адреса (всё, что идет после символа `@`).

**Функции и аргументы**

- Функция `get_domains()`
- Обязательный аргумент `emails`


**Пример использования**

```python
emails = ["user123@gmail.com", "admin@mail.ru", "support@yandex.ru"]
domains = get_domains(emails)

print(list(domains))
# ['gmail.com', 'mail.ru', 'yandex.ru']
```

---

## 3 задача: Сегментация целевой аудитории

Вам необходимо написать функцию `filter_target_audience()`. Бэкенд получил массив объектов (словарей) из базы данных. Нужно отфильтровать этот список, оставив только совершеннолетних пользователей (`age >= 18`), у которых включена подписка (`is_premium == True`).

**Функции и аргументы**

- Функция `filter_target_audience()`
- Обязательный аргумент `users`


**Пример использования**

```python
users = [
    {"username": "alex", "age": 17, "is_premium": True},
    {"username": "maria", "age": 22, "is_premium": False},
    {"username": "ivan", "age": 25, "is_premium": True},
    {"username": "anna", "age": 19, "is_premium": True},
]

target_audience = filter_target_audience(users)

print(list(target_audience))
# [{'username': 'ivan', 'age': 25, 'is_premium': True}, {'username': 'anna', 'age': 19, 'is_premium': True}]
```

---

## 4 задача: Сборка ответа API

Вам необходимо написать универсальную функцию `build_response()` для формирования HTTP-ответа сервера. Функция должна принимать статус-код, неограниченное количество сообщений об ошибках (если они есть) и любые дополнительные данные пользователя (payload).

**Функции и аргументы**

- Функция `build_response()`
- Обязательный аргумент `status_code`
- Необязательный аргумент `errors`
- Обязательный аргумент `payload`

**Пример использования**

```python
response_1 = build_response(200, user_id=404, token="abc123xyz")
print(response_1)
# {'status': 200, 'errors': (), 'data': {'user_id': 404, 'token': 'abc123xyz'}}

response_2 = build_response(400, "Invalid email format", "Password too short", attempt=3)
print(response_2)
# {'status': 400, 'errors': ('Invalid email format', 'Password too short'), 'data': {'attempt': 3}}
```

---

## 5 задача: Агрегация логов транзакций

Вам необходимо написать функцию `calculate_total_spent()`, которая анализирует логи покупок пользователя. Дан список словарей, где каждый словарь — это транзакция с указанием суммы (`amount`). Нужно свести эту структуру к одному числу — вычислить общую сумму всех покупок пользователя (LTV - Life Time Value).

**Функции и аргументы**

- Функция `calculate_total_spent()`
- Обязательный аргумент `transactions`

**Пример использования**

```python
transactions = [
    {"trx_id": "A1", "amount": 1500.00},
    {"trx_id": "A2", "amount": 350.50},
    {"trx_id": "B1", "amount": 2100.00},
]

total_spent = calculate_total_spent(transactions)

print(total_spent)
# 3950.5
```
