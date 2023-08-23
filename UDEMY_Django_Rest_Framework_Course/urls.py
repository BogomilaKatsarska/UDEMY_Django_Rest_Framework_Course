from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('movie/', include('watchlist_app.urls')),
    path('movie/', include('watchlist_app.api.urls')),

]
