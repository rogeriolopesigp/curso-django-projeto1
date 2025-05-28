from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase
    
class RecipeDetailViewsTest(RecipeTestBase):

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes-recipe', kwargs={'pk': 1}))
        self.assertIs(view.func.view_class, views.RecipeDetail)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get('recipes-recipe', kwargs={'pk': 333})
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_the_correct_recipe(self):
        self.make_recipe(title='This is a detail page test')
        response = self.client.get(reverse('recipes-recipe', kwargs={'pk':1}))
        content = response.content.decode('utf- 8')

        self.assertIn('This is a detail page test', content)

    def test_recipe_detail_template_doesnt_load_when_not_published(self):
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes-recipe', kwargs={'pk':recipe.id}))
        self.assertEqual(response.status_code, 404)

