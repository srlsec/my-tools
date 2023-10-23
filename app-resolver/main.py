import requests
from requests.exceptions import ConnectTimeout
import pandas as pd
import argparse
import sys
import time
from datetime import datetime
from openpyxl import load_workbook
from concurrent.futures import ThreadPoolExecutor

resolved_apps = []

# Banner
def banner():
    # https://patorjk.com/software/taag/#p=testall&f=Graffiti&t=cobratoxin
    dec = "\n| Resolve apps |"
    banner="""
                                              _                
                                             | |               
   __ _ _ __  _ __ ______ _ __ ___  ___  ___ | |_   _____ _ __ 
  / _` | '_ \| '_ \______| '__/ _ \/ __|/ _ \| \ \ / / _ \ '__|
 | (_| | |_) | |_) |     | | |  __/\__ \ (_) | |\ V /  __/ |   
  \__,_| .__/| .__/      |_|  \___||___/\___/|_| \_/ \___|_|   
       | |   | |                                               
       |_|   |_| Developed by: Sarathlal_Srl | GitHub: @srlsec                                               
                    
        """
    print(dec + banner)

def app_resolve(l):
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    try:
        r = requests.get(l, allow_redirects=True, headers=headers, timeout=(50))

        data = {
                        "url": l,
                        "resolved_url": r.url,
                        "s_code": r.status_code,
                    }

    except ConnectTimeout:
        data = {
                        "url": l,
                        "resolved_url": "",
                        "s_code": "",
                    }

    except ConnectionError:
        print('ConnectionError:')
        data = {
                        "url": l,
                        "resolved_url": "",
                        "s_code": "",
                    }

    except ConnectionRefusedError:
        print('ConnectionRefusedError:')
        data = {
                        "url": l,
                        "resolved_url": "",
                        "s_code": "",
                    }
    
    except:
        data = {
                        "url": l,
                        "resolved_url": "",
                        "s_code": "",
                    }

    resolved_apps.append(data)
    print(data)


def main():
    # parser = argparse.ArgumentParser(description=f'Web App resolver')
    # parser.add_argument('-i', '--input', type=str, default='target')
    # parser.add_argument('-o', '--output', type=str, help='The output file to store the results')

    # try:
    #     args = parser.parse_args()
    # except SystemExit:
    #     sys.exit()
    
    # input_list = args.input
    # output = args.output

    lists = 'apps.txt'
    thread = 10
    try:
        domain = lists.replace('"','')
        process = open(domain, 'r').read().splitlines()
        with ThreadPoolExecutor(max_workers=int(thread)) as e:
            [e.submit(app_resolve, l) for l in process]
    except:
          print('Incorrect')

    df = pd.DataFrame(resolved_apps)
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