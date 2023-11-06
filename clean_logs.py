'''
Explenation goes here
'''

def read_log (file: str) -> list:

    with open(file, 'r') as f:
        lines = f.readlines()
        lines_to_delete = []
        i = 0

        while i <= len(lines)-2:

            line1 = lines[i]
            line2 = lines[i+1]
            
            if line1[37:] == line2[37:]:
                # if lines match do something
                # print(line1[37:], line2[37:])
                lines_to_delete.append(i)
                # advance one line
                i += 1
            elif line1[37:] != line2[37:]:
                # if lines don't match advance one line
                i += 1

    return lines, lines_to_delete


def clean_log(lines: list, list_of_lines: list, file: str):
    with open(file, 'w') as f:
        for number, line in enumerate(lines):
            if number not in list_of_lines:
                f.write(line)


def main():

    testfile = 'E:/Python Tools/Clean Logs/clean_logs/28102023Classix.asc'

    lines, lines_to_delete = read_log(testfile)
    clean_log(lines, lines_to_delete, testfile)



if __name__ == "__main__":
    main()