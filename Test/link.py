import requests

import urllib.parse

#import dns.resolver
analise=[]

lit=['gv.ao']
from  threading import  Thread

def domonio_de_terceiro(url):
    tunnel_domains=lit
    
    


    hostname = urllib.parse.urlparse(url).hostname
    for domain in tunnel_domains:
        if domain in hostname:
            

            return   url[12:]

    return False








print(domonio_de_terceiro('https://www.siac.gv.ao/'))








