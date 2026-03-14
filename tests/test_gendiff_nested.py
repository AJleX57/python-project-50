import os
import pytest
from gendiff import generate_diff

def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'test_data', file_name)

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def get_expected_result():
    expected_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'test_data',
        'expected_nested_result.txt'
    )
    return read_file(expected_path).rstrip()

@pytest.mark.parametrize("file1,file2", [
    ("nested_file1.json", "nested_file2.json"),
    ("nested_file1.yml", "nested_file2.yml"),
])
def test_generate_diff_nested(file1, file2):
    path1 = get_fixture_path(file1)
    path2 = get_fixture_path(file2)
    
    expected = get_expected_result()
    result = generate_diff(path1, path2)
    
    assert result == expected

def test_generate_diff_nested_mixed_formats():
    json_file = get_fixture_path('nested_file1.json')
    yaml_file = get_fixture_path('nested_file2.yml')
    
    expected = get_expected_result()
    result = generate_diff(json_file, yaml_file)
    
    assert result == expected
