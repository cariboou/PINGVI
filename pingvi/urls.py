"""pingvi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from pingvi_app.views import home, how_to_start, specialists, get_approach, register, user_login, user_logout, load_datetimes, appointment, my_appointments


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('', home, name='home'),
    path('how_to_start/', how_to_start, name='how_to_start'),
    path('specialists/', specialists, name = 'specialists'),
    path('specialists/<int:approach_id>/', get_approach, name='get_approach'),
    path('appointment/', appointment, name='appointment'),
    path('my-appointments/', my_appointments, name='my_appointments'),
    path('ajax/load-datetimes/', load_datetimes, name='ajax_load_datetimes')
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


