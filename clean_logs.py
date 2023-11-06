'''
Explenation goes here
'''

def read_log_file(file: str):
    with open(file, 'w') as f:
        line1 = f.readline()
        line2 = f.readline()

        print(line1, line2)

def main():

    testfile = 'E:/Python Tools/Clean Logs/clean_logs/28102023Classix.asc'

    read_log_file(testfile)


if __name__ == "__main__":
    main()