import requests 
import pandas 

class Bit_bucket_Model():
    def __init__(self):
        self.url='https://api.bitbucket.org/2.0/repositories'

    def get(self,user):
        return requests.get(f'{self.url}/{user}')

    def make_json(self,user):
        response = self.get(user)
        return response.json()

    def status_reponse(self):
        self.status = requests.Response()
    
    def make_csv(self,user):
        response = self.get(user)
        return self.convert_json(response.content)

    def convert_json(self,json):
        arquivo = pandas.read_json(json)
        df= pandas.DataFrame(arquivo)
        print(df)
        return arquivo.to_csv('bitbucket.csv')


