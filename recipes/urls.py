from django.urls import path
from . import views

'app/model_viewtype'
'recipes/recipe_detail.html'

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipes-home'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipes-detail'),
    path('recipe/create/', views.RecipeCreateView.as_view(), name='recipes-create'),
    path('recipe/<int:pk>/update/', views.RecipeUpdateView.as_view(), name='recipes-update'),
    path('recipe/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipes-delete'),
    path('about/', views.about, name='recipes-about'),
    path('search_recipes/', views.search_recipes, name='search-recipes'),
    path('category/<str:cats>/', views.category_view, name='category-view'),
]