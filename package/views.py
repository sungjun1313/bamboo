from django.shortcuts import render
from mysite.views import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from package.forms import CustomForm, Pack1Form, Pack2Form
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView,ListView, DeleteView
from package.models import Custom, Pack1, Pack2

# Create your views here.
class CustomView(LoginRequiredMixin, CreateView):
    template_name = 'package/custom.html'
    form_class = CustomForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CustomView, self).form_valid(form)
    def get_success_url(self):
        return reverse('package:pack1',args=(self.object.id,))

class CreatePack1(LoginRequiredMixin, CreateView):
    template_name = 'package/pack1.html'
    form_class = Pack1Form

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreatePack1, self).form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(CreatePack1, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context
    def get_success_url(self):
        return reverse('package:pack2',args=(self.kwargs['pk'],))

class CreatePack2(LoginRequiredMixin, CreateView):
    template_name = 'package/pack2.html'
    form_class = Pack2Form

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreatePack2, self).form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(CreatePack2, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context
    def get_success_url(self):
        return reverse('package:custom',)

class CustomList(LoginRequiredMixin, ListView):
    template_name = 'package/custom_list.html'

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Custom.objects.filter(owner_id = pk)

class ChangeCustom(LoginRequiredMixin, UpdateView):
    template_name = 'package/custom_change.html'
    model = Custom
    form_class = CustomForm

    def get_success_url(self):
        return reverse('package:customList', args=(self.request.user.id,))

class ChangePack1(LoginRequiredMixin, UpdateView):
    template_name = 'package/pack1_change.html'
    model = Pack1
    fields = {"p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10", "p11", "p12", "p13", "p14", "p15", "p16", "p17", "p18", "p19", "p20", "p21", "p22",}

    def get_success_url(self):
        return reverse('package:customList', args=(self.request.user.id,))

class ChangePack2(LoginRequiredMixin, UpdateView):
    template_name = 'package/pack2_change.html'
    model = Pack2
    fields = {"p23", "r23", "p24", "r24", "p25", "r25", "p26", "r26", "p27", "r27", "p28", "r28", "p29", "r29", "p30", "r30", "p31", "r31", "p32", "r32", "p33", "r33", "p34", "r34", "p35", "r35", "p36", "r36", }

    def get_success_url(self):
        return reverse('package:customList', args=(self.request.user.id,))

class AdminCreatePack1(LoginRequiredMixin, CreateView):
    template_name = 'package/pack1.html'
    form_class = Pack1Form

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(AdminCreatePack1, self).form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(AdminCreatePack1, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context
    def get_success_url(self):
        return reverse('package:customList', args=(self.request.user.id,))

class AdminCreatePack2(LoginRequiredMixin, CreateView):
    template_name = 'package/pack2.html'
    form_class = Pack2Form

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(AdminCreatePack2, self).form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(AdminCreatePack2, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context
    def get_success_url(self):
        return reverse('package:customList', args=(self.request.user.id,))

class Total(LoginRequiredMixin, DeleteView):
    model = Custom
    template_name = 'package/total.html'
