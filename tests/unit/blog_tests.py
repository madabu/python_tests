from unittest import TestCase
from blog import Blog

class BlogTests (TestCase):
    def test_create_blog(self):
        new_blog = Blog ("Test Title", "Test Author")

        self.assertEqual("Test Title", new_blog.title)
        self.assertEqual("Test Author", new_blog.author)
        self.assertListEqual([], new_blog.posts)
        #or use self.assertListEqual (len([]), len(new_blog.posts))
        #or use self.assertEqual (0, len(new_blog.posts))

    def test_repr(self):
        new_blog1 = Blog ("John's Blog", "John")
        new_blog2 = Blog ("Jane's Blog", "Jane")

        self.assertEqual(new_blog1.__repr__(),"John's Blog by John (0 posts)")
        self.assertEqual(new_blog2.__repr__(),"Jane's Blog by Jane (0 posts)")

    def test_repr_multiple_posts(self):
        another_blog = Blog ("Somebody's Blog", "Somebody")
        another_blog.posts = [{'title': "The Title", 'content': "The Content"}]

        yet_another_blog = Blog ("Making Tea", "The Queen of England")
        yet_another_blog.posts = [{'title': "How to make English Breakfast Tea", 'content': "Recipe"}]

        self.assertEqual(another_blog.__repr__(),"Somebody's Blog by Somebody (1 post)")
        self.assertEqual(yet_another_blog.__repr__(), "Making Tea by The Queen of England (1 post)")

