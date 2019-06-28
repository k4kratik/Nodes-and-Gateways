from django.urls import path
from .views import Home, CreateGatewayView, CreateNodeView, SignUp, GatewayList


urlpatterns = [
    path('', Home, name='home'),
    path('create-gw/', CreateGatewayView, name='create-gateway'),
    path('create-node/', CreateNodeView, name='create-node'),
    path('accounts/signup/', SignUp.as_view(), name='signup'),
    path('gateway-list/', GatewayList, name='gateway-list'),

]
