def format_diff(diff):
    lines = ['{']
    
    for key, data in diff.items():
        status = data['status']
        
        if status == 'added':
            lines.append(f'  + {key}: {data["value"]}')
        elif status == 'removed':
            lines.append(f'  - {key}: {data["value"]}')
        elif status == 'unchanged':
            lines.append(f'    {key}: {data["value"]}')
        elif status == 'changed':
            lines.append(f'  - {key}: {data["old_value"]}')
            lines.append(f'  + {key}: {data["new_value"]}')
    
    lines.append('}')
    return '\n'.join(lines)
