

import   requests
DADOS='https://redecanais.ec'
dados=requests.get(url=DADOS,allow_redirects=True)
print(dados.url)
print(dados.history)
class  redirects():

    @classmethod

    def  Redirects(cls,url):
        dados=requests.get(urls=url,allow_redirects=True)
        return  dados.url,dados.history






