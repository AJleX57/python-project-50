import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str, help='first file')
    parser.add_argument('second_file', type=str, help='second file')
    
    args = parser.parse_args()
    # Пока просто выводим аргументы, потом здесь будет логика сравнения
    print(f'Comparing {args.first_file} and {args.second_file}')


if __name__ == '__main__':
    main()
