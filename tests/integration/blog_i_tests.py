from unittest import TestCase
from blog import Blog

class BlogTests (TestCase):
    def test_create_post_in_blog(self):
        and_another_blog = Blog("Fruits", "Farmer")
        and_another_blog.create_post("About Bananas", "Bananas are great")

        self.assertEqual(1,len(and_another_blog.posts))
        self.assertEqual(and_another_blog.posts[0].title, "About Bananas")
        self.assertEqual(and_another_blog.posts[0].content, "Bananas are great")

    def test_json(self):
        vegetable_blog = Blog ("Vegetables", "Vegetabler")
        vegetable_blog.create_post("Potatoes","Potatoes can become french fries")

        expected_json = {
            'title': "Vegetables",
            'author': "Vegetabler",
            'posts': [
                {'title': "Potatoes", 'content': "Potatoes can become french fries"}
            ]
        }

        self.assertDictEqual(expected_json, vegetable_blog.json())

    def test_json_with_no_posts(self):
        b = Blog ("Empty Blog","Nobody")
        expected_json = {
            'title': "Empty Blog",
            'author': "Nobody",
            'posts': []
        }

        self.assertDictEqual(expected_json, b.json())