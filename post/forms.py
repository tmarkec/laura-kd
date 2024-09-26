# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author_name', 'body', 'image', 'color'] 

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))
      
        self.helper.layout = Layout(
            Field('author_name'),
            Field('body'),
            Field('image'),
            Field('color'),  
        )
