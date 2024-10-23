from urllib.parse import  urlparse
import urllib.parse
from bottle import response
from  .json_file import  json_read_file
from src .models import db_query


class bank_Angola():

    @classmethod
    def  search_database(cls,urls):
        input_urls=db_query.search_data(urls)
        if input_urls==[]:
            return  'Sem denucia'
        else:
             return  input_urls

    @classmethod
    def bank_seach_Angola(cls,url):
        tunnel_domains =json_read_file.read_json()




        hostname = urllib.parse.urlparse(url).hostname
        for domain in tunnel_domains:
            if domain in hostname:
                return  domain

        return  False





