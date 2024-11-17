from django.test import TestCase

from property.factories import PropertyFactory
from user.tests.factories import OwnerFactory

class PropertyTestCase(TestCase):
    def set_user(self, user):
        self.user = user
        self.client.force_login(self.user)

    def test_index_page_redirect_for_not_logged_in_user(self):
        response = self.client.get('/index/', follow=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.wsgi_request.path, '/login/')


    def test_my_properties_page_shows_own_properties(self):
        owner = OwnerFactory()
        properties = PropertyFactory.create_batch(10, owner=owner)
        
        self.set_user(owner)
        
        response = self.client.get('/index/my_properties/')
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_properties.html')
        self.assertEqual(len(response.context['own_properties']), 10)
