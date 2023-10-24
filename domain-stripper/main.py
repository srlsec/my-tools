from urllib.parse import urlparse, parse_qs
import tldextract
import os, sys, time
import argparse
from datetime import datetime
import pandas as pd


def exctract_host(input_list, output):
    with open(input_list, 'r') as f:
        lines = f.read().splitlines()

    hosts = []

    for i, line in enumerate(lines, start=1):
        url = line.strip()
        parsed_url = urlparse(url)

        ext = tldextract.extract(url)

        domain = ext.domain
        main_domain = ext.registered_domain
        
        suffix = ext.suffix
        sub_domain = ext.subdomain
        hostname = parsed_url.hostname
        netloc = parsed_url.netloc
        scheme = parsed_url.scheme
        port = parsed_url.port
        if port == None:
            if scheme == 'http':
                port = '80'
            if scheme == 'https':
                port = '443'
        endpoint = parsed_url.path
        query = parsed_url.query
        path = os.path.dirname(endpoint)

        dict_result = parse_qs(parsed_url.query, keep_blank_values=True)

        # print("URL : " + app)
        print("Protocol : " + scheme)
        print("Domain : " + domain)
        print("TLD : " + suffix)
        print("Domain with tld : " + main_domain)
        # print("Hostname : " + hostname)
        print("Sub domain : " + sub_domain)
        print("netloc : " + netloc)
        print("Port : " + str(port))
        print("Path : " + path)
        print("Path with filename : " + endpoint)
        print("Querystring : " + query)
        print("Separate Querystring : " + str(dict_result))

        # with_path = '/'.join(endpoint.split('/')[:-1])
        # print(with_path)
        # print(endpoint.split('/')) 

        hosts.append(hostname)

    new_hosts = [*set(hosts)]

    with open(output, 'w') as f:
        for r in new_hosts:
            f.write(f"{r}\n")



output_data = []

# Banner
def banner():
    dec = "\n| Resolve apps |"
    banner="""
 __   __                       ___  __        __      __   __             ___  __  ___  ___  __  
|  \ /  \  |\/|  /\  | |\ | __  |  /  \ __ | |__) __ /  ` /  \ |\ | \  / |__  |__)  |  |__  |__) 
|__/ \__/  |  | /~~\ | | \|     |  \__/    | |       \__, \__/ | \|  \/  |___ |  \  |  |___ |  \ 
                                                                                                 
Developed by: Sarathlal_Srl | GitHub: @srlsec                                                                                               
        """
    print(dec + banner)


def domainstripp(input_list):
    with open(input_list, 'r') as f:
        lines = f.read().splitlines()

    hosts = []

    for i, line in enumerate(lines, start=1):
        url = line.strip()
        parsed_url = urlparse(url)

        ext = tldextract.extract(url)

        domain = ext.domain
        main_domain = ext.registered_domain
        
        suffix = ext.suffix
        sub_domain = ext.subdomain
        hostname = parsed_url.hostname
        netloc = parsed_url.netloc

        dict_result = parse_qs(parsed_url.query, keep_blank_values=True)

        # print("Domain : " + domain)
        # print("TLD : " + suffix)
        # print("Domain with tld : " + main_domain)
        # print("Sub domain : " + sub_domain)
        # print("netloc : " + netloc)

        sub = ''
        if sub_domain != '':
            sub = url

        data = {        
                        "url": url,
                        "tld": suffix,
                        "domain_with_tld": main_domain,
                        "subdomain": sub_domain,
                        "sub": sub,
                    }

        print(data)
        output_data.append(data)


def main():
    input_list = 'domains.txt'
    
    domainstripp(input_list)
    
    df = pd.DataFrame(output_data)
    df.to_excel(f'output.xlsx', header=True)

if __name__ == "__main__":
    try :
        start = time.time()
        banner()

        print(datetime.now().strftime( "================ STARTED - %d/%m/%Y %H:%M:%S 00:00:00:00 ================") + '\n')

        main()
        
        now = datetime.now()
        end = time.time()
        hours, rem = divmod(end-start, 3600)
        minutes, seconds = divmod(rem, 60)

        print(now.strftime('\n' + "=============== COMPLETED - %d/%m/%Y %H:%M:%S")+  " {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds)  + ' ===============' + '\n')

    except KeyboardInterrupt:
        print(f'\nKeyboard Interrupt.\n')
        sys.exit(130)