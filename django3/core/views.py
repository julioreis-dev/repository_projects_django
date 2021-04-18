from django.views.generic import TemplateView, FormView
from .models import Servico, Funcionario, Features
from .forms import ContatoForm
from django.contrib import messages
from django.urls import reverse_lazy


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionario'] = Funcionario.objects.order_by('?').all()
        context['feature'] = Features.objects.order_by('?').all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_email()
        messages.success(self.request, 'Email enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o email')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


class Erro400View(TemplateView):
    template_name = '404.html'


class Erro500View(TemplateView):
    template_name = '500.html'
