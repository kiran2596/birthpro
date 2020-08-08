from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'birthday'

urlpatterns = [
    path('create/',views.WishView.as_view(),name='wishlist'),
    path('',views.NameList.as_view(),name='viewlist'),
    path('<int:pk>/',views.BirthWishView.as_view(),name='birthlist'),
    # path('create/',views.SchoolCreateView.as_view(),name = 'create'),
    # path('update/<int:pk>/',views.SchoolUpdateView.as_view(),name= 'update'),
    # path('delete/<int:pk>/',views.SchoolDeleteView.as_view(),name= 'delete'),

]