from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):
    def setUp(self) -> None:
        self.dados = {
            'nome': 'Fernando cerqueira',
            'email': 'fcerqueira@gmail.com',
            'titulo': 'assuntos diversos',
            'mensagem': 'mensagem diversas para diversas pessoas',
        }
        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        return self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        newdados = {
            'nome': 'Fernando cerqueira',
            'email': 'fcerqueira@gmail.com',
        }
        self.cliente = Client()
        request = self.cliente.post(reverse_lazy('index'), data=newdados)
        return self.assertEquals(request.status_code, 200)
