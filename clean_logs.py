'''
Explenation goes here
'''

def clean_Log (file: str):
    with open(file, 'r+') as f:
        line1 = f.readline()
        line2 = next(f)

        while True:
            if line2 == "End of File {}".format(file):
                # Break if the end of the file is reached
                print("End of File {}\n".format(file))
                break
            elif line1[37:] == line2[37:]:
                # if lines match do something
                print(line1[37:], line2[37:])
                # advance one line
                line1, line2 = advance_line(line1, line2, f, file)
            elif line1[37:] != line2[37:]:
                # if lines don't match advance one line
                line1, line2 = advance_line(line1, line2, f, file)


def advance_line(line1, line2, fileobject, file):

    line1 = line2
    try:
        line2 = next(fileobject)
    except StopIteration:
        line2 = "End of File {}".format(file)

    return line1, line2


def main():

    testfile = 'E:/Python Tools/Clean Logs/clean_logs/28102023Classix.asc'

    clean_Log(testfile)


if __name__ == "__main__":
    main()