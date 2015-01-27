import socket
from urllib.parse import urlparse
#open hosts.txt in read mode
f = open('hosts.txt','r')
#opens/creates ip.txt in write -append mode
g = open('ips.txt', 'a')
     
#read each line in hosts.txt
for line in f.read().split('\n'):

    #parses url string and stores value in o
    o=urlparse(line)

    #writes full url string for testing
    #g.write(str(o))

    #pulls out domain
    domain = o.netloc

    #print domain for testing
    #g.write(str(domain))

    #neuter url so no accidental infection
    neutered=line.replace('.', '[dot]')

    #print neutered url
    g.write(str(neutered))

    #print pipe delimiter
    g.write('|')

    try:
        #resolve domain to ip
        ip = socket.gethostbyname(domain)

        #print ip
        g.write(str(ip))

       #error handling if IP fails to resolve 
    except socket.gaierror:
        g.write('FAILED TO RESOLVE')

    #new line created for spacing        
    g.write('\n')
