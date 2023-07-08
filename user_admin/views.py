from typing import Any, Dict
from django.http import HttpResponseRedirect
from django.shortcuts import render
from core.models import Post , Product,VAT,Category
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, CreateView
# Create your views here.
from user_admin.forms import PostCreateForm,TvaCreateForm,CategoryCreatForm

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'admin/add-post.html'
    success_url = 'add-post'


    def form_valid(self, form):
        form.instance.author = self.request.user
        if 'image' in self.request.FILES:
            form.image = self.request.FILES['image']
        else:
            print(self.request)

        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content','image','tags']
    template_name ='admin/add-post.html'
    success_url = 'add-post'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name','category','short_desc','long_desc','price','vat','thumbnail']
    template_name = 'admin/add-product.html'
    success_url = 'add-product'
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['tva_form'] = TvaCreateForm
        context['category_form'] = CategoryCreatForm
        context['category'] = Category.objects.all()
        context['tva'] = VAT.objects.all()
        return context
    
    def form_valid(self, form):
            return super().form_valid(form)
        
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name','category','short_desc','long_desc','price','vat','thumbnail']
    template_name = 'admin/add-product.html'
    success_url = 'add-product'
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['tva_form'] = TvaCreateForm
        context['category_form'] = CategoryCreatForm
        context['category'] = Category.objects.all()
        context['tva'] = VAT.objects.all()
        return context
    
    def form_valid(self, form):
            return super().form_valid(form)
        
        

        
def creat_tva(request):
    form_tva = TvaCreateForm(request.POST)
    if request.method == 'POST':
        if form_tva.is_valid(): 
            form_tva.save()
            return HttpResponseRedirect("add-product")
        else:
            form_tva
    context = {
        'form_tva':form_tva,
    }
    return  HttpResponseRedirect("add-product")

def creat_category(request):
    form_category = CategoryCreatForm(request.POST)
    if request.method == 'POST':
        if form_category.is_valid(): 
            form_category.save()
            return HttpResponseRedirect("add-product")
        else:
            form_category
    context = {
        'form_tva':form_category,
    }
    return HttpResponseRedirect("add-product")