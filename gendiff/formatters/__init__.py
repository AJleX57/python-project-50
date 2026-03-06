from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain


def apply_format(diff, format_name):
    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        return format_plain(diff)
    else:
        raise ValueError(f"Unknown format: {format_name}")
