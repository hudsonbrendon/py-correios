import unittest
import requests_mock

from correios import Correios


class CorreiosTestCase(unittest.TestCase):

    def setUp(self):
        self.correios = Correios()

    def test_get_url(self):
        self.assertEqual(self.correios._get_url('rastreio', 'PR12345BR'),
                         'http://api.postmon.com.br/v1/rastreio/PR12345BR')

    @requests_mock.Mocker()
    def test_cep(self, request_mock):
        url = 'http://api.postmon.com.br/v1/cep/59142070'
        data = {
            'Rua': 'Hawaii',
            'Número': '160',
            'Bairro': 'Ponta Negra',
            'Cidade': 'Natal',
            'Estado': 'Rio Grande do Norte',
            'UF': 'RN',
            'CEP': '59142-070'
        }
        request_mock.get(url, json=data)
        self.assertEqual(self.correios.cep('59142070'), data)

    @requests_mock.Mocker()
    def test_encomenda(self, request_mock):
        url = 'http://api.postmon.com.br/v1/rastreio/ect/PR12345BR'
        data = {
            'Codigo': '12345',
            'Cidade': 'Natal/RN',
            'Status': 'Saiu para entrega'
        }
        request_mock.get(url, json=data)
        self.assertEqual(self.correios.encomenda('PR12345BR'), data)


if __name__ == '__main__':
    unittest.main()
