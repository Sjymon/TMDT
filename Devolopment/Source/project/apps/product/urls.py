from django.conf.urls import url

from .views import ViewProduct, AddProduct, EditProduct, DetailProduct, DeleteProduct

urlpatterns = [
    url(r'^$', ViewProduct.as_view(), name='product'),
    url(r'^add/$', AddProduct.as_view(), name='addproduct'),
    url(r'^detail/(?P<pk>.*)/$', DetailProduct.as_view(), name='detailproduct'), 
    url(r'^edit/(?P<pk>.*)/$', EditProduct.as_view(), name='editproduct'),
    url(r'^delete/(?P<pk>.*)/$', DeleteProduct.as_view(), name='deleteproduct'), 
]