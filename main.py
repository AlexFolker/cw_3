import os
from config import ROOT_DIR
from src.utils import get_filtered_list, get_sorted_list, print_from_dict, open_json_file

PATH_TO_OPERATIONS = os.path.join(ROOT_DIR, 'src', "operations.json")


def main():
    open_file = open_json_file(PATH_TO_OPERATIONS)
    filtered_list = get_filtered_list(open_file)
    sorted_list = get_sorted_list(filtered_list)
    for operation in sorted_list[:5]:
        print_from_dict(operation)


if __name__ == '__main__':
    main()
