"""
URL configuration for propertyhunt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from user.views import (
    login_view,
    logout_view,
    register_view,
    redirection,
    )

from property.views import (
    index_view,
    the_property_view,
    my_properties_view,
    edit_property_view,
    delete_property,
    create_property_view,
    )

from interest.views import show_interest, messages_owner


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', register_view, name='registration'),
    path('index/', index_view, name='index'),
    path('', redirection, name='redirection'),
    path('index/property/<int:property_id>/', the_property_view, name='the_property'),
    path('index/my_properties/', my_properties_view, name='own_properties'),
    path('index/my_properties/edit/<int:property_id>/', edit_property_view, name='edit_property'),
    path('index/my_properties/edit/<int:property_id>/delete/', delete_property, name='delete_property'),
    path('index/my_properties/create', create_property_view, name='create_property'),
    path('index/property/<int:property_id>/show_interest', show_interest, name='show_interest'),
    path('index/messages/', messages_owner, name='messages_owner'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    