import os
from gendiff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'test_data', file_name)


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def test_plain_nested():
    file1 = get_fixture_path('nested_file1.json')
    file2 = get_fixture_path('nested_file2.json')
    
    expected_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'test_data',
        'expected_plain_result.txt'
    )
    expected = read_file(expected_path).rstrip()
    
    result = generate_diff(file1, file2, 'plain')
    
    assert result == expected


def test_plain_flat():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    
    expected = """Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true"""
    
    result = generate_diff(file1, file2, 'plain')
    
    assert result == expected

