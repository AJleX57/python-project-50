import json
import os
from gendiff import generate_diff


def get_fixture_path(file_name):
    """Get absolute path to fixture file."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read_file(file_path):
    """Read file content."""
    with open(file_path, 'r') as f:
        return f.read()


def test_generate_diff():
    """Test generate_diff function with flat JSON files."""
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    
    expected = read_file(os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'test_data',
        'expected_result.txt'
    ))
    
    result = generate_diff(file1, file2)
    assert result == expected


def test_generate_diff_with_same_files():
    """Test generate_diff with identical files."""
    file1 = get_fixture_path('file1.json')
    
    result = generate_diff(file1, file1)
    # Должен показать все ключи как неизменные
    assert '  - ' not in result
    assert '  + ' not in result


def test_generate_diff_with_empty_file():
    """Test generate_diff with empty JSON."""
    # Создадим временный пустой JSON
    empty_path = get_fixture_path('empty.json')
    with open(empty_path, 'w') as f:
        json.dump({}, f)
    
    file1 = get_fixture_path('file1.json')
    
    try:
        result = generate_diff(file1, empty_path)
        # Должны увидеть все ключи как удалённые
        assert '  - ' in result
    finally:
        # Удалим временный файл
        os.remove(empty_path)
