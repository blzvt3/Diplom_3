## Дипломный проект. Задание 3: UI-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы UI-тесты, покрывающие страницы: восстановление пароля, личный кабинет, конструктор, лента заказов

### Структура проекта

- `tests` - пакет, содержащий тесты, разделенные по страницам. Например, `test_constructor.py`, `test_personal_account.py` и т.д.
- `pages` - пакет, содержащий Page Object-классы
- `allure_results` - пакет, содержащий json файлы отчета о тестировании

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчёта о тестировании**

>  `$ pytest --alluredir=allure_results`
>  `$ allure serve allure_results`