from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    @task(2)
    def test_users(self):
        self.client.get("/users/", auth=('zuorn', '123456'))

    @task(1)
    def test_groups(self):
        self.client.get("/groups/", auth=('zuorn', '123456'))


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
