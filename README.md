# htmethod

Just a small script I wrote in python to query accepted HTTP Methods.
Nothing exciting, or new, but something to help me learn.




Usage:

python3 htmethod.py [user will be prompted for domain to query]

python3 htmethod.py -d [example.com]

python3 htmethod.py -d [example.com example2.com example3.com]

python3 htmethod.py -f [file with URLs]




Domain/url files should have one per line.


REQUIRES: Tested on python3



Bugs for sure, I'm still trying to find more ways to break it - currently if you enter a domain that your IP 
is banned from, the tool hangs, so that is the first fix to come.


