from   flask  import    Flask , request
from  src .models import db_query
from  src.controllers import  main_general

app=Flask(__name__)

@app.route('/registro',methods=['POST'])
def  registro():

    dados=request.get_json()
    links=dados['links']
    discricao=dados['discricao']




    return   db_query.insert_values(links, discricao)



@app.route('/analise',methods=['POST'])
def analise():
    dados=request.get_json()
    select=dados['filter']
    links=dados['links']
   
    if select=='banco':
        res = main_general.filter_banco.filter1(links)
        print(res)
        return res

    elif select=='social':

        res=main_general.filter_social.filter_rede_social(links)

        return res
    elif select=='governo':
        resposta=main_general.gov.Vali(links)

        return resposta



@app.route('/admin')
def   admin():


    return 'admin'









app.run(host='0.0.0.0',port=8080,debug=True)








