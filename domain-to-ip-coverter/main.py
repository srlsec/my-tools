import os, requests, sys, time
from concurrent.futures import ThreadPoolExecutor
from socket import gethostbyname
from datetime import datetime
import pandas as pd

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


def domaintoip(i):
    try:
        ip = gethostbyname(i)
        # open('ips.txt', 'a').write(ip + '\n')
    except:
        ip = "Error"
    
    data = {
                        "domain": i,
                        "ip": ip,
                    }
    
    output_data.append(data)
    print(data)

def main():
    lists = 'domains.txt'
    thread = 10
    try:
        domain = lists.replace('"','')
        process = open(domain, 'r').read().splitlines()
        with ThreadPoolExecutor(max_workers=int(thread)) as e:
            [e.submit(domaintoip, i) for i in process]
    except:
          print('Incorrect')
    
    df = pd.DataFrame(output_data)
    df.to_excel(f'output.xlsx', header=True)

if __name__ == "__main__":
    try :
        start = time.time()
        banner()

        main()
        
        now = datetime.now()
        end = time.time()
        hours, rem = divmod(end-start, 3600)
        minutes, seconds = divmod(rem, 60)

        print(now.strftime('\n' + "=============== COMPLETED - %d/%m/%Y %H:%M:%S")+  " {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds)  + ' ===============' + '\n')

    except KeyboardInterrupt:
        print(f'\nKeyboard Interrupt.\n')
        sys.exit(130)