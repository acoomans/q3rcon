from pkg_resources import resource_filename, resource_string

path = resource_filename(__name__, 'data/file.txt')
data = resource_string(__name__, 'data/file.txt')


class MyClass:

    def __init__(self):
        self.message = "hello, data is: " + data.decode('utf-8') + '(' + path + ')'
