from django import forms
from .models import Customer


#In this example, we're creating a CustomerForm class that inherits from Django's built-in ModelForm class. We're specifying the Customer model as the model attribute in the Meta class, and including the name and email fields in the fields attribute.
##We're also including a custom clean_email method to check that the email address entered in the form is unique. If the email address is already in use by another Customer object, we raise a ValidationError to prevent duplicate entries.
#You can then use this form in your Django views and templates to create and update Customer objects. For example, in your views.py file:


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and Customer.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email
