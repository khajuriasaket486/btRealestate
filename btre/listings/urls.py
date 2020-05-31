from django.urls import path
from listings import views
urlpatterns = [
    # /listings will be the url of first path
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search/', views.search, name='search'),

]