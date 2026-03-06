from gendiff.parser import parse_file
from gendiff.diff_tree import build_diff
from gendiff.formatters import apply_format


def generate_diff(file_path1: str, file_path2: str, format_name='stylish') -> str:
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    
    diff = build_diff(data1, data2)
    return apply_format(diff, format_name)


__all__ = ('generate_diff',)
