from gendiff import generate_diff
from gendiff.diff_tree import build_diff
from gendiff.parser import parse_file
import json
import os

def debug_order():
    file1 = os.path.join('tests', 'fixtures', 'nested_file1.json')
    file2 = os.path.join('tests', 'fixtures', 'nested_file2.json')
    
    data1 = parse_file(file1)
    data2 = parse_file(file2)
    
    print("DATA1 keys:", list(data1.keys()))
    print("DATA2 keys:", list(data2.keys()))
    print("\n")
    
    diff = build_diff(data1, data2)
    
    print("DIFF STRUCTURE:")
    print(json.dumps(diff, indent=2, default=str))
    
    print("\n" + "="*50)
    print("FULL DIFF TREE:")
    
    def print_node(node, depth=0):
        indent = '  ' * depth
        print(f"{indent}Key: {node['key']}, Type: {node['type']}")
        if node['type'] == 'nested':
            for child in node['children']:
                print_node(child, depth + 1)
    
    for node in diff:
        print_node(node)

if __name__ == '__main__':
    debug_order()