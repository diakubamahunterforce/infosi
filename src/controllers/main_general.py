from  threading  import   Thread



from .bank_status import *
from .redes_social import *
from.infosi_gov import *
#from api_validetor import  list
import requests

# Sua chave de API
api_key = '79c01aa90bef42976c4a1a5d50dea74ef5959674e6339bfb6b84aa943e0a4056'
#url_to_scan = 'http://exemplo.com'  # URL que você deseja analisar

# Endpoint da API para análise de URLs
url = 'https://www.virustotal.com/vtapi/v2/url/report'

# Parâmetros da solicitação
def  pest(url_to_scan):
    params = {
        'apikey': api_key,
        'resource': url_to_scan,
    }

    # Fazendo a solicitação
    response = requests.get(url, params=params)

    # Verificando o status da resposta
    if response.status_code == 200:
        result = response.json()
       # print(result['scans'])
        A=result['scans']['Kaspersky']['result']
        B=result['scans']['Fortinet']['result']
        
        C=result['scans']['Dr.Web']['result']
        #D=['scans']['Google Safebrowsing']['result']
       
       
        
       # D=result['scans']['MalwareURL']['result']
      

      #  print(result['resource'])
        # for x in result:
        print (A)
        return A,B,C

    else:
        print('Erro na solicitação:', response.status_code)





class  filter_banco():
    @classmethod


    def  filter1(cls, urls):

        url_to_scan =urls
        #A=pest(url_to_scan)
        dados=bank_Angola.bank_seach_Angola(urls)
        dados1=bank_Angola.search_database(urls)
        A,B,C=pest(url_to_scan)
 
        lista={'banco':dados ,
               'denucia':dados1,
               'fortinet':B
               ,'Kaspersky':A,
               'Dr.Web':C,
               
              
              




               }
      #  print(A)
        return  lista


class filter_social():
      @classmethod
      def filter_rede_social(cls, url):
          url_to_scan =url
          A,B,C=pest(url_to_scan)
          dados = Rede_social.rede_social(url)
          dados1=Rede_social.search_database(url)

          lista = {'Rede social': dados,
                   'denucia': dados1,
                   'fortinet':A 
              , 'Kaspersky': B,
                   'BitDefender': C,
                  
                   

                   }



          return lista
      

class  gov():
    @classmethod
    def Vali(cls,url):
        dados=domonio_de_terceiro(url)
        url_to_scan =url

        A,B,C,D,=pest(url_to_scan)
        dados1=Rede_social.search_database(url)

        lista = {'governo': dados,
                   'denucia': dados1,
                   'fortinet':A 
              , 'Kaspersky': B,
                   'BitDefender': C,
                   'MalwareURL': D ,
                   'Phishing Database': ''

                   }
        return lista

        
       

        





































