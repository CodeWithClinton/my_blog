from django.test import TestCase

from blogapp.models import Blog

class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Blog.objects.create(title='Django Fullcourse', body='The blog body')

    def test_title_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_body_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('body').verbose_name
        self.assertEqual(field_label, 'body')

    def test_title_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('title').max_length
        self.assertEqual(max_length, 50)