## Запуск тестов

Для запуска тестов используйте команды:
```linux
pip install -r requirements.txt
coverage run -m unittest -v tests_what_is_year_now.py
coverage html
open htmlcov/index.html
```