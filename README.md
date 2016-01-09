# Display a list of active ports on a host

## Description
 Given an IP address as the input, this script returns a list of active ports 

## Cloning
```
git clone https://github.com/snehamj/PortScanner.git
```

## Requirements
```
python2.7 or higher
nmap
```

Install requirements with apt-get

```
sudo apt-get install nmap
```

## Usage

``` 
usage: Checks for active ports on the given host
        [-h] [--allports] [--range] host
 
 positional arguments:
   host            The IP address of the host
   
 optional arguments:
   -h, --help      show this help message and exit
   --allports      Scan all 65536 ports
   --range         Specify the range of ports in the format start-end
 ```
 
#### Example output 1) By default the most popular 1000 ports are scanned
 
 ```
root@ubuntu:/home/ubuntu/port# python portsca.py 8.8.8.8
Scanning the most popular 1000 ports...
Please wait... Fetching results

Active ports are: 
Port	PortID
tcp 	53

 ```
#### Example output 2) By specifying the argument "--range" in the command line, the port between the range specified will be scanned
 ```
root@ubuntu:/home/ubuntu/port# python portsca.py --range 108.214.113.79
Please specify the range of ports you want to scan in the format start-end inclusive: 0-2000
Scanning the ports in the range specified...
Please wait... Fetching results

There are no active ports on the specified host IP address
```
#### Example output 3) By specifying the argument "--all" in the command line, all 65535 ports will be scanned(Note: Time-consuming)
```
root@ubuntu:/home/ubuntu/port# python portsca.py --all 108.214.113.79
Scanning all 65536 ports... Please note, it is takes a long time to scan all 65536 ports
Please wait.. Fetching results

```
