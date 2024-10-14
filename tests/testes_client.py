# tests/test_client.py

import unittest
from unittest.mock import patch
from cnpjData.client import *
from exceptions import RateLimitException


class TestCNPJAPIClient(unittest.TestCase):

    @patch('cnpjData.client.requests.get')
    def test_consultar_cnpj_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"cnpj": "27865757000102", "razao_social": "Test Company"}

        client = CNPJAPIClient()
        result = client.consultar_cnpj("27865757000102")
        self.assertIn("cnpj", result)
        self.assertEqual(result["cnpj"], "27865757000102")

    @patch('cnpjData.client.requests.get')
    def test_consultar_cnpj_rate_limit(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 429
        mock_response.json.return_value = {
            "status": 429,
            "titulo": "Muitas requisições",
            "detahes": "Excedido o limite máximo de 3 consultas por minuto. Liberação ocorrerá em Thu Jun 03 2021 16:15:00 GMT-0300 (Horário Padrão de Brasília)"
        }

        client = CNPJAPIClient()
        with self.assertRaises(RateLimitException):
            client.consultar_cnpj("27865757000102")

    @patch('cnpjData.client.requests.post')
    def test_validar_inscricao_suframa_success(self, mock_post):
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"cnpj": "61940292006682", "inscricao_suframa": "210140267", "ativo": True}

        client = CNPJAPIClient()
        result = client.validar_inscricao_suframa("61940292006682", "210140267")
        self.assertIn("ativo", result)
        self.assertTrue(result["ativo"])

    @patch('cnpjData.client.requests.post')
    def test_validar_inscricao_suframa_rate_limit(self, mock_post):
        mock_response = mock_post.return_value
        mock_response.status_code = 429
        mock_response.json.return_value = {
            "status": 429,
            "titulo": "Muitas requisições",
            "detahes": "Excedido o limite máximo de 3 consultas por minuto. Liberação ocorrerá em Thu Jun 03 2021 16:15:00 GMT-0300 (Horário Padrão de Brasília)"
        }

        client = CNPJAPIClient()
        with self.assertRaises(RateLimitException):
            client.validar_inscricao_suframa("61940292006682", "210140267")


if __name__ == '__main__':
    unittest.main()
