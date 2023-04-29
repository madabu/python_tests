from unittest import TestCase
from blog import Blog

class BlogTests (TestCase):

    #Testing if the posts are added to the new blog
    def test_create_post_in_blog(self):
        #creating a new blog,
        #the Blog class has the blog title and author as args
        and_another_blog = Blog("Fruits", "Farmer")

        #creating a post in the new blog
        #the Post class has post title and content as args
        #using the create_post function from the Blog class
        and_another_blog.create_post("About Bananas", "Bananas are great")

        #Verifying that the list of posts has 1 post after creating it:
        self.assertEqual(1,len(and_another_blog.posts))
        #Verifying that the title of the post in the first position
        #of my list matches the value declared above:
        self.assertEqual(and_another_blog.posts[0].title, "About Bananas")
        #Verifying that the content of the post in the first position
        #of my list matches the value declared above:
        self.assertEqual(and_another_blog.posts[0].content, "Bananas are great")

    #Testing if the JSON method correctly displays the information provided
    #after creating a new blog and a new post inside the blog
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

    #Testing if the JSON method displays an empty list when there are no posts on the blog
    def test_json_with_no_posts(self):
        b = Blog ("Empty Blog","Nobody")
        expected_json = {
            'title': "Empty Blog",
            'author': "Nobody",
            'posts': []
        }

        self.assertDictEqual(expected_json, b.json())