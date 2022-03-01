import csv


def main():
    students_dict = read_dict("students.csv", 0)

    # Create a list of keys the length of index 0 can be compared with the
    # input length
    keys = [students_dict.keys()]
    student_name_key = 1

    i_number_input = input("Please enter an I-Number (XXXXXXXXX): ").replace("-", "")

    while i_number_input not in students_dict:
        if not isint(i_number_input):
            print("Invalid I-Number")

        elif len(i_number_input) < len(keys[0]):
            print("Invalid I-Number: too few digits")

        elif len(i_number_input) > len(keys[0]):
            print("Invalid I-Number: too many digits")

        elif i_number_input not in students_dict:
            print("No such student")

        i_number_input = input("Please enter an I-Number (XXXXXXXXX): ").replace(
            "-", ""
        )

    name = students_dict[i_number_input][student_name_key]
    print(name)


def isint(num):
    """Check if a string is an integer."

    Parameters:
        str_num: a string that will be checked for integer.

    Return:
        boolean: True or False
    """
    try:
        int(num)
        return True
    except ValueError:
        return False


def read_dict(file, key_index):
    """Read content from file and uses the item in key_index as key.

    :arg1: TODO
    :returns: TODO

    """
    file_dict = {}
    with open(file, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row in reader:
            file_dict[row[key_index]] = row

    return file_dict


if __name__ == "__main__":
    main()
