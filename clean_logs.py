'''
Explenation goes here
'''

import os
import shutil


def read_log (file: str) -> list:

    with open(file, 'r', encoding='ANSI') as f:
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
    with open(file, 'w', encoding='ANSI') as f:
        for number, line in enumerate(lines):
            if number not in list_of_lines:
                f.write(line)


def copy_file_with_old(filename):
    # get the file name and extension
    name, ext = os.path.splitext(filename)
    # create a new file name with "_old" suffix
    new_name = name + "_old" + ext
    # copy the original file to the new file
    shutil.copyfile(filename, new_name)


def main():

    log_folder = 'E:/Python Tools/Clean Logs/clean_logs/logs'
    log_files = os.listdir('clean_logs\logs')
    
    for log_file in log_files:

        # Read in the log file to clean
        path = log_folder + '/' + log_file
        lines, lines_to_delete = read_log(path)

        if len(lines_to_delete) == 0:
            # if there are no duplicate lines do nothing
            continue
        else:
            # make a backup of the old logfile
            copy_file_with_old(path)
            # write new logfile with duplicate lines removed
            clean_log(lines, lines_to_delete, path)



if __name__ == "__main__":
    main()