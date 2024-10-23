import requests

import urllib.parse

#import dns.resolver
analise=[]

lit=['gov.ao','co.ao','gv.ao']
from  threading import  Thread

def domonio_de_terceiro(url):
    tunnel_domains=lit
    
    


    hostname = urllib.parse.urlparse(url).hostname
    for domain in tunnel_domains:
        if domain in hostname:
            

            return   url[8:]

    return False






