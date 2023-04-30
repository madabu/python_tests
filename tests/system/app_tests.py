from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post


class AppTest(TestCase):

    #Testing if when we call app.menu,
    #mock_input is called with app.MENU_PROMPT
    #in other words,
    #we are testing if the menu prompt shows up when we call the app.menu function
    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value = 'q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    #Testing if the menu quits
    #if the user were to enter 'q'
    def test_menu_quits(self):
        #mocking the user input with the value 'q'
        with patch('builtins.input', return_value = 'q') as mocked_input_to_quit:
            #assigning the menu to a result variable to make the assertion easier to write
            result = app.menu()

            #verifying that the menu function returns None, indicating that it has quit
            self.assertIsNone(result)

    #Testing if the menu calls the ask_create_blog function
    #if a user were to input 'c' into the menu prompt
    def test_menu_calls_ask_create_a_blog(self):
        #patching and mocking the ask_create_blog function
        with patch('app.ask_create_blog') as mocked_ask_create_blog:
            #patching and mocking the user input
            with patch('builtins.input') as mocked_input_to_call_ask_create_a_blog:
                #if the user were to enter 'c'
                #and then 'q' to quit
                mocked_input_to_call_ask_create_a_blog.side_effect = ('c', 'q')

                #then, call the menu
                app.menu()

                #verifying that the correct function is called by the menu
                #if the user input is 'c'
                mocked_ask_create_blog.assert_called()

    #Testing if a blog is created if
    #a user were to input 'c' into the menu prompt
    def test_menu_and_ask_create_a_blog(self):
        #we are mocking the user's input:
        with patch('builtins.input') as mocked_input_to_call_and_create_blog:
            #using the menu selection, the blog title and the blog author side effects
            #as well as the 'q' selection to quit
            mocked_input_to_call_and_create_blog.side_effect = ('c', "Testing Create Blog", "Create Blog Tester", 'q')

            app.menu()

            #then we verify whether the list of blogs contains the blog created by the user:
            self.assertIsNotNone(app.blogs['Testing Create Blog'])

    #Testing if a blog is created and added to the corresponding dict
    #if the user were to input that they want to create a blog
    #after they enter(we mock) the title and the author of the blog
    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input_to_create_blog:
             #first, we input the blog title and the author name
             mocked_input_to_create_blog.side_effect = ("I want to create a blog", "Blog Creator") #side effects used to create a blog
             #secondly, we call the method
             app.ask_create_blog()
             #then we verify if the dict contains the blog
             self.assertIsNotNone(app.blogs.get("I want to create a blog"))

    #Testing if the print_blogs function is called in the menu
    #if the user were to input 'l'
    def test_menu_calls_print_blogs(self):
        #when we replace a function like print_blogs
        #with the mocked "fake" function (mocked_print_blogs)
        #the mock does not do/execute anything
        with patch('app.print_blogs') as mocked_print_blogs:
            #in order to enter a value into the menu to make a selection
            #we need to input a value ('l'):
           with patch('builtins.input', return_value='l'):
                app.menu()

                #verifying if the print_blogs() function is called
                #when the menu() function is executed with the input value 'l'
                mocked_print_blogs.assert_called()

    #Testing if the print_blogs() function
    #displays the correct information in the correct format
    #if the user were to create a blog with a title and their author name
    def test_print_blogs(self):
        #create a new blog
        stub_blog = Blog ("Stub", "Stubber")
        #attributing the blog name to the blog object
        #because, in my system blog_name : Blog object
        app.blogs = {"Stub": stub_blog}

        #replacing the print function with the mock
        with patch('builtins.print') as mocked_print_blogs:

            app.print_blogs()

            #verifying if the mocked method is called with the correct argument
            #which is the String below, and it is the expected output of the
            #print_blogs() function:
            mocked_print_blogs.assert_called_with(' - Stub by Stubber (0 posts)')

    #Testing if the menu calls the ask_read_blog function if
    #the user were to enter 'r'
    def test_menu_calls_read_blog(self):
        #patching the ask_read_blog function and mocking it
        with patch('app.ask_read_blog') as mocked_read_blog:
            #patching the user's input
            with patch('builtins.input') as mocked_input_to_read_blog:
                #using 'r' as a side effect to request to read
                #and call the ask_read_blog function
                #and using 'q' as a side effect to quit after inputting 'r'
                #otherwise, the test goes on forever
                mocked_input_to_read_blog.side_effect = ('r', 'q')

                #then, we call the menu
                app.menu()

                #verifying is the correct function is called by the menu:
                mocked_read_blog.assert_called()

    #Testing if the corresponding posts are printed when
    #the user enters te name of the blog they want to read
    def test_ask_read_blog(self):
        #first, we create a blog:
        blog_to_read = Blog("I want to read this blog", "Blog Reader")
        #secondly, we associate the title key with the value of the blog object
        app.blogs = {"I want to read this blog": blog_to_read}

        #then, we must fake(patch) the user's input
        #if the user wants to read a specific blog, they must enter/input its title
        with patch('builtins.input', return_value = "I want to read this blog"):
            #then we mock the print_posts function from the ask_read_blog function,
            #to test whether this function inside the ask_read_blog_funtion is being called
            with patch('app.print_posts') as mocked_print_posts:
                #then the ask_read_blog function is called:
                app.ask_read_blog()

                #lastly, we verify that the posts printed correspond to the blog title given by the user
                mocked_print_posts.assert_called_with(blog_to_read)

    #Testing if the print_post method is called correctly by the print_posts function
    def test_print_posts(self):
        blog_with_posts_printed = Blog("I want to read these posts", "Post Reader")
        blog_with_posts_printed.create_post("Testing print_posts function", "We are testing the print posts function here")
        app.blogs = {"Testing print_posts function": blog_with_posts_printed}

        #the print_posts function used the print_post function
        #so that is why we are patching and mocking that function:
        with patch('app.print_post') as mocked_print_posts:
            app.print_posts(blog_with_posts_printed)

            #verifying if the print post function is called
            #with the first post in the posts list (element in the first position [0])
            #that belongs to the blog with the title given by the user:
            mocked_print_posts.assert_called_with(blog_with_posts_printed.posts[0])
            #assert method checks whether this mock object is being called with the correct arg

    #Testing if the menu calls the ask_create_post function
    #if the user were to input 'p' into the menu prompt
    def test_menu_calls_print_post(self):
        #patching and mocking the ask_create_post function
        with patch('app.ask_create_post') as mocked_ask_create_post:
            #mocking the user input
            with patch('builtins.input') as mocked_input_ask_create_post:
                #to ask create post and then quit
                mocked_input_ask_create_post.side_effect = ('p','q')

                app.menu()

                #verifying that the correct function is called by the menu:
                mocked_ask_create_post.assert_called()

    #Testing if the print_post method is called with the correct parameter
    #and if it prints the post according to the template established in app.py
    #when the user asks to read a blog, the posts should be printed like the expected_printed_post
    def test_print_post(self):
        #creating a new post with its title and content
        post_for_printing = Post ("Printed Post", "I want this post to be printed")
        #assigning the expected format
        expected_printed_post = '''
    --- Printed Post ---
    
    I want this post to be printed

'''
        #using the patch to print the mocked function and its text
        with patch('builtins.print') as mocked_print_post:
            #calling the print_post function that
            #takes the post created above as an arg
            app.print_post(post_for_printing)

            #verifying that the post's (and function's)
            #text and format matches the expected format declared above
            mocked_print_post.assert_called_with(expected_printed_post)

    #Testing if the ask_create_post function successfully
    #helps the user create a new post
    #in a blog
    def test_ask_create_post(self):
        #create a new blog
        blog_for_creating_post = Blog ("Post Creation", "Post Creator")
        #assign the title (key) to the blog object
        app.blogs = {"Post Creation": blog_for_creating_post}

        #patch and mock the user input
        with patch('builtins.input') as mocked_input_to_create_post:
            #the ask_create_post function asks the user to input 3 side effects:
            #the blog_name, the post_title, and the post_content
            mocked_input_to_create_post.side_effect = ("Post Creation", "The Post I created", "I want to create a post")

            #after providing requested input, we call the function
            app.ask_create_post()

            #then, we verify that the title of the first post from the blog is:
            self.assertEqual(blog_for_creating_post.posts[0].title, "The Post I created")
            #and we verify that the content of the first post from the blog is:
            self.assertEqual(blog_for_creating_post.posts[0].content, "I want to create a post")
            #the assert checks that the values entered match the values declared before