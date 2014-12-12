#!/python3/bin/python3

import subprocess
from prettytable import PrettyTable

class TableContentGenerator():
    def generate_table(command):
        # call the command and catch the output in using the comminicate() 
        # method for Popen 
        process = subprocess.Popen(command,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        stdout_list = str(stdout).split('\\n')
        
        # Remove the headers from the output, it will always be the first row 
        headers = stdout_list.pop(0)
        # Createh the list using split(), since the rows are strings 
        headers_list = str(headers).split()
        headers_len = len(headers_list)
        
        # Create the table as PrettyTable to use its features 
        content_table = PrettyTable(headers_list)
        # One space between column edges and contents (default)
        content_table.padding_width = 1
        
        # we need to make sure every row in the stdout of the command run has the
        # right format, we iterate though all of them, in case they don't we fix it
        # and the add it to the table 
        for row in stdout_list:
            row_fields = str(row).split()
            row_len = len(row_fields)
        
            # we need to make sure the list has appropiate fields, so the list
            # can be added to the prettytable  
            if(row_len > headers_len):
                # if the list has more fields we remove all of them otu of the limits
                # and add them to the last field
                row_fields[headers_len - 1:] = ['\n '.join(row_fields[headers_len - 1:]
                    )]
            elif(row_len < headers_len):
                # if the list has less fields thant the headers we need to add fields
                # to it, we add None 
                row_fields.extend([None] * (headers_len - row_len))
        
            # add the the row to the table, once it has been fixed
            content_table.add_row(row_fields)
    
        return content_table

table = generate_table(['ps', 'aux', '--sort', '-rss'])
print(table)
