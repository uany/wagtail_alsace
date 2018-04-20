from base.forms import MailchimpSignUpForm
from django.views.generic.edit import FormView, View
from django.http import JsonResponse
from django.conf import settings
from django.http import HttpResponse, HttpResponseServerError

import requests
from requests.auth import HTTPBasicAuth

class MailchimpSignUpView(FormView):
    template_name = 'tags/mailchimp_form.html'
    form_class = MailchimpSignUpForm
    success_url = '/'

    def form_valid(self, form):
        f = super().form_valid(form)
        url = '{}/{}/{}/{}'.format(settings.MAILCHIMP_API_URL, 'lists', settings.MAILCHIMP_LIST_ID, 'members')

        # Make call to mailchimp
        mce_request = requests.post(url,
                                    json={
                                        "email_address": form.data['email'],
                                        "status": "subscribed"
                                    },
                                    auth=HTTPBasicAuth('wagtail', settings.MAILCHIMP_API_KEY))

        return JsonResponse(mce_request.json(),
                            status=mce_request.status_code)

class FacebookWebhook(View):

    def get(self, request, *args, **kwargs):
        mode = self.request.GET.get('hub.mode')
        challenge = self.request.GET.get('hub.challenge')
        verify_token = self.request.GET.get('hub.verify_token')

        if mode == 'subscribe' and verify_token == settings.FB_VERIFY_TOKEN:
            return HttpResponse(challenge)
        else:
            return HttpResponseServerError()


