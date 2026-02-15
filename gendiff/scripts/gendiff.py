import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str, help='first file')
    parser.add_argument('second_file', type=str, help='second file')
    parser.add_argument('-f', '--format', type=str, 
                        default='stylish',  # значение по умолчанию
                        help='set format of output (default: stylish)')
    
    args = parser.parse_args()
    
    # Пока просто выводим информацию
    print(f"Comparing {args.first_file} and {args.second_file}")
    print(f"Output format: {args.format}")


if __name__ == '__main__':
    main()
