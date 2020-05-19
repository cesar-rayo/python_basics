from selenium import webdriver
from custom import Custom

from unittest import mock
from unittest.mock import patch, MagicMock

import pytest
import os
import requests
import json

class TestSample():

    def test_prueba_1(self):
        entrada = {"primer_numero":12,"segundo_numero":20}
        respuesta = Custom.addition(entrada)
        assert 32 == respuesta

    def test_prueba_2(self):
        entrada = {"primer_numero":40,"segundo_numero":20}
        respuesta = Custom.addition(entrada)
        assert 60 == respuesta

    @pytest.fixture()
    def set_environment(self):
        print("Execute fixture")

    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="/home/cesar-rayo/Documents/selenium/chromedriver_81/chromedriver")
        driver.implicitly_wait(30)
        driver.maximize_window()
        yield # Break
        driver.close() # close tab
        driver.quit() # close window
        print("Test ends")

    def test_navigation(self, test_setup):
        driver.get("https://luzavargas.github.io/supermercado/")
        driver.find_element_by_xpath('//*[@id="top_nav"]/ul/li[2]/a').click()
        driver.find_element_by_id("keyword").send_keys("Something")
        driver.find_element_by_id("searchbutton").click()
        assert driver.title == "Supermercados CRAI - Productos"

    def test_navigation_2(self, test_setup):
        driver.get("https://luzavargas.github.io/supermercado/")
        driver.find_element_by_xpath('//*[@id="top_nav"]/ul/li[2]/a').click()
        driver.find_element_by_id("keyword").send_keys("Something_else")
        driver.find_element_by_id("searchbutton").click()
        assert driver.title == "Supermercados CRAI - Productos"
    
    def test_first_Test(self, set_environment):
        with patch.dict(os.environ, {'SOME_VAR': 'SOME_VALUE'}):
            assert os.environ['SOME_VAR'] == "SOME_VALUE"

    @patch.object(requests, 'post')
    def test_post_patch(self, mockpost):
        magic_value = {'registries':['data']}
        mock_response = mock.Mock()
        mockpost.return_value = mock_response
        mock_response.text = "some text"
        mock_response.json.return_value = magic_value

        url = 'https://non_existing/endpoint'
        data = {'somekey': 'somevalue'}

        response = requests.post(url, data = data)
        assert response.text == "some text"


    def test_mock_method(self):
        custom_json = "{\"key\":\"value\"}"
        response = Custom.set_custom_parameter("{\"key\":\"value\"}")
        assert "custom" in response

    def test_mock_method(self):
        custom_json = {"response":{"object":"content"}}
        Custom.porcess_json = MagicMock(return_value = custom_json)
        response = Custom.porcess_json("{\"key\":\"value\"}")
        assert response == custom_json

    @patch.object(requests, 'post')
    def test_vacio(self, mockpost):
        magic_value = {'Respuesta':0}
        mock_response = mock.Mock()
        mockpost.return_value = mock_response
        mock_response.text = "some text"
        mock_response.json.return_value = magic_value

        respuesta = Custom.check_clients('123123')
        assert "No hay registros" == respuesta

    @patch.object(requests, 'post')
    def test_muchos_registros(self, mockpost):
        magic_value = {'Respuesta':13}
        mock_response = mock.Mock()
        mockpost.return_value = mock_response
        mock_response.text = "some text"
        mock_response.json.return_value = magic_value


        respuesta = Custom.check_clients('123123')
        assert "Si hay registros" == respuesta





