from urllib.parse import urlparse, parse_qs
import tldextract
import os
import argparse
import sys

def exctract_app(input_list, output):
    with open(input_list, 'r') as f:
        lines = f.read().splitlines()

    apps = []

    for i, line in enumerate(lines, start=1):
        url = line.strip()
        parsed_url = urlparse(url)

        netloc = parsed_url.netloc
        scheme = parsed_url.scheme

        app = scheme + "://" + netloc
        apps.append(app)

    new_apps = [*set(apps)]

    with open(output, 'w') as f:
        for r in new_apps:
            f.write(f"{r}\n")

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

def main():
    parser = argparse.ArgumentParser(description=f'URL Extractor')
    parser.add_argument('-i', '--input', type=str, default='target')
    parser.add_argument('-o', '--output', type=str, help='The output file to store the results')

    parser.add_argument('-host', help='Whois Lookup', action='store_true')
    parser.add_argument('-app', help='Whois Lookup', action='store_true')

    try:
        args = parser.parse_args()
    except SystemExit:
        sys.exit()
    
    input_list = args.input
    output = args.output
    host = args.host
    app = args.app

    if host is True:
        exctract_host(input_list, output)
    
    if app is True:
        exctract_app(input_list, output)

if __name__ == "__main__":
    main()