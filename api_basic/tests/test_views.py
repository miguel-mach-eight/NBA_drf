from django import urls
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from api_basic import models, views
#from model_bakery import baker 


class TestUserBase(TestCase):

    username = 'randomuser'
    password = 'randompassword'

    def setUp(self):
        super().setUp()

        User = get_user_model()

        self.user = User.objects.create_user(username='randomuser',
                                            email='example@example.com',
                                            password='randompassword',)
        self.user.role = self.user_type
        self.user.save()
        
class ReadWriteUserTest(TestUserBase):

    url = urls.reverse('Players list-list')
    user_type = 'read-write'

    def setUp(self):
        super().setUp()
        self.client.force_login(self.user)

        # self.assertTrue(self.client.login(username=self.username,
                                          #password=self.password))

    def test_read_write_user_GET_REQUEST(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_read_write_user_POST_REQUEST(self):
        
        response = self.client.post(self.url, {
            'id':'4',
            'first_name':'John',
            'h_in' : '77',
            'h_meters' : '1.96',
            'last_name' : 'Doe',
            })
        self.assertEqual(response.status_code, 201)

class ReadOnlyUserTest(TestUserBase):

    url = urls.reverse('Players list-list')
    user_type = 'read-only'

    def setUp(self):
        super().setUp()
        self.client.force_login(self.user)


        #self.assertTrue(self.client.login(username=self.username,
                                          #password=self.password))

    def test_read_only_user_GET_REQUEST(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_read_write_user_POST_REQUEST(self):
        response = self.client.post(self.url, {
            'first_name':'Miguel',
            'h_in' : '77',
            'h_meters' : '1.96',
            'last_name' : 'Figueroa'
            })
        self.assertEquals(response.status_code, 403)

class NonAuthenticatedTest(TestCase):
    
    url = urls.reverse('Players list-list')

        #self.client.force_logout()

    def test_non_authenticated_user_GET_REQUEST(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_non_authenticated_user_POST_REQUEST(self):
        response = self.client.post(self.url, {
            'first_name':'Miguel',
            'h_in' : '77',
            'h_meters' : '1.96',
            'last_name' : 'Figueroa'
            })
        self.assertEquals(response.status_code, 401)
