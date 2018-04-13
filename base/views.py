from base.forms import MailchimpSignUpForm
from django.views.generic.edit import FormView


class MailchimpSignUpView(FormView):
    template_name = 'tags/mailchimp_form.html'
    form_class = MailchimpSignUpForm
    success_url = '/thanks/'

    def form_valid(self, form):

        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        return super().form_valid(form)