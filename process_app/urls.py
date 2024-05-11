from django.urls import path

from process_app.views import index

urlpatterns = [
    path('hello-world/',index,name='hello-world'),
]