from gendiff.core.parser import parse_file
from gendiff.core.diff_tree import build_diff
from gendiff.formatters import apply_format


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    diff = build_diff(data1, data2)
    return apply_format(diff, format_name)


__all__ = ('generate_diff',)
