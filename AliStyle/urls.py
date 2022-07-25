from django.contrib import admin
from django.urls import path
from asosiy.views import *
from userapp.views import *
from sotuvapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # asosiy url
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view()),
    path('asosiy/', AsosiyView.as_view(), name='asosiy'),
    path('bolimlar/', BolimlarView.as_view(), name='bolimlar'),
    path('bolimlar/<int:pk>/', IchkiView.as_view(), name='ichki'),
    path('ichkisi/', Page_listView.as_view(), name='ichkisi'),

                  # userapp url
    path('', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
