from django import forms
from .models import Comment
from django.contrib.auth.models import User
from category.models import Category


class CommentForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        label='Category',
        queryset=Category.objects.all())
    comment = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 
               'rows': 3, 
               'placeholder': 'Enter your comments on your expenses here...'}))

    class Meta:
        model = Comment
        fields = ['comment', 'category']
      
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CommentForm, self).__init__(*args, **kwargs)
        if self.user:
            self.fields['user_id'] = forms.ModelChoiceField(
                queryset=User.objects.filter(id=self.user.id)
            )