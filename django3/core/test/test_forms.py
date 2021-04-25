from django.test import TestCase
from core.forms import ContatoForm

class ContatoFormTestCase(TestCase):
    def setUp(self) -> None:
        self.nome = 'Fernando silveira'
        self.email = 'fsilveira@gmail.com'
        self.titulo = 'assuntos diversos'
        self.mensagem = 'mensagem diversas para diversas pessoas'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'titulo': self.titulo,
            'mensagem': self.mensagem,
        }

        self.form = ContatoForm(data=self.dados)

    def test_send_email(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_email()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_email()

        self.assertEquals(res1, res2)
