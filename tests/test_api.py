from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from users.models import User
from blogs.models import Blog
from comments.models import Comment


class UserAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword"
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_create_user(self):
        url = reverse("users:user-list")
        response = self.client.post(url, self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_get_user_list(self):
        url = reverse("users:user-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class BlogAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword"
        }
        self.user = User.objects.create_user(**self.user_data)
        self.blog_data = {
            "title": "Test Blog",
            "content": "This is a test blog.",
            "user": self.user
        }
        self.blog = Blog.objects.create(**self.blog_data)

    def test_create_blog(self):
        url = reverse("blogs:blog-list")
        response = self.client.post(url, self.blog_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Blog.objects.count(), 2)

    def test_get_blog_list(self):
        url = reverse("blogs:blog-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class CommentAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword"
        }
        self.user = User.objects.create_user(**self.user_data)
        self.blog_data = {
            "title": "Test Blog",
            "content": "This is a test blog.",
            "user": self.user
        }
        self.blog = Blog.objects.create(**self.blog_data)
        self.comment_data = {
            "content": "This is a test comment.",
            "user": self.user,
            "blog": self.blog
        }
        self.comment = Comment.objects.create(**self.comment_data)

    def test_create_comment(self):
        url = reverse("comments:comment-list")
        response = self.client.post(url, self.comment_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 2)

    def test_get_comment_list(self):
        url = reverse("comments:comment-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)