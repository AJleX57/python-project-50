from gendiff.parser import parse_file
from gendiff.diff_tree import build_diff
from gendiff.formatters.stylish import format_stylish

def generate_diff(file_path1: str, file_path2: str, format_name='stylish') -> str:
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    
    diff = build_diff(data1, data2)
    
    if format_name == 'stylish':
        return format_stylish(diff)
    else:
        return format_stylish(diff)

__all__ = ('generate_diff',)
