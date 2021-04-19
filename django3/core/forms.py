from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Seu nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    titulo = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        titulo = self.cleaned_data['titulo']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome:{nome}\nEmail:{email}\nAssunto:{titulo}\nMensagem:{mensagem}'

        mail = EmailMessage(subject=titulo, body=conteudo, from_email='contato@gmail.com', to=['contato@gmail.com'], headers={'Reply-to': email})
        mail.send()
