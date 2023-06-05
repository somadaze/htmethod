# htmethod

Just a small script I wrote in python to take a single or list of domains and query their accepted HTTP Methods.
Nothing exciting, or new, but something to help me learn.

Requires python.

Usage:

python3 htmethod.py -d [example.com]
python3 htmethod.py -d [example.com example2.com example3.com]
python3 htmethod.py -f [file with URLs]

Domain/url files should have one per line.

Bugs for sure, I'm still trying to find more ways to break it - currently if you enter a domain that your IP 
is banned from, the tool hangs, so that is the first fix to come.


