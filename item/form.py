from django import forms
from category.models import Category
from django.contrib.auth.models import User


class ItemForm(forms.Form):
    category_id = forms.ModelChoiceField(queryset=Category.objects.all())
    name = forms.CharField(label='Item Name', max_length=100)
    description = forms.CharField(label='Description', max_length=1000)
    price = forms.DecimalField(label='Price', max_digits=10, decimal_places=2)
    quantity = forms.IntegerField(label='Quantity')
    created_at = forms.DateTimeField(label='Created At')
    updated_at = forms.DateTimeField(label='Updated At')
    # image = forms.ImageField(label='Image')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ItemForm, self).__init__(*args, **kwargs)
        if self.user:
            self.fields['user_id'] = forms.ModelChoiceField(
                queryset=User.objects.filter(id=self.user.id)
            )

    def __str__(self):
        return self.name