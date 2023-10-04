from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

handler404 = 'bookings.views.custom_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("bookings.urls"), name="bookings_urls"),
    path('accounts/', include('allauth.urls')),
]
