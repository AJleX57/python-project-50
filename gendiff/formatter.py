"""Module for formatting diff output."""


def format_value(value):
    """Format value for output."""
    if isinstance(value, bool):
        return str(value).lower()  # Преобразуем True/False в true/false
    return value


def format_diff(diff):
    """Format diff dictionary into a human-readable string."""
    lines = ['{']
    
    for key, data in diff.items():
        status = data['status']
        
        if status == 'added':
            value = format_value(data['value'])
            lines.append(f'  + {key}: {value}')
        elif status == 'removed':
            value = format_value(data['value'])
            lines.append(f'  - {key}: {value}')
        elif status == 'unchanged':
            value = format_value(data['value'])
            lines.append(f'    {key}: {value}')
        elif status == 'changed':
            old_value = format_value(data['old_value'])
            new_value = format_value(data['new_value'])
            lines.append(f'  - {key}: {old_value}')
            lines.append(f'  + {key}: {new_value}')
    
    lines.append('}')
    return '\n'.join(lines)
