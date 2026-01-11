from django.urls import path
from . import views
urlpatterns = [
    path("", views.AnimalView.as_view()),
    path("<int:id>/", views.AnimalDetailView.as_view()),
    path("category/", views.CategoryView.as_view()),
    path("category/<int:id>/", views.CategoryDetailView.as_view()),
]