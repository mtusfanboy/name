# Лабораторная работа №4: Модули и пакеты: импорт, создание, использование

## Описание работы
В данной лабораторной работе рассматриваются принципы работы с модулями и пакетами в Python. Учащиеся изучают, как импортировать стандартные модули, создавать собственные модули и пакеты, а также использовать их для структурирования программ. Работа включает три задания:

1. **Импорт стандартных модулей**: Учащиеся импортируют модули `math` и `datetime` для выполнения математических операций и работы с датой и временем.
2. **Создание и использование собственного модуля**: Учащиеся создают собственный модуль `my_module.py` и используют его в другом файле.
3. **Создание и использование пакетов**: Учащиеся создают пакет с несколькими модулями и демонстрируют их использование.

## Структура работы
```
lab4
--package
----__init__.py
----digit_module.py
----word_module.py
--my_module.py
--task1.py
--task2.py
--task3.py
```

## Содержание файлов

### `__init__.py`
```python
from .word_module import *
from .digit_module import *
```

### `digit_module.py`
```python
def multiplie_digits(a, b):
    return a * b


def devide_digits(a, b):
    return a / b
```

### `word_module.py`
```python
def capitalize_string(string: str):
    return string.capitalize()


def strip_str(string: str):
    return string.strip()
```

### `my_module.py`
```python
def adding_numders(a, b):
    return a + b
```

## Задание 1: Импорт стандартных модулей

### Реализация в `task1.py`
```python
import math
import datetime

print(math.sqrt(81))
print(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
```

## Задание 2: Создание и использование собственного модуля

### Реализация в `task2.py`
```python
from my_module import adding_numders

print(adding_numders(5, 5))
```

## Задание 3: Создание и использование пакетов

### Реализация в `task3.py`
```python
import package

print(package.capitalize_string("hello"))
print(package.devide_digits(10, 2))
```

## Заключение
В ходе выполнения лабораторной работы были освоены принципы работы с модулями и пакетами в Python. Учащиеся научились импортировать стандартные модули, создавать собственные модули и пакеты, а также использовать их для структурирования программ.