from post import Post

class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    #The __repr__() method is used to define a string representation of an object,
    #it provides a concise and unambiguous representation of an object's state
    #primarily intended for debugging and development purposes
    def __repr__(self):
        return '{} by {} ({} post{})'.format(self.title,
                                               self.author,
                                               len(self.posts),
                                              's' if len(self.posts) != 1 else '')

    #when a new post is created,
    #the post with its title and content are added
    #to the posts list of the blog,
    #using the Post class
    def create_post(self, title, content):
        self.posts.append((Post(title, content)))

    #JSON is a lightweight data interchange format
    #that is primarily used for data exchange between systems
    #JSON does not support complex data types like sets and tuples
    def json(self):
        #returning a String representation of this blog
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts]
            #returning the json method for each post in posts
        }