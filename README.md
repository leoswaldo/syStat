syStat
=========

syStat is a tool created to get basic status from our Linux Servers. syStat
runs an scan in the system every time it is run.

System information:
----
    - OS Details
    - CPU Usage
    - Memory
    - Disk Space
    - Network
    - Processes Running
    - Users


Status
----

Ready to be used


Usage
----

There is a set of options to used in this tool, you can find an brief
explanation below, for a more detailed explanation please got to docs.

The information could be retrived in next formats:

    --stdout : print in terminal
    --log : send output to standard log file
    --mail <mail> : send output through mail

> NOTE

> By default the tool will return status of all sections, if you need of one
> specific section you can do that by passing it(them) as parameter(s)


    --os
    --cpu
    --memory
    --disk
    --network
    --processes
    --users


Tech
------

Python3


Requirements
------
Python 3 or higher
If ther is usage of --mail parameter the server must be configure as SMTP


License
-----
"Para el pueblo"
Yes that means MIT :)


Contributors Welcome
----
> If you want to contribute to this project feel free to
> put in contact with me (lmaciasm10@gmail.com) and lets discuss
> your ideas :)
