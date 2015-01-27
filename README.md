# url_to_ip.py
Python script to resolve list of URLs to IPs 

Place URLs on separate lines in a file called hosts.txt.  
Script will parse the URL and resolve the domain to an IP using urllib.
Output will be IPs in IP.txt.

Output is URL (neutered) '.' is replaced with '[dot]'.  This is to neuter the output so no accidental clicking of the potentially malicious URL in my case.  The output is formatted as:
'neutered_url|1.2.3.4'

This code was written while trying to resolve a long list of malicious URLs to IPs and is very basic.  If you have any ideas, suggestions or improvements for this, please let me know.
