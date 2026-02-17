from gendiff.parser import parse_file
from gendiff.differ import build_diff
from gendiff.formatter import format_diff


def generate_diff(file_path1: str, file_path2: str) -> str:
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    
    diff = build_diff(data1, data2)
    return format_diff(diff)


__all__ = ('generate_diff',)
