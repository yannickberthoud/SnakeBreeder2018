from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(initial='Votre nom', required = True, error_messages={'required': 'Champs obligatoire'})
    email = forms.EmailField(help_text='Saississez une adresse e-mail valide.', required = True, error_messages={'required': 'Champs obligatoire'})
    comment = forms.CharField(widget=forms.Textarea, required = True, error_messages={'required': 'Champs obligatoire'})
    