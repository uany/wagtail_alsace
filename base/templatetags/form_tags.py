from django import template
from base.forms import MailchimpSignUpForm

register = template.Library()
# https://docs.djangoproject.com/en/1.9/howto/custom-template-tags/

@register.inclusion_tag('tags/mailchimp_form.html', takes_context=True)
def mailchimp_form(context):
    context['mailchimp_form'] = MailchimpSignUpForm()
    return context
