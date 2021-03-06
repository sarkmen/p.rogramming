"""programming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/', include('accounts.urls')),

    url(r'^$', 'blog.views.index'),
    url(r'^posts/$', 'blog.views.post_list'),
    url(r'^posts/(?P<pk>\d+)/$', 'blog.views.post_detail'),

    url(r'^posts/new/$', 'blog.views.post_new'),
    url(r'^posts/(?P<pk>\d+)/edit/$', 'blog.views.post_edit'),
    url(r'^posts/(?P<post_pk>\d+)/commment/$', 'blog.views.comment_new'),
    url(r'^posts/(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', 'blog.views.comment_edit')
]

urlpatterns += static(settings.MEDIA_URL,  document_root= settings.MEDIA_ROOT)