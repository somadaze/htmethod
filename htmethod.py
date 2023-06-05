import argparse
import requests
from urllib.parse import urlparse

def test_http_methods(domain):
    methods = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'TRACE', 'PATCH']  # http methods

    # add "http://" if not present in the domain
    if not domain.startswith('http://') and not domain.startswith('https://'):
        domain = 'http://' + domain

    # extract the scheme (http/https) and netloc (domain)
    parsed_url = urlparse(domain)
    scheme = parsed_url.scheme
    netloc = parsed_url.netloc

    try:
        results = []
        for method in methods:
            url = f'{scheme}://{netloc}'
            response = requests.request(method, url)

            # filter out 4xx status codes
            if response.status_code >= 400 and response.status_code < 500:
                continue

            results.append(f'{method}({response.status_code})')

        result_str = ', '.join(results)
        return f'{domain} : {result_str}'  

    except requests.exceptions.RequestException:
        return f'{domain} invalid domain'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='HTTPMeth')
    parser.add_argument('-d', '--domains', nargs='+', help='domain(s) to check')
    parser.add_argument('-f', '--file', help='file containing the domains, one per line')

    args = parser.parse_args()

    if args.file:
        try:
            with open(args.file, 'r') as file:
                domains = [line.strip() for line in file if line.strip()]

            results = []
            for domain in domains:
                result = test_http_methods(domain)
                print(result)
                results.append(result)

            processed_valid_domain = any('invalid domain' not in result for result in results)

        except FileNotFoundError:
            print('file not found.')

    elif args.domains:
        results = []
        for domain in args.domains:
            domains = domain.split(',')
            for single_domain in domains:
                result = test_http_methods(single_domain.strip())
                print(result)
                results.append(result)
                if 'invalid domain' not in result:
                    break  
    else:
        while True:
            domain = input("domain(s): ")
            if not domain:
                break

            domains = domain.split(',')
            results = []

            for single_domain in domains:
                result = test_http_methods(single_domain.strip())
                print(result)
                results.append(result)

            processed_valid_domain = any('invalid domain' not in result for result in results)

            if processed_valid_domain:
                break  

