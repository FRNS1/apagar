import requests
import json

class ferramentas:

    def ConsomeApi(estado_escolhido):
        lista_cidades = []
        response = requests.get('http://apiadvisor.climatempo.com.br/api/v1/locale/city?country=BR&token=a07dd1dbb3245c8ec4172b292494b39b')
        json_bytes = response.content
        json_str = json_bytes.decode('utf-8')
        json_obj = json.loads(json_str)
        for cidade in json_obj:
            estado_ = cidade['state']
            if estado_escolhido == estado_:
                lista_cidades.append(cidade['name'])
        return lista_cidades
