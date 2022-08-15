from django.shortcuts import render
from .models import Contact, DMCA, PrivacyPolicy, TermsOfUse, AboutUs
from django.views.generic import TemplateView

class ContactView(TemplateView):

    model = Contact
    fields = '__all__'

    template_name = 'extras/contact.html'


class DmcaView(TemplateView):

    template_name = 'extras/dmca.html'
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        dmca = DMCA.objects.all()
        context['dmca'] = dmca
        
        return context

class PrivacyView(TemplateView):

    template_name = 'extras/privacy.html'
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        privacy_policy = PrivacyPolicy.objects.all()
        context['privacy_policy'] = privacy_policy
        
        return context

class TermsView(TemplateView):

    template_name = 'extras/terms.html'
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        terms_of_use = TermsOfUse.objects.all()
        context['terms_of_use'] = terms_of_use
        
        return context


class AboutView(TemplateView):

    template_name = 'extras/about.html'
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        about_us = AboutUs.objects.all()
        context['about_us'] = about_us
        
        return context










