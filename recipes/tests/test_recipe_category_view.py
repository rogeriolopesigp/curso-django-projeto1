from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase
    
class RecipeCategoryViewsTest(RecipeTestBase):

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes-category', kwargs={'category_id': 1}))
        self.assertIs(view.func.view_class, views.RecipeListViewCategory)   
    
    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get('recipes-category', kwargs={'category_id': 2})
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        self.make_recipe(title='This is a category test')
        response = self.client.get(reverse('recipes-category', args=(1,)))
        content = response.content.decode('utf- 8')

        self.assertIn('This is a category test', content)

    def test_recipe_category_template_doesnt_load_when_not_published(self):
        self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes-category', args=(1,)))
        self.assertEqual(response.status_code, 404)
        


