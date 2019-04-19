"""kirr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib import admin
# import kirr_redirect_view,KirrCBView, test_view
from shortener.views import URLRedirectView,HomeView
from django.conf.urls import url
urlpatterns = [
    #pattern matching runs from top to bottom
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    # url(r'^about123/', test_view),
    # url(r'^(?P<shortcode>[\w-]+)/$',kirr_redirect_view),
    url(r'^(?P<shortcode>[\w-]+)/$',URLRedirectView.as_view(),name='scode'),
    # url(r'^about123/', test_view),
]
