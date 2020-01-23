import requests
import unittest
from api.test_project.mysql_action import DB
import yaml


class UserTest(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/users'
        self.auth = ('zorn', '123456')

    def test_001_get_user(self):
        r = requests.get(self.base_url + '/1/', auth=self.auth)
        result = r.json()

        self.assertEqual(result['username'], 'zuorn')
        self.assertEqual(result['email'], 'zuorn@qq.com')


class GroupTest(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/groups'
        self.auth = ('zuorn', '123456')

    def test_001_group_developer(self):
        r = requests.get(self.base_url + '/1/', auth=self.auth)
        result = r.json()

        self.assertEqual(result + ['name'], "Developer")


if __name__ == '__main__':
    db = DB()
    f = open('datas.yaml', 'r')
    datas = yaml.load(f)
    db.init_data(datas)
    unittest.main()
