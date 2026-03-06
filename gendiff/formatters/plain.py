def stringify(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def build_path(parts):
    return '.'.join(parts)


def iter_plain(diff, path_parts):
    lines = []
    sorted_diff = sorted(diff, key=lambda x: x['key'])
    
    for node in sorted_diff:
        key = node['key']
        type_ = node['type']
        current_path = path_parts + [key]
        full_path = build_path(current_path)
        
        if type_ == 'nested':
            lines.extend(iter_plain(node['children'], current_path))
        elif type_ == 'added':
            val = stringify(node['value'])
            lines.append(f"Property '{full_path}' was added with value: {val}")
        elif type_ == 'removed':
            lines.append(f"Property '{full_path}' was removed")
        elif type_ == 'changed':
            old_val = stringify(node['old_value'])
            new_val = stringify(node['new_value'])
            lines.append(f"Property '{full_path}' was updated. From {old_val} to {new_val}")
    
    return lines


def format_plain(diff):
    lines = iter_plain(diff, [])
    return '\n'.join(lines)
