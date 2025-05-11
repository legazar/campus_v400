from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,label = "Nom d'utilisateur",widget = forms.TextInput(attrs = {'class':'form-control'}),required=True)
    password = forms.CharField(min_length=8,label= 'Mot de passe',widget = forms.PasswordInput(attrs = {'class':'form-control'}),required=True)

class RegsiterForm(forms.Form):
    username = forms.CharField(max_length=100,label = "Nom d'utilisateur",widget = forms.TextInput(attrs = {'class':'form-control'}),required=True)
    email = forms.CharField(label = "Adresse e-mail",widget = forms.EmailInput(attrs = {'class':'form-control'}),required=True)
    password = forms.CharField(min_length=8,label= 'Mot de passe',widget = forms.PasswordInput(attrs = {'class':'form-control'}),required=True)