#!/usr/bin/python3

from urllib.parse import urlparse
import subprocess
import datetime
import argparse

filedir="/h/work/dns/"

# get url from cli args
parser = argparse.ArgumentParser()
parser.add_argument("url",help="url or domain to look up")
parser.add_argument("-w", "--write", help="write output to file", action="store_true")
args = parser.parse_args()

url = args.url

# format url / domain for use with dig
if url.startswith("http"):
    url = urlparse(url)
    url = url.netloc

# build filename for optional export
filename = url + "." + datetime.datetime.today().strftime('%Y%m%d') + ".txt"

#print(url)

#dig $1 any +noall +answer
#dig $1 a +noall +answer
#dig $1 ns +noall +answer
#dig $1 mx +noall +answer
#dig $1 txt +noall +answer

digcmds = ["ns","a","mx","txt","srv","soa"]

output = url + " " + datetime.datetime.today().strftime('%Y%m%d %H:%M') + ":\n\n"

for cmd in digcmds:
    output += subprocess.check_output(["dig",url,cmd,"+noall","+answer"],).decode("utf-8") 
    output += "\n"
    
if args.write:
    print("Writing to: " + filedir + filename)
    with open(filedir + filename, "w") as text_file:
        text_file.write(output)
            
   
print(output)
