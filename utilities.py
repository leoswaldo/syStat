#!/python3/bin/python3

import subprocess


## Function: run_command
#  Description: call the command in the os and return the stdout and stderr,
#      or error message in case an exception is caught
#  Parameters: command
#      command: command to run in the os, it should be a list
#        (the command and its parameters) E.g.: ['ps', 'aux']
def run_command(command):
    # status of running the  command (0= sucess, 1= fail)
    status = 0
    # call the command and catch the output in using the comminicate()
    # method for Popen
    try:
        process = subprocess.Popen(command,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
    except:
        stdout = stderr = 'There was an exception running ' + str(command)
        status = 1

    return status, stdout, stderr


## Function: format_string
#  Description: give special format to lines for content of sections
#  Parameters: title, string
#      title: title for the line (appended at the beggining)
#      string: content of the line (appended at the end)
def format_string(title, string):
    # the subprocess module returns byte types, so we need to decode to utf-8
    # And add some details to the string
    string = string.decode('utf-8')
    formatted_string = title + ': ' + string
    return formatted_string


## Function: format_section
#  Description: give special format to sections
#  Parameters: section_title, section_content
#      section_title: title for the section (appended at the begginig)
#      section_content: content of the section (appended at the end)
def format_section(section_title, section_content):
    # Format: Line1: section title, Line2: content, end: two blank lines
    section = section_title + '\n'
    section += section_content
    section += '\n\n'
    return section