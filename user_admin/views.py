from django.shortcuts import render
from core.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, CreateView
# Create your views here.
from user_admin.forms import PostCreateForm

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'admin/add-post.html'


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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



