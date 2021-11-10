from django.urls import path
from homework_1 import views

urlpatterns = [
    path('', views.greeting),
    path('introduction/', views.introduction),
    path('now/', views.current_date_time),
    path('task/', views.square_of_number_dictionary),

]
