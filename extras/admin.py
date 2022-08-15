from django.contrib import admin
from .models import Contact, DMCA, PrivacyPolicy, TermsOfUse, AboutUs
from django.utils.html import format_html


admin.site.register(Contact)
admin.site.register(DMCA)
admin.site.register(PrivacyPolicy)
admin.site.register(TermsOfUse)
admin.site.register(AboutUs)










