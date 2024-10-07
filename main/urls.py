
from django.urls import path,include
from . import views
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('', views.home , name="index"),
    path('project', views.blog, name ="project"),
    path('blog', views.blog, name ="blog"),
    path('portfolio',views.portfolio, name="portfolio"),

]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
