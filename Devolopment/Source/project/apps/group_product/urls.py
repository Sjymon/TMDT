from django.conf.urls import url

from .views import ViewGroupProduct, AddGroupProduct, DetailGroupProduct, EditGroupProduct, DeleteGroupProduct

urlpatterns = [
    url(r'^$', ViewGroupProduct.as_view(), name='group_product'),	
    url(r'^add/$', AddGroupProduct.as_view(), name='add'),	
    url(r'^detail/(?P<pk>.*)/$', DetailGroupProduct.as_view(), name='detail'), 
    url(r'^edit/(?P<pk>.*)/$', EditGroupProduct.as_view(), name='edit'), 
    url(r'^delete/(?P<pk>.*)/$', DeleteGroupProduct.as_view(), name='delete'), 
]