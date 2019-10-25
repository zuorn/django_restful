import unittest
import requests

class UserTest(unittest.TestCase):
    def setUp(self):
        self.base_url=''
        self.auth=('','')

    def test_get_user(self):
        r = requests.get(self.base_url+'/1/',auth=self.auth)
        result = r.json()

        self.assertEqual(result['username',''])
        self.assertEqual(result['email'], '')


    def test_add_user(self):
        form_data={'username':'','email':'','groups':''}
        r = requests.post(self.base_url+'/',data=form_data, auth=self.auth)
        result = r.json()

        self.assertEqual(result('username'),'')


    def test_delet_user(self):
        r = requests.delete(self.base_url + '/11/', auth = self.auth)

        self.assertEqual(r.status_code,204)

    def test_update_user(self):
        form_data = {'email':''}
        r = requests.patch(self.base_url+'/3/', auth = self.auth, data=form_data)
        result = r.json()

        self.assertEqual(result['email'],'')

    def test_no_auth(self):
        r = requests.get(self.base_url)
        result = r.json()

        self.assertEqual(result['detaill'],'Authentication credentials were not provided')

class Group_Test(unittest.TestCase):

    def setUp(self):
        self.base_url=''
        self.auth=('','')


    def test_group_developer(self):
        r = requests.get(self.base_url+'/5/',auth=self.auth)
        result = r.json()

    def test_add_group(self):
        form_data={'name':'Pm'}
        r = requests.post(self.base_url+'/',auth=self,data=form_data)
        result = r.json()

        self.assertEqual(result['name'],'Pm')

    def test_update_group(self):
        form_data={'name':'Boss'}
        r = requests.patch(self.base_url+'/5/',auth=self.auth,data=form_data)
        result = r.json()

        self.assertEqual(result['name'],'Boss')

    def test_delete_group(self):
        r = requests.delete(self.base_url+'/8/',auth=self.auth)

        self.assertEqual(r.status_code,204)

if __name__ == '__main__':
    unittest.main()

