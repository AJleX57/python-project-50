"""Tests for gendiff package."""
import os
import pytest
from gendiff import generate_diff


def get_fixture_path(file_name):
    """Get absolute path to fixture file."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read_file(file_path):
    """Read file content."""
    with open(file_path, 'r') as f:
        return f.read()


def get_expected_result():
    """Get expected diff result."""
    expected_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'test_data',
        'expected_result.txt'
    )
    return read_file(expected_path)


# Параметризованные тесты для разных форматов
@pytest.mark.parametrize("file1,file2", [
    ("file1.json", "file2.json"),
    ("file1.yml", "file2.yml"),
    ("file1.yaml", "file2.yaml"),
])
def test_generate_diff(file1, file2):
    """Test generate_diff with different file formats."""
    path1 = get_fixture_path(file1)
    path2 = get_fixture_path(file2)
    
    expected = get_expected_result()
    result = generate_diff(path1, path2)
    
    assert result == expected


def test_generate_diff_mixed_formats():
    """Test generate_diff with mixed formats (JSON and YAML)."""
    json_file = get_fixture_path('file1.json')
    yaml_file = get_fixture_path('file2.yaml')
    
    expected = get_expected_result()
    result = generate_diff(json_file, yaml_file)
    
    assert result == expected


def test_generate_diff_with_same_files():
    """Test generate_diff with identical files."""
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file1.yml')  # Same content, different format
    
    result = generate_diff(file1, file2)
    # Должен показать все ключи как неизменные
    assert '  - ' not in result
    assert '  + ' not in result
