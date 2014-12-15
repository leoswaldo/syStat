#!/python3/bin/python3

import utilities
from table_content_generator import TableContentGenerator


class SectionsGenerator():

    def __init__(self):
        self.table_generator = TableContentGenerator()

    ## Method: generate_os_section
    #  Description: generate and format OS section content
    def generate_os_section(self):
        # Get content for os section
        # Next also could be by using socket.getfqdn
        fqdn_command = ['hostname', '--fqdn']
        fqdn_status, fqdn, fqdn_stderr = utilities.run_command(fqdn_command)
        # Some details about the OS
        os_command = ['cat', '/proc/version']
        os_status, os, os_stderr = utilities.run_command(os_command)
        # Give special format to results, to be appended and then return
        fqdn = utilities.format_string("Machine", fqdn)
        os = utilities.format_string('OS', os)
        os_section_content = fqdn + os
        # Give special format to section
        os_section = utilities.format_section('OS Details', os_section_content)
        return os_section

    ## Method: generate_cpu_section
    #  Description: generate and format cpu performance section
    def generate_cpu_section(self):
        cpu_command = ['top', '-bn', '1']
        # Get content for cpu section
        top_status, top, top_stderr = utilities.run_command(cpu_command)
        # Need to split the output to get the second and third line from top
        top_rows = str(top).split('\\n')
        cpu_performance = ''
        # Iterate through the content to append second and third line from top
        for line_index in range(1, 3):
            cpu_performance += top_rows[line_index] + '\n'

        # Give special format to section
        cpu_section = utilities.format_section('CPU Performance',
            cpu_performance)
        return cpu_section

    ## Method: genearte_memory_section
    #  Description: generateand format memory section
    def generate_memory_section(self):
        # Define command and headers
        mem_command = ['cat', '/proc/meminfo']
        mem_table_headers = ['Field', 'Size', 'Unit']
        # Generate table
        mem_table = self.table_generator.generate_table(mem_command,
            mem_table_headers)
        # Give special format to section
        mem_section = utilities.format_section('Memory', mem_table)
        return mem_section

    ## Method: generate_disk_section
    #  Description: generate and format disk space section
    def generate_disk_section(self):
        disk_command = ['df', '-h']
        # Generate table
        disk_table = self.table_generator.generate_table(disk_command)
        # Give special format to section
        disk_section = utilities.format_section('Disk Space', disk_table)
        return disk_section

    ## Method: generate_network_section
    #  Description: generate and format network section
    def generate_network_section(self):
        hostname_command = ['hostname', '--fqdn']
        ip_command = ['hostname', '--ip-addr']
        ports_command = ['netstat', '-taupen']
        # Get and format hostname/IP address
        hostname_status, hostname, hostname_stderr =\
            utilities.run_command(hostname_command)
        hostname = utilities.format_string('Host', hostname)
        ip_status, ip, ip_stderr = utilities.run_command(ip_command)
        ip = utilities.format_string('Default IP Address', ip)
        # Get and format ports listening, The netstat command gives an special
        # format of the table
        ports_status, ports, ports_stderr = utilities.run_command(ports_command)
        ports_table = ports.decode('utf-8')
        network_section_content = hostname + ip + ports_table
        network_section = utilities.format_section('Network',
            network_section_content)
        return network_section

    ## Method: generate_process_section
    #  Description: generate and format processes section
    def generate_process_section(self):
        processes_command = ['ps', 'aux', '--sort', '-rss']
        # Generate table
        processes_table = self.table_generator.generate_table(processes_command)
        # Give special format to processes section
        processes_section = utilities.format_section('Process Running',
            processes_table)
        return processes_section

    def generate_programs_section(self):
        pass

    def generate_users_section(self):
        pass