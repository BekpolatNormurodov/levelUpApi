from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/stories/', include('_stories.urls')),
    path('api/v1/conversation/', include('_conversation.urls')),
]