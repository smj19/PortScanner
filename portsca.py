#! /usr/bin/env python2.7


import subprocess
import argparse
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser("Checks for active ports on the given host")
parser.add_argument('host', help=' The IP address of the host')
parser.add_argument('--all',action='store_true', help='Scan all 65536 ports')
parser.add_argument('--range',action='store_true',help='Specify the range of ports in the format start-end')

args = parser.parse_args()

def verboseprint(*args):
  for arg in args:
    print arg,
  print


if args.all:
  verboseprint("Scanning all 65536 ports... Please note, it is takes a long time to scan all 65536 ports")
  nmap = subprocess.Popen(['nmap', '-sS','-p 0-65535', '-oX','scanme.xml', args.host], stdout=subprocess.PIPE)
  verboseprint("Please wait.. Fetching results")

elif args.range:
  range  = raw_input("Please specify the range of ports you want to scan in the format start-end inclusive: ")
  verboseprint("Scanning the ports in the range specified...")
  nmap = subprocess.Popen(['nmap', '-sS','-p', range, '-oX','scanme.xml', args.host], stdout=subprocess.PIPE)
  verboseprint("Please wait... Fetching results")

else:
  verboseprint("Scanning the most popular 1000 ports...")
  nmap = subprocess.Popen(['nmap', '-sS', '-oX','scanme.xml', args.host], stdout=subprocess.PIPE)
  verboseprint("Please wait... Fetching results")
 
nmap.wait()
stdout,stderr = nmap.communicate()

if stderr:
  verboseprint("Error:", stderr)
else:
  pass

with open('scanme.xml','rt') as f:
  tree = ET.parse(f)


if len(tree.findall('.//port')) > 0:
  print "\nActive ports are: "
  for n in tree.iter('port'):
    port = n.attrib.get('protocol')
    id = int(n.attrib.get('portid'))
    print "Port\tPortID"
    print port,"\t",id
 
else:
  print "\nThere are no active ports on the specified host IP address\n"



