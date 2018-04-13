from django import forms


class MailchimpSignUpForm(forms.Form):
    your_name = forms.EmailField(label='Email', max_length=256, required=True)
