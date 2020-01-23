from django.test import TestCase
import requests


# Create your tests here.
class UserTest(TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/users'
        self.auth = ('zuorn', 'zuoruining')

    def test_get_user(self):
        r = requests.get(self.base_url + '/1/', auth=self.auth)
        result = r.json()

        self.assertEqual(result['username'], 'zuorn')
        self.assertEqual(result['email'], 'zuorn@qq.com')

    def test_add_user(self):
        form_data = {'usernmae': 'zuorn123', 'email': 'zuorn123@qq.com', 'groups': 'http://127.0.0.1:8000/groups/2/'}
        r = requests.post(self.base_url + '/', data=form_data, auth=self)
        result = r.json()

        self.assertEqual(result['username'], "zuorn123")

    def test_delete_user(self):
        r = requests.delete(self.base_url + '/11/', auth=self.auth)

        self.assertEqual(r.status_code, 204)

    def test_update_user(self):
        form_data = {'email': "test01@qq.com"}
        r = requests.patch(self.base_url + '/2/', auth=self.auth, data=form_data)
        result = r.json()

        self.assertEqual(result['email'], 'test01@qq.com')


    def test_user_already_exists(self):
        form_data = {'username' : ''}
