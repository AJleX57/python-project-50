### Hexlet tests and linter status:
[![Actions Status](https://github.com/AJleX57/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/AJleX57/python-project-50/actions)

[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=AJleX57_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=AJleX57_python-project-50)

## Описание

**gendiff** — это утилита командной строки для сравнения двух конфигурационных файлов. Программа поддерживает форматы JSON и YAML, а также три способа отображения различий: stylish, plain и json.

Проект создан в рамках обучения на Хекслете и демонстрирует:
- Работу с файловыми форматами (JSON, YAML)
- Рекурсивное сравнение вложенных структур
- Различные форматеры вывода
- Функциональный стиль программирования
- Непрерывную интеграцию (CI) с тестами и линтером

## Демонстрация работы

### Stylish формат (по умолчанию)
[![asciicast](https://asciinema.org/a/xdvoYjy4fbSH7Ygr.svg)](https://asciinema.org/a/xdvoYjy4fbSH7Ygr)

### Plain формат
[![asciicast](https://asciinema.org/a/SkJ9GzW3LkZIoAwQ.svg)](https://asciinema.org/a/SkJ9GzW3LkZIoAwQ)

### JSON формат
[![asciicast](https://asciinema.org/a/C6vVHJS0EAZpP550.svg)](https://asciinema.org/a/C6vVHJS0EAZpP550)


## Установка

```bash
# Клонируйте репозиторий
git clone https://github.com/AJleX57/python-project-50.git
cd python-project-50

# Создайте виртуальное окружение
python3 -m venv .venv
source .venv/bin/activate  # для Linux/macOS
# .venv\Scripts\activate  # для Windows

# Установите зависимости
make install