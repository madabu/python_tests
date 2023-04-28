from blog import Blog

#in-memory data base that is a dictionary
blogs = dict() #blog_name : Blog object

MENU_PROMPT = 'Enter "c" to create a blog, "l" to list posts, "r" to read a blog, "p" to create a post, or "q" to quit: '

POST_TEMPLATE = '''
    --- {} ---
    
    {}

'''

def menu ():
    #what the menu does:
    #shows the user the available blogs
    #lets the user make a choice
    #and do something with that choice
    #eventually exit

    print_blogs()

    #the user gets asked what they want to do,
    #the menu prompt is displayed
    #and with their input, they respond:
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
            #while the user does not enter 'q' to quit,
            #they will be asked to make another selection:
        selection = input(MENU_PROMPT)

def print_blogs():
    #print the available blogs
    #for a dict, both the key and the value need to be included in the loop
    #.items gives us a list of key,blog tuples
    #[(blog_name, Blog), (blog_name, Blog)]

    for key, blog in blogs.items():
        print(' - {}'.format(blog))

def ask_create_blog():
    #to create a blog,
    #the user must give the title of the blog they want to create
    #and their name
    #using the input function
    title = input("Enter the title of your new blog, please: ") #first side effect, see function test
    author = input("Enter your author name, please: ") #second side effect, see function test

    #then the blog will be stored in the dictionary as
    #blog_name : Blog object (the Blog class has title and author as parameters)
    #under the 'title' key

    blogs[title] = Blog(title, author)

def ask_read_blog():
    #to read a blog,
    #the user must enter the title of the blog they want to read
    title = input("Enter the title of the blog you'd like to read: ")

    #then the posts from the blog the user wants to read, will be printed
    print_posts(blogs[title])

def print_posts(blog):
    #through this function, the loop iterates over each post on the blog
    for post in blog.posts:
        #and with the print_post method, each post is then printed
        print_post(post)

def print_post(post):
    #this function is called in the print_posts function
    #it prints the post using the POST_TEMPLATE,
    #which prints the post's title and content
    #in the format declared above
    print(POST_TEMPLATE.format(post.title, post.content))

def ask_create_post():
    blog_name = input("Enter the title of the blog you'd like to post in, please: ") #first side effect
    blog_title = input("Enter the title of your post: ") #second side effect
    blog_content = input("Enter the content of your post: ") #third side effect

    blogs[blog_name].create_post(blog_title, blog_content)