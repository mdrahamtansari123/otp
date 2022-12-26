
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'NuNorm LogIn'
admin.site.site_title = 'Vikash Yadav'
admin.site.index_title = 'LogIn API'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls', namespace='accounts')),
]
