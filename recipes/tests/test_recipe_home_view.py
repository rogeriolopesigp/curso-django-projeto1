from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase
from unittest.mock import patch
    
class RecipeHomeViewsTest(RecipeTestBase):

    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes-home'))
        self.assertIs(view.func.view_class, views.RecipeListViewHome)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes-home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes-home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes-home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']

        self.assertIn('Recipe Title', content)
        self.assertIn('10  Minutos', content)
        self.assertEqual(len(response_context_recipes), 1)    

    def test_recipe_home_template_doesnt_load_when_not_published(self):
        self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes-home'))
        content = response.content.decode('utf-8')

        self.assertIn('', content)

    @patch('recipes.views.PER_PAGE', new=3)
    def test_recipe_home_pagination(self):
        for i in range(9):
            kwargs = { 'author_data': {'username': f'user{i}'}, 'slug': f'exemplo{i}'}
            self.make_recipe(**kwargs)

        response = self.client.get(reverse('recipes-home'))
        recipes = response.context['recipes']
        paginator = recipes.paginator

        self.assertEqual(paginator.num_pages, 3)
        self.assertEqual(len(paginator.get_page(1)), 3)
        self.assertEqual(len(paginator.get_page(2)), 3)
        self.assertEqual(len(paginator.get_page(3)), 3)

    @patch('recipes.views.PER_PAGE', new=3)
    def test_invalid_page_query_uses_page_one(self):
        for i in range(9):
            kwargs = { 'author_data': {'username': f'user{i}'}, 'slug': f'exemplo{i}'}
            self.make_recipe(**kwargs)

        response = self.client.get(reverse('recipes-home') + '?page=3e3e')
        self.assertEqual(response.context['recipes'].number, 1)
