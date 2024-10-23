from urllib.parse import  urlparse
import urllib.parse
from bottle import response
from .json_file  import  json_read_file
from src.models import  db_query


class Rede_social():

    @classmethod
    def search_database(cls, urls):
        input_urls = db_query.search_data(urls)
        if input_urls == []:
            return 'Sem denucia'
        else:
            return input_urls



    @classmethod
    def rede_social(cls,url):
        lit=  ["youTube.com","facebook.com", "whatsapp.com","instagram.com","viber.c", "wechat.com", "tikTok.com","douyin.com", "qq.com"," Weibo.com","kuaishou.com","snapchat.com","qzone.com","telegram.com","interest.com", "Reddit.com","Linkedin.com","quora.com","viber.com","imo.com","line.com"," picsart.com","tikee.com","discord.com","x.com","stackexchange.com"]
       
        tunnel_domains=lit
    
    


        hostname = urllib.parse.urlparse(url).hostname
        for domain in tunnel_domains:
             if domain in hostname:

                    return   domain

        return False 






        
            

        

