"""
Author : nkalyan🤠
implementing Python Scripts on reading and returning the name no of mails that sent each day in week
 and plot/display them in bar graph

 I wrote code In  counting to count the number of emails sent by each distinct user.   That code may be helpful for this assignment.
"""


import matplotlib.pyplot as plt
from os import getcwd


def file_path():
    """Method that ask the users file name and returns it"""
    file_name = input("Enter the file name:")
    return file_name


def pop_values(filename):
    """Method the reads file and returning value"""
    file_name = filename
    try:                                    # look for exception
        fp = open(file_name, "r")
    except FileNotFoundError:               # if found exception display error
        print("File Does not exist, please check your file name")
        exit()
    else:                                   # if no exceptions thrown then performs this block
        with fp:
            for line in fp:
                line = line.strip("\n")
                offset = line.find("From")
                offset1 = line.find("@")
                line = line[-24:]
                offset3 = line.find("@")
                if offset == 0 and offset1 > 0 and offset3 == -1:
                    line = line[:-21]
                    yield line


def main():
    """Calls the all functions that necessary to get the output"""
    name = file_path()      # calls the file path method
    dictionary = {'Sun': 0, 'Mon': 0, 'Tue': 0, 'Wed': 0, 'Thu': 0, 'Fri': 0, 'Sat': 0}  # store the day val in dict
    value = pop_values(name)
    count = 0
    for i in value:
        if i in dictionary:
            dictionary[i] += 1
        count += len(i)
    val = dictionary.values()
    keys = dictionary.keys()
    zp = zip(dictionary.keys(), dictionary.values())
    for item in val:
        i = val
        j = keys
        plt.bar(j, i, align='center', alpha=0.5)

    plt.ylabel('Number of messages')            
    plt.title('Emails per day')
    plt.show()                                  # method that shows the bar graph of our code result


if __name__ == '__main__':
    """calls the main method"""
    main()
