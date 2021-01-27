from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='subscriptions-home'),
    path('<int:new_id>/', views.detail, name='detail'),
    path('most_views', views.most_views, name='most_views'),
    path('tag/<slug:tag_slug>/', views.home, name='post_list_by_tag'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.success),  # new
    path('cancel/', views.cancel),  # new
    path('webhook/', views.stripe_webhook), 
]