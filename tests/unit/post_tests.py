from unittest import TestCase
from post import Post

#the test cases must inherit from the 'TestCase' library
#each function has to start with 'test_'

class PostTests(TestCase):
    #Testing post creation:
    def test_create_post(self):
        #create a new post (object):
        new_post = Post("Test Title", "Test Content")

        #Test the post using the TestCase API that is the PostTests self object:

        #Is "Test Title" actually the title of the new post?
        self.assertEqual("Test Title", new_post.title)

        #Is "Test Content" actually the content of the new post?
        self.assertEqual("Test Content", new_post.content)

    def test_json(self):
        new_post = Post ("Test Title","Test Content")
        expected_json = {'title': "Test Title", 'content': "Test Content"}

        self.assertDictEqual(expected_json, new_post.json())
