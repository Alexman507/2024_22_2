from django import forms
from django.forms import BooleanField

from main.models import Product, Contact, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean(self):
        blacklist = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        cleaned_data = self.cleaned_data['name'] + self.cleaned_data['description']

        for b_word in blacklist:
            if b_word in cleaned_data:
                raise forms.ValidationError(
                    'Нельзя использовать запретки (ладно, можно, но не все)')

        else:
            return self.cleaned_data


class ContactForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
