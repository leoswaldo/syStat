#!/python3/bin/python3

import sys
import getopt
from sections_generator import SectionsGenerator


## Function: discover_args
#  Description: Define the args passed to systat script
#  Parameters:options
#    options: args line with its corresponding values passed to systat script
def discover_args(options):
    global show_all_sections

    # We need to iterate through all options, after this we'll call later to
    # generate it status content, so we avoid generating multiple content of
    # the same section, like next: './systat.py --cpu --cpu --cpu'
    for opt, arg in options:
        if(opt in '--stdout'):
            global stdout
            stdout = True
        elif(opt in '--log'):
            global log
            log = True
        elif(opt in '--mail'):
            global mail
            global mail_to
            mail = True
            mail_to = arg
        elif(opt in '--os'):
            global os
            os = True
            show_all_sections = False
        elif(opt in '--cpu'):
            global cpu
            cpu = True
            show_all_sections = False
        elif(opt in '--memory'):
            global memory
            memory = True
            show_all_sections = False
        elif(opt in '--disk'):
            global disk
            disk = True
            show_all_sections = False
        elif(opt in '--network'):
            global network
            network = True
            show_all_sections = False
        elif(opt in '--process'):
            global process
            process = True
            show_all_sections = False
        elif(opt in '--programs'):
            global programs
            programs = True
            show_all_sections = False
        elif(opt in '--users'):
            global users
            users = True
            show_all_sections = False


## Function: generate_content
#  Description: Based on the args, this function will trigger the functions to
#  generate every status section content, and append it to the final result
def generate_content():
    # By default syStat shows all status sections, but in case at least one
    # is passed the program
    # Open scope for global vars
    global show_all_sections, os, cpu, memory, disk, network, process, programs
    global users

    # Create the section_generator object to generar each section
    section_generator = SectionsGenerator()

    # sections will store the result of all required sections
    sections = ''

    if(show_all_sections or os):
        # call to generate the status section
        sections += section_generator.generate_os_section()
    if(show_all_sections or cpu):
        # call to generate the status section
        sections += section_generator.generate_cpu_section()
    if(show_all_sections or memory):
        # call to generate the status section
        sections += section_generator.generate_memory_section()
    if(show_all_sections or disk):
        # call to generate the status section
        sections += section_generator.generate_disk_section()
    if(show_all_sections or network):
        # call to generate the status section
        sections += section_generator.generate_network_section()
    if(show_all_sections or process):
        # call to generate the status section
        pass
    if(show_all_sections or programs):
        # call to generate the status section
        pass
    if(show_all_sections or users):
        # call to generate the status section
        pass

    print(sections)


if(__name__ == '__main__'):
    # options to be catched by the script
    longstyle_options = ['stdout', 'log', 'mail=', 'os', 'cpu', 'memory',
        'disk', 'network', 'process', 'programs', 'users']

    # read args sent to systat
    options, reminder = getopt.gnu_getopt(sys.argv[1:], '', longstyle_options)
    # to easily determine if the user wants to see all status section
    show_all_sections = True
    # Initialize global vars
    os = cpu = memory = disk = network = process = programs = users = False
    # inspect options sent to systat
    discover_args(options)
    # generate status content for sections
    generate_content()
