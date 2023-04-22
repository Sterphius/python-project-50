import argparse


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.add_argument('-format', '--format', help='set format of output', required=False)

    args = parser.parse_args()
    print(args.filename, args.count, args.verbose)

    # TODO: здесь мы вызываем какой-то метод, который сравнивает 2 файла


if __name__ == '__main__':
    main()
