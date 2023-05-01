from django.http import request
from django.shortcuts import redirect, render
from django.views import View   
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from allauth.account.views import PasswordSetView,PasswordChangeView
from django.urls import reverse_lazy

# utillity

class HomeView(View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Home"
        greeting['pageview'] = "Home"        
        return render(request, 'blog/index.html',greeting)
class AboutView(View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Home"
        greeting['pageview'] = "About-us"
        return render(request,'blog/pages/about-us.html',greeting)
class ShopView(View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Home"
        greeting['pageview'] = "Shop"
        return render(request,'blog/pages/shop.html',greeting)
class BlogView(View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Home"
        greeting['pageview'] = "Blog"
        return render(request,'blog/pages/blog.html',greeting)
class BlogDetailsView(View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Home"
        greeting['pageview'] = "Blog"
        return render(request,'blog/pages/blog-details.html',greeting)
class  checkoutView(View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Home"
        greeting['pageview'] = "Checkout"
        return render(request,'blog/pages/checkout.html',greeting)
class  ContactView(View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Home"
        greeting['pageview'] = "Contact-us"
        return render(request,'blog/pages/checkout.html',greeting)


class DashboardView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Dashboard"
        greeting['pageview'] = "Dashboards"        
        return render(request, 'dashboard/dashboard.html',greeting)
class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('dashboard')
class MyPasswordSetView(LoginRequiredMixin, PasswordSetView):
    success_url = reverse_lazy('dashboard')
