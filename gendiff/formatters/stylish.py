def format_value(value, depth):
    if isinstance(value, dict):
        indent = '    ' * depth
        lines = ['{']
        # Сортируем ключи словаря
        for key in sorted(value.keys()):
            val = value[key]
            lines.append(f'{indent}    {key}: {format_value(val, depth + 1)}')
        lines.append(indent + '}')
        return '\n'.join(lines)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)


def iter_(diff, depth):
    lines = []
    indent = '    ' * depth
    
    # СОРТИРУЕМ УЗЛЫ ПЕРЕД ВЫВОДОМ
    sorted_diff = sorted(diff, key=lambda x: x['key'])
    
    for node in sorted_diff:
        key = node['key']
        type_ = node['type']
        
        if type_ == 'nested':
            # СОРТИРУЕМ ДЕТЕЙ ТОЖЕ
            sorted_children = sorted(node['children'], key=lambda x: x['key'])
            children = iter_(sorted_children, depth + 1)
            lines.append(f'{indent}    {key}: ' + '{')
            lines.extend(children)
            lines.append(f'{indent}    ' + '}')
        elif type_ == 'added':
            val = format_value(node['value'], depth + 1)
            lines.append(f'{indent}  + {key}: {val}')
        elif type_ == 'removed':
            val = format_value(node['value'], depth + 1)
            lines.append(f'{indent}  - {key}: {val}')
        elif type_ == 'unchanged':
            val = format_value(node['value'], depth + 1)
            lines.append(f'{indent}    {key}: {val}')
        elif type_ == 'changed':
            old_val = format_value(node['old_value'], depth + 1)
            new_val = format_value(node['new_value'], depth + 1)
            lines.append(f'{indent}  - {key}: {old_val}')
            lines.append(f'{indent}  + {key}: {new_val}')
    
    return lines


def format_stylish(diff):
    # СОРТИРУЕМ ВЕРХНИЙ УРОВЕНЬ
    sorted_diff = sorted(diff, key=lambda x: x['key'])
    lines = ['{']
    lines.extend(iter_(sorted_diff, 0))
    lines.append('}')
    return '\n'.join(lines)