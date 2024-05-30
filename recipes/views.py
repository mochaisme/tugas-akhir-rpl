from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Recipe, Category
from django.forms import ModelForm

def home(request):
    recipes = Recipe.objects.all().order_by('-created_at')
    context = {
        'recipes': recipes
    }
    return render(request, 'recipes/home.html', context)

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'
    ordering = ['-created_at']  # Ensure the list view is ordered by created_at

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(RecipeListView, self).get_context_data(**kwargs)
        context['cat_menu'] = cat_menu
        return context

class RecipeDetailView(DetailView):
    model = Recipe

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['title', 'description', 'category', 'recipe_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = ['title', 'description', 'category', 'recipe_image']

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author or self.request.user.is_staff

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes-home')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author or self.request.user.is_staff

def about(request):
    return render(request, 'recipes/about.html', {'title': 'About us page'})

def search_recipes(request):
    if request.method == "POST":
        searched = request.POST['searched']
        recipes = Recipe.objects.filter(title__icontains=searched)
        return render(request, 'recipes/search_recipes.html', {'searched': searched, 'recipes': recipes})
    else:
        return render(request, 'recipes/search_recipes.html', {'title': 'Search Recipes'})

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'category', 'recipe_image']

def category_view(request, cats):
    category_recipes = Recipe.objects.filter(category=cats)
    return render(request, 'recipes/category_view.html', {'cats': cats, 'category_recipes': category_recipes})
