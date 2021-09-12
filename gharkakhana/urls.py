import django.conf.urls

from . import views

urlpatterns = [
    django.conf.urls.url(r'^$', views.home, name='home'),
    django.conf.urls.url(r'^login/?$', views.login, name='login'),
    django.conf.urls.url(r'^logout/?$', views.logout, name='logout'),
    django.conf.urls.url(r'^home/?$', views.home, name='home'),
    django.conf.urls.url(r'^signup/?$', views.signup, name='signup'),
    django.conf.urls.url(r'^search/?$', views.search, name='search'),
    django.conf.urls.url(r'^details/?$', views.details, name='details'),
    django.conf.urls.url(r'^savedetails/?$', views.editDetails, name='editDetails'),
    django.conf.urls.url(r'^cart/?$', views.cart, name='cart'),
    django.conf.urls.url(r'^history/?$', views.history, name='history'),
    django.conf.urls.url(r'^addtocart/?$', views.saveToCart, name='saveToCart'),
    django.conf.urls.url(r'^restprofile/?$', views.restprofile, name='restprofile'),
    django.conf.urls.url(r'^resthistory/?$', views.restaurantOrderHistory, name='resthistory'),
    django.conf.urls.url(r'^delivered/?$', views.delivered, name='delivered'),
    django.conf.urls.url(r'^addfooditem/?$', views.addfooditem, name='addfooditem'),
    django.conf.urls.url(r'^removefooditem/?$', views.removefooditem, name='removefooditem'),

    # url(r'^makepaymenet/?$'.views.makepaymenet,name='makepaymenet'),
    django.conf.urls.url(r'^restaurant/(?P<restname>[a-zA-Z0-9\s]+)/?$', views.restview, name='restview'),
]