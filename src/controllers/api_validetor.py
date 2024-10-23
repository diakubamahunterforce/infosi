import requests

# Sua chave de API
api_key = '79c01aa90bef42976c4a1a5d50dea74ef5959674e6339bfb6b84aa943e0a4056'
url_to_scan = 'http://exemplo.com'  # URL que você deseja analisar

# Endpoint da API para análise de URLs
url = 'https://www.virustotal.com/vtapi/v2/url/report'

# Parâmetros da solicitação
def  list(url_to_scan):
    params = {
        'apikey': api_key,
        'resource': url_to_scan,
    }

    # Fazendo a solicitação
    response = requests.get(url, params=params)

    # Verificando o status da resposta
    if response.status_code == 200:
        result = response.json()
        #print(result)
   
        F=result['scans']['Dr.Web']
       # print(result['scans']['Fortinet'])
        print(F)

      #  print(result['scans']['BitDefender'])
      #  print(result['scans']['MalwareURL'])
       # print(result['scans']['Phishing Database'])

        # print(result)
        for x in result['scans']:
                print (x)

    else:
        print('Erro na solicitação:', response.status_code)


import requests

def get_url_report(api_key, url):
    endpoint = 'https://www.virustotal.com/vtapi/v2/url/report'
    params = {
        'apikey': api_key,
        'resource': url,
    }
    
    response = requests.get(endpoint, params=params)
    return response.json()




print(list('https://5822-102-218-85-218.ngrok-free.app/'))

