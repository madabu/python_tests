class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def json(self):
        #JavaScript Object Notation
        #Used to transmit data between a server and a web applicaton,
        #as an alternative to XML
        #JSON data is represented in key-value pairs
        #KEYS are always strings,
        #VALUES can be strings, numbers, booleans, null, arrays etc.

        #this method returns a dictionary with properties of the post
        return {
            'title': self.title,
            'content': self.content,
            # trailing comma used to make sure older lines are not modified
            # when adding new lines
        }

    #a special method that returns a string representation of an object,
    #which can be used to recreate the object
    def __repr__(self):
        return f"Post ({self.title}, {self.content})"