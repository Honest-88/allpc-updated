from django.urls import path, include
from extras import views
from extras.views import ContactView, DmcaView, PrivacyView, TermsView, AboutView


app_name = "extras"

#app_name = 'users'
urlpatterns = [
    path(route='extras/contact/', view=ContactView.as_view(), name='contact'),
    path(route='extras/dmca/', view=DmcaView.as_view(), name='dmca'),
    path(route='extras/privacy/', view=PrivacyView.as_view(), name='privacy'),
    path(route='extras/terms/', view=TermsView.as_view(), name='terms'),
    path(route='extras/about/', view=AboutView.as_view(), name='about'), 

]