from django import urls
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from api_basic import models, views
#from model_bakery import baker 


class TestUserBase(TestCase):

    def setUp(self):
        super().setUp()

        User = get_user_model() #Necessary to implement our custom user model inside the tests

        self.user = User.objects.create_user(username='randomuser',
                                            email='example@example.com',
                                            password='randompassword',)
        self.user.role = self.user_type #When inherting this class, user_type will be defined inside the test
        self.user.save()
        self.instance = models.NBAplayers.objects.create(first_name='John', h_in = '74', h_meters = '1.89', last_name='Doe') #Create some dummy data for our DB before making tests
        self.instance.save() 

        #The following data will not be in the DB, but rather added or updated to it.
        self.data = {
            'first_name':'John',
            'h_in' : '77',
            'h_meters' : '2',
            'last_name' : 'Doe',
            }    
class ReadWriteUserTest(TestUserBase):

    url = urls.reverse('Players list-list') 
    user_type = 'read-write'

    def setUp(self):
        super().setUp()
        self.client.force_login(self.user)

    def test_read_write_user_GET_REQUEST(self): #Test wether my verified user can see players or not
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_read_write_user_POST_REQUEST(self): #Test whether my verified user can add new players or not, in this case 'John Doe'
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 201)

    def test_read_write_user_POST_CONTENT(self): #Test if the content added with our POST REQUEST is actually the same we created in 'data'.
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.data, self.data)

    def test_read_write_user_PUT_REQUEST(self): #Test if we can update data from already existing players
        url = urls.reverse('Players list-detail', args=[1])
        response = self.client.put(url, data=self.data , content_type='application/json')
        self.assertEqual(response.status_code, 200)

class ReadOnlyUserTest(TestUserBase):

    url = urls.reverse('Players list-list')
    user_type = 'read-only'

    def setUp(self):
        super().setUp()
        self.client.force_login(self.user)
 
    def test_read_only_user_GET_REQUEST(self): #Test wether my verified user can see players or not.
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_read_only_user_POST_REQUEST(self): #Test whether my verified user can add new players or not, in this case 'John Doe'.  A read-only User shouldn't.
        response = self.client.post(self.url, data=self.data)
        self.assertEquals(response.status_code, 403)
    
    def test_read_only_user_PUT_REQUEST(self): #Test if we can update data from already existing players. A read-only User shouldn't.
        url = urls.reverse('Players list-detail', args=[1])
        response = self.client.put(url, data=self.data , content_type='application/json')
        self.assertEqual(response.status_code, 403)

class NonAuthenticatedTest(TestCase):
    
    url = urls.reverse('Players list-list')

    def test_non_authenticated_user_GET_REQUEST(self): #Test wether my verified user can see players or not. A non authenticated User shouldn't.
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
