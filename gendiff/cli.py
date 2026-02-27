import argparse
import sys
from gendiff import generate_diff


def main():
    
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str, help='first file')
    parser.add_argument('second_file', type=str, help='second file')
    parser.add_argument('-f', '--format', type=str,
                        default='stylish',
                        help='output format: stylish, plain, json (default: stylish)')
    
    args = parser.parse_args()
    
    try:
        diff = generate_diff(args.first_file, args.second_file, args.format)
        print(diff)
    except FileNotFoundError as e:
        print(f"Error: File not found - {e.filename}", file=sys.stderr)
        sys.exit(1)
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
