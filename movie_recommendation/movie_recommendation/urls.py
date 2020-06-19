from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    path('accounts/', include('accounts.urls')),
    path('recommender/', include('recommender.urls')),
]

urlpatterns += staticfiles_urlpatterns()   # ask django to serve the static files 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

