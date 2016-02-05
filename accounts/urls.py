from django.conf.urls import url
from django.contrib.auth.views import login
from accounts.forms import LoginForm
from accounts import views


urlpatterns = [
    url(r'^login/$', login, kwargs = {'authentication_form': LoginForm,}),
    url(r'^profile/$', views.profile),
    url(r'^signup/$', views.signup),
    url(r'^register_success/$', views.register_success),
    url(r'^approval/(?P<activation_key>\w+)/$', views.activate),

]