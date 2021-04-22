from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path('buyer/', views.buyer_list),
    path('buyer/<int:pk>/', views.buyer_detail),
    path('order/', views.order_list),
    path('order/<int:pk>/', views.order_detail),
    path('feedback/', views.feedback_list),
    path('feedback/<int:pk>/', views.feedback_detail),
    path('block/', views.block_list),
    path('userblocks/<int:pk>/', views.user_blocks),
    path('blocksdel/<int:pk>/<int:pk2>/', views.blocksdel),

    path('block/<int:pk>/', views.block_detail),
    path('sellertype/', views.sellertype_list),
    path('sellertype/<int:pk>/', views.sellertype_detail),
    path('seller/', views.seller_list),
    path('seller/<int:pk>/', views.seller_detail),
    path('payement_methods/', views.payement_methods_list),
    path('payement_methods/<int:pk>/', views.payement_methods_detail),
    path('profile/', views.profile_list),
    path('profile/<int:pk>/', views.profile_detail),
    path('order_items/', views.order_items_list),
    path('order_items/<int:pk>/', views.order_items_detail),
    path('available_orders/', views.available_orders),
    path('user_info/<int:pk>/', views.user_info),
    path('user/', views.user_list),
    path('accept_order/<int:pk>/', views.accept_order),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('create_account/', views.create_new_user),
    path('confirm_order/<int:pk>/', views.confirm_order),
    path('user/<int:pk>/', views.user_detail),
    path('new_user/', views.new_user),
    path('user_info/<int:pk>/', views.user_info),

]