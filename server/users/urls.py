from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import ( 
    EmailTokenObtainPairView, 
    RegisterView,
    Loggedin,
    LogoutAPIView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name = "register"),
    path('login/', EmailTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('loggedin/', Loggedin.as_view(), name="logged_in"),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]