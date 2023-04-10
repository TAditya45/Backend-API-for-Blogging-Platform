from django.test import TestCase
from django.contrib.auth import get_user_model
from myapp.models import Blog, Comment
from myapp.friend_utils import find_friends

User = get_user_model()

class FriendUtilsTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='user1', email='user1@example.com')
        self.user2 = User.objects.create(username='user2', email='user2@example.com')
        self.user3 = User.objects.create(username='user3', email='user3@example.com')
        self.blog1 = Blog.objects.create(user=self.user1, title='Blog 1', content='Content 1')
        self.blog2 = Blog.objects.create(user=self.user2, title='Blog 2', content='Content 2')
        self.blog3 = Blog.objects.create(user=self.user3, title='Blog 3', content='Content 3')
        self.comment1 = Comment.objects.create(user=self.user1, blog=self.blog1, content='Comment 1')
        self.comment2 = Comment.objects.create(user=self.user2, blog=self.blog1, content='Comment 2')
        self.comment3 = Comment.objects.create(user=self.user1, blog=self.blog2, content='Comment 3')
        self.comment4 = Comment.objects.create(user=self.user3, blog=self.blog2, content='Comment 4')

    def test_find_first_level_friends(self):
        friends = find_friends(self.user1)
        expected_friends = set([self.user2])
        self.assertEqual(friends, expected_friends)

    def test_find_second_level_friends(self):
        friends = find_friends(self.user2, level=2)
        expected_friends = set([self.user3])
        self.assertEqual(friends, expected_friends)

    def test_find_third_level_friends(self):
        friends = find_friends(self.user1, level=3)
        expected_friends = set([])
        self.assertEqual(friends, expected_friends)

