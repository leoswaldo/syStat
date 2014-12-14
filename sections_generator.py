#!/python3/bin/python3

import utilities


class SectionsGenerator():

    ## Method: generate_os_section
    #  Description: generate and format OS section content
    def generate_os_section(self):
        # Get content for os section
        # Next also could be by using socket.getfqdn
        fqdn_status, fqdn, fqdn_stderr = utilities.run_command(
                ['hostname', '--fqdn'])
        # Some details about the OS
        os_status, os, os_stderr = utilities.run_command(
            ['cat', '/proc/version'])
        # Give special format to results, to be appended and then return
        fqdn = utilities.format_string("Machine", fqdn)
        os = utilities.format_string('OS', os)
        os_section_content = fqdn + os
        # Give special format to section
        os_section = utilities.format_section('OS Details', os_section_content)
        return os_section

    def generate_cpu_section(self):
        pass

    def genearte_memory_section(self):
        pass

    def genearte_disk_section(self):
        pass

    def genearte_network_section(self):
        pass

    def genearte_process_section(self):
        pass

    def genearte_programs_section(self):
        pass

    def genearte_users_section(self):
        pass