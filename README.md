Щоб поставити бек локально потрібно:

- Встановити Python
- З командного рядку прописати команду щоб створити віртуальне середовище
shell```python -m venv app```
- В репозиторії нажміть на Code -> Download ZIP щоб загрузити код
- Розпакувати архів в папку з віртульним середовищем
- Зайти в папку з віртульним середовищем через командний рядок
shell```cd app```
- Активувати віртуальне середовище
shell```source bin/activate```
- Зайти в папку з додатком
shell```cd sportclub```
- Встановити залежності
shell```python -m pip install -r requiriments.txt```
- Мігрувати базу даних та апустити тестовий сервер
shell```
python ./manage.py migrate
python ./manage.py runserver
```
