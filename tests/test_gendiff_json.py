import os
import json
import pytest
from gendiff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'test_data', file_name)


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def test_json_nested():
    file1 = get_fixture_path('nested_file1.json')
    file2 = get_fixture_path('nested_file2.json')
    
    result = generate_diff(file1, file2, 'json')
    
    # Проверяем, что результат - валидный JSON
    parsed = json.loads(result)
    assert isinstance(parsed, list)
    assert len(parsed) > 0


def test_json_flat():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    
    result = generate_diff(file1, file2, 'json')
    
    parsed = json.loads(result)
    assert isinstance(parsed, list)
    
    # Проверяем структуру для плоских файлов
    for item in parsed:
        assert 'key' in item
        assert 'type' in item


def test_json_with_yaml():
    file1 = get_fixture_path('nested_file1.yml')
    file2 = get_fixture_path('nested_file2.yml')
    
    result = generate_diff(file1, file2, 'json')
    
    parsed = json.loads(result)
    assert isinstance(parsed, list)
