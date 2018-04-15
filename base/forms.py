from django import forms


class MailchimpSignUpForm(forms.Form):
    email = forms.EmailField(label='Email',
                                 max_length=256,
                                 required=True,
                                 widget=forms.EmailInput(attrs={'placeholder': 'me@email.com'}))
