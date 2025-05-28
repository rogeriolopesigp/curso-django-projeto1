from django.urls import path
# from recipes.views import home
from . import views

urlpatterns = [
    path('', views.RecipeListViewHome.as_view(), name='recipes-home'), # Home
    path('recipes/search/', views.RecipeListViewSearch.as_view(), name='recipes-search'),
    path('recipes/category/<int:category_id>/', views.RecipeListViewCategory.as_view(), name='recipes-category'),    
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipes-recipe'),
]