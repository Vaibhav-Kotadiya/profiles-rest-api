from django.urls import path

from profiles_app.views import HelloApiView

urlpatterns = [
    path('', HelloApiView.as_view())
]
