from django.urls import path
from services.user_module.views import registration

urlpatterns = [
    path('registration/', registration, name='registration'),
]
