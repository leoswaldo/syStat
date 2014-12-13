#!/python3/bin/python3

import subprocess


## Function: run_command
#  Description: call the command in the os and return the stdout and stderr,
#      or error message in case an exception is caught
#  Parameters: command
#      command: command to run in the os
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