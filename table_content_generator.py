#!/python3/bin/python3

from prettytable import PrettyTable
import utilities


class TableContentGenerator():

    ## Method: __init__
    #  Description: initialize the class vars
    def __init__(self):
        self.content_table = None

    ## Method: generate_table
    #  Description: generate content for the table
    #  Parameters: command
    #    command: command to run in the os to get the content of the table, it
    #        should be a list (the command and its parameters)
    def generate_table(self, command):
        status, stdout, stderr = utilities.run_command(command)
        # if success running the command, otherwise else
        if(status == 0):
            # the rows are separated by  '\n' so we need to split it
            command_output = str(stdout).split('\\n')
            # Remove the headers from the output, it will always be the
            # first row
            headers = command_output.pop(0)
            # Createh the list using split(), since the rows are strings
            header_fields = str(headers).split()
            num_fields = len(header_fields)

            # initialize the table as PrettyTable to use its features with
            # headers from output, and add content
            self.content_table = PrettyTable(header_fields)
            self.add_content(command_output, num_fields)
        else:
            self.content_table = stdout

        return self.content_table

    ## Method: add_content
    #  Description: iterate through command output and add it to the table with
    #      right format
    #  Parameters: command_output, num_fields
    #      command_output: the result of running the command in the os
    #      num_fields: the ammount of fields in the tables base on the headers
    def add_content(self, command_output, num_fields):
        # we need to make sure every row in the stdout of the command run has
        # the right format, we iterate though all of them, in case they don't
        # we fix it and then add it to the table
        for output_row in command_output:
            row_fields = str(output_row).split()
            row_len = len(row_fields)

            # we need to make sure the list has appropiate fields, so the list
            # can be added to the prettytable
            if(row_len > num_fields):
                # if the list has more fields we remove all of them otu of the
                # limits and add them to the last field
                row_fields[num_fields - 1:] =\
                    ['\n '.join(row_fields[num_fields - 1:])]
            elif(row_len < num_fields):
                # if the list has less fields thant the headers we need to
                # add fields to it, we add None
                row_fields.extend([None] * (num_fields - row_len))

            # add the the row to the table, once it has been fixed
            self.content_table.add_row(row_fields)

if __name__ == '__main__':
    print('This class script should not be called as main script')
    '''
    table = TableContentGenerator()
    mytable = table.generate_table(['ps', 'aux', '--sort', '-rss'])
    print(mytable)
    '''