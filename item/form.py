from django import forms
from category.models import Category
from django.contrib.auth.models import User
from .models import Item
from datetime import datetime
from cloudinary.forms import CloudinaryFileField


class ItemForm(forms.ModelForm):
    name = forms.CharField(label='Item Name', max_length=100)
    category = forms.ModelChoiceField(
        label='Category',
        queryset=Category.objects.all()
    )
    description = forms.CharField(label='Description', max_length=1000)
    price = forms.DecimalField(
        label='Price (£)', max_digits=10, decimal_places=2
        )
    quantity = forms.IntegerField(label='Quantity')
    image = CloudinaryFileField(label='Image', required=False)
    purchase_date = forms.DateField(
        label='Purchase Date',
        widget=forms.DateInput(attrs={'type': 'date', 'max': datetime.now().date()})
    )

    class Meta:
        model = Item
        fields = ['category', 'name', 'description', 
                  'price', 'quantity', 'image', 'purchase_date']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ItemForm, self).__init__(*args, **kwargs)
        if self.user:
            self.fields['user_id'] = forms.ModelChoiceField(
                queryset=User.objects.filter(id=self.user.id)
            )
        if self.instance and self.instance.pk:
            self.fields['image'].widget = forms.widgets.FileInput()
            if self.instance.image:
                self.fields['image'].help_text = (
                    f'<img src="{self.instance.image.url}" alt="{self.instance.name}" '
                    'style="max-width: 200px; max-height: 200px;" />'
                )

    def __str__(self):
        return self.name

