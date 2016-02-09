from django.forms import ModelForm

from .models import RetailerContact


class RetailerContactForm(ModelForm):
    class Meta:
        model = RetailerContact
        fields = '__all__'
