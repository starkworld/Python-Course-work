"""
Created on 27 Friday feb 16:53:34 2020

@author: nkalyan🤠
        Implementing Python scripts on slicing and dicing files"""


def get_line(file_name):
    """This function opens the given file and reads it and yield each number of values at a time,
                or raise exception if there is no such files exist"""

    try:
        """Checks for error"""
        fp = open(file_name, 'r')

    except FileNotFoundError:
        print(f"Cannot open {file_name}  plz check.")

    else:
        """Perform the task for opening file and yields each values"""
        with fp:
            for each_line in fp:
                string_name = 'X-DSPAM-Confidence:'
                if each_line.find(string_name) >= 0:
                    number = each_line[len(string_name):]
                    yield number


def check_number(number):
    """This function checks the input value is correct or not
                and return the floating value if correct input"""
    try:
        float_val = float(number)

    except ValueError:
        return None

    else:
        return float_val


def get_file_name():
    """This function asl the user for file and returns  it"""

    f_name = input('Input your file name: ')
    return f_name


def get_mean(list_values):
    """This function return the mean value"""

    if len(list_values) == 0:
        raise ZeroDivisionError('Maybe you input a empty file, or there is no float number in spam confidence. ')

    whole_sum = 0

    for i in list_values:
        whole_sum += i
    return whole_sum / len(list_values)


def main():
    """The main function which perform the all the function calls and return the output to the user"""

    while True:
        prompt: str = input("Input q/Q to quit, any other to continue: ")

        if prompt.lower() == 'q':
            break

        try:
            """This try block catches the error for  all the user inputs or other exceptions raised in functions and, 
                        return the type of exception if there is any otherwise perform the operations"""

            f_name = get_file_name()
            number_list = []
            line_generator = get_line(f_name)

            for item in line_generator:
                float_values = check_number(item)

                if float_values is not None:
                    number_list.append(float_values)

            mean_values = get_mean(number_list)
            print("Average spam confidence: {:.4f}".format(mean_values))

        except ZeroDivisionError as e:
            print(e)


if __name__ == '__main__':
    main()
