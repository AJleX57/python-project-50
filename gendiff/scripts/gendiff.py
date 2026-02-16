import argparse
import json
from gendiff.parser import parse_file


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str, help='first file')
    parser.add_argument('second_file', type=str, help='second file')
    parser.add_argument('-f', '--format', type=str,
                        default='stylish',
                        help='set format of output (default: stylish)')
    
    args = parser.parse_args()
    
    try:
        data1 = parse_file(args.first_file)
        data2 = parse_file(args.second_file)
        
        # Здесь будет логика сравнения
        print(f"File 1: {data1}")
        print(f"File 2: {data2}")
        print(f"Format: {args.format}")
        
    except FileNotFoundError as e:
        print(f"Error: File not found - {e.filename}")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == '__main__':
    main()
