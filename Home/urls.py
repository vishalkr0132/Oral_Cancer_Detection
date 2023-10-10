from Home import views
from django.conf import settings
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='Home'),
    path('image',views.image,name="image"),
    path('output',views.output,name="output"),
    # path('login',views.login,name="login"),
    path('login', views.user_login, name='user_login'),
    path('Registation',views.Registation,name="Registation"),
    path('Profile', views.Profile, name='Profile'),
   


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
