from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.forms import ModelForm

from . import models

# Create your views here.
def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'recipes/home.html', context)

class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'recipes/home.html'
    cats = models.Category.objects.all()
    context_object_name = 'recipes'
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = models.Category.objects.all()
        context = super(RecipeListView, self).get_context_data(**kwargs)
        context['cat_menu'] = cat_menu
        return context
    
class RecipeDetailView(DetailView):
    model = models.Recipe
    
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    fields = ['title', 'description','category', 'recipe_image']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = ['title', 'description','category', 'recipe_image']
    
    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author or self.request.user.is_staff:
            return True
        return False
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recipes-home')
    
    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author or self.request.user.is_staff:
            return True
        return False
    
def about(request):
    return render(request, 'recipes/about.html', {'title': 'About us page'})

def search_recipes(request):
    if request.method == "POST":
        searched = request.POST['searched']
        recipes = models.Recipe.objects.filter(title__contains=searched)
        return render(request, 'recipes/search_recipes.html', {'searched': searched, 'recipes': recipes})
    else:
        return render(request, 'recipes/search_recipes.html', {'title': 'Search Recipes'})

#Ini yang terakhir

class RecipeForm(ModelForm):
    class Meta:
        model = models.Recipe
        fields = ['title', 'description', 'category', 'recipe_image']

def category_view(request, cats):
    category_recipes = models.Recipe.objects.filter(category=cats)
    return render(request, 'recipes/category_view.html', {'cats': cats, 'category_recipes': category_recipes})