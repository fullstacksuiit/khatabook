
from django.contrib import admin
from django.urls import path
from udhaar.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_index, name="index" ),
    path('udhaar', render_transactions, name="udhaar")
]
