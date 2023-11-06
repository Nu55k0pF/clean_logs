'''
This is a sepcialised script to go through logfiles and delete duplicate Lines
'''

import os
import shutil


def read_log (file: str) -> list:
    """ Reads a log file and returns a list of lines and a list of line numbers that are to be deleted. 
    Parameters
    ----------
    file : str
        The name of the log file to be read.

    Returns
    -------
    list
        A list of two elements: a list of strings representing the lines of the log file, and a list of integers representing the line numbers that are to be deleted.
    """

    with open(file, 'r', encoding='ANSI') as f:
        lines = f.readlines()
        lines_to_delete = []
        i = 0

        while i <= len(lines)-2:

            line1 = lines[i]
            line2 = lines[i+1]
            try:
                line3 = lines[i+2]
                line4 = lines[i+3]
            except IndexError:
                line3 = "empty"
                line4 = "empty"

            try:
                    
                if line1[37:] == line2[37:]:
                    # if lines match do something
                    # print(line1[37:], line2[37:])
                    lines_to_delete.append(i)
                    # advance one line
                    i += 1
                elif line1 == line3 and line2 == line4:
                        # check for a special case
                        lines_to_delete.append(i)
                        lines_to_delete.append(i+1)
                        # advance one line
                        i += 1
                else:
                    i += 1
            except IndexError:
                pass    

    return lines, lines_to_delete


def clean_log(lines: list, list_of_lines: list, file: str):
    """ Writes the contents of a list of lines to a file, except for the lines whose numbers are in another list.

   P arameters
    ----------
    lines : list
        A list of strings representing the lines of a log file.
    list_of_lines : list
        A list of integers representing the line numbers that are to be deleted from the log file.
    file : str
        The name of the file where the cleaned log will be written.

    Returns
    -------
    None

    """

    with open(file, 'w', encoding='ANSI') as f:
        for number, line in enumerate(lines):
            # Write all lines, execpt if the line number is in the list of lines that are to be deleted
            if number not in list_of_lines:
                f.write(line)


def copy_file_with_old(filename: str):
    """
    Copies a file to a new file with the same name and _old
    Parameters
    ----------
    filename : str
        The name of the file to be copied.

    Returns
    -------
    None
    """

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