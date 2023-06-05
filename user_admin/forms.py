from django import forms
from django.forms import ModelForm
from core.models import Post



class PostCreateForm(ModelForm):
    custom_names = {'content': 'area'}
    
    def add_prefix(self, field_name):
        field_name = self.custom_names.get(field_name, field_name)
        return super(PostCreateForm, self).add_prefix(field_name)
    content = forms.CharField(required=False ,widget=forms.Textarea())
    class Meta:
        model = Post
        fields = ['title','image', 'content',  'tags']