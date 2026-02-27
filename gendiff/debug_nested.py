from gendiff import generate_diff
import os
import difflib

def debug():
    file1 = os.path.join('tests', 'fixtures', 'nested_file1.json')
    file2 = os.path.join('tests', 'fixtures', 'nested_file2.json')
    
    result = generate_diff(file1, file2)
    
    expected_path = os.path.join('tests', 'test_data', 'expected_nested_result.txt')
    with open(expected_path, 'r') as f:
        expected = f.read()
    
    # Разбиваем на строки
    result_lines = result.splitlines()
    expected_lines = expected.splitlines()
    
    print(f"Всего строк в RESULT  : {len(result_lines)}")
    print(f"Всего строк в EXPECTED: {len(expected_lines)}")
    print("\n" + "="*80)
    
    # Используем difflib для показа различий
    diff = difflib.unified_diff(
        expected_lines, 
        result_lines,
        fromfile='expected',
        tofile='result',
        lineterm=''
    )
    
    print('\n'.join(list(diff)[:50]))  # Первые 50 строк различий
    
    print("\n" + "="*80)
    print("ПЕРВЫЕ 10 СТРОК КАЖДОГО ФАЙЛА:")
    print("="*80)
    for i in range(min(10, len(result_lines), len(expected_lines))):
        if result_lines[i] != expected_lines[i]:
            print(f"\nСтрока {i}:")
            print(f"RESULT  : {repr(result_lines[i])}")
            print(f"EXPECTED: {repr(expected_lines[i])}")
        else:
            print(f"Строка {i}: OK")

if __name__ == '__main__':
    debug()