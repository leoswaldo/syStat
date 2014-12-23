#!/python3/bin/python3

import sys
import getopt
import time
import datetime
import socket
import smtplib
from email.mime.text import MIMEText
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
        elif(opt in '--users'):
            global users
            users = True
            show_all_sections = False


## Function: write_to_log
#  Description: send output to log file
def write_to_log():
    # Open scope for global vars
    global sections
    # prepare timestamp for log filename
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).\
        strftime('%Y-%m-%d_%H:%M:%S')
    with open('logs/systat_' + timestamp, 'w') as log_file:
        log_file.write(sections)
    log_file.close()


## Function: send_mail
#  Description: send output to mail
def send_mail():
    global sections, mail_to
    msg = MIMEText(sections)

    # Prepare subject of mail
    fqdn = socket.getfqdn()
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).\
        strftime('%Y-%m-%d_%H:%M:%S')
    subject = 'syStat generated on %s at %s' % (fqdn, timestamp)
    sender = 'syStat@' + fqdn

    # Define headers of mail
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = mail_to

    # Send the message via our own SMTP server.
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()


## Function: deliver_output
#  Description: based on the args, send the output to corresponding destinations
def deliver_output():
    # Open scope for global vars
    global stdout, log, mail, sections
    if(stdout):
        print(sections)
    if(log):
        write_to_log()
    if(mail):
        send_mail()


## Function: generate_content
#  Description: Based on the args, this function will trigger the functions to
#  generate every status section content, and append it to the final result
def generate_content():
    # By default syStat shows all status sections, but in case at least one
    # is passed the program
    # Open scope for global vars
    global show_all_sections, os, cpu, memory, disk, network, process
    global users, sections

    # Create the section_generator object to generar each section
    section_generator = SectionsGenerator()

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
        sections += section_generator.generate_process_section()
    if(show_all_sections or users):
        # call to generate the status section
        sections += section_generator.generate_users_section()


if(__name__ == '__main__'):
    # options to be catched by the script
    longstyle_options = ['stdout', 'log', 'mail=', 'os', 'cpu', 'memory',
        'disk', 'network', 'process', 'users']

    # read args sent to systat
    options, reminder = getopt.gnu_getopt(sys.argv[1:], '', longstyle_options)
    # to easily determine if the user wants to see all status section
    show_all_sections = True
    # Initialize global vars
    os = cpu = memory = disk = network = process = users = False
    log = stdout = mail = False
    mail_to = sections = ''
    # inspect options sent to systat
    discover_args(options)
    # generate status content for sections
    generate_content()
    # send the output to corresponding destinations
    deliver_output()
