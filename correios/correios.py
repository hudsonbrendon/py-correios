import requests


class Correios(object):

    def __init__(self):
        self.__URL = 'http://api.postmon.com.br/v1/{}/{}'

    def _get_url(self, url, codigo):
        '''Retorna uma url para verificação de cep ou encomenda.'''
        return self.__URL.format(url, codigo)

    def _request(self, url, codigo):
        ''''Realiza as requisições para as urls informadas.'''
        try:
            data = requests.get(self._get_url(url, codigo)).json()
        except Exception as error:
            raise error
        return data

    def encomenda(self, codigo):
        ''''Retorna as informações referentes a encomenda informada no código.

            Parâmetros:

            - codigo: Código da encomenda, por padrão deve ser passado nesse formato: PR123456BR
        '''
        data = self._request('rastreio/ect', codigo)
        return data

    def cep(self, cep):
        '''Retorna as informações referentes ao endereço informado no CEP.

           Parâmetros:

           - cep: Número do CEP, por padrão deve ser passado nesse formato: 5917200
        '''
        data = self._request('cep', cep)
        return data
