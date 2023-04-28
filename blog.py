from post import Post

class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return '{} by {} ({} post{})'.format(self.title,
                                               self.author,
                                               len(self.posts),
                                              's' if len(self.posts) != 1 else '')

    def create_post(self, title, content):
        self.posts.append((Post(title, content)))

    def json(self):
        #returning a String representation of this blog
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts]
            #returning the json method for each post in posts
        }