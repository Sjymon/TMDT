from django.conf.urls import url

from apps.core.views import HomePageView, AdminView 

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^main/$', AdminView.as_view(), name='main'),
    

]
