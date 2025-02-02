import yaml


class ApplicationProvider:
    def __init__(self, path):
        self.path = path
        self.spec = None
        self.init()

    def init(self):
        with open(self.path + '/application.yaml', 'r') as f:
            self.spec = yaml.load(f, Loader=yaml.SafeLoader)

    def getPath(self):
        return self.path

    def get_name(self):
        return self.spec['name']

    def dump(self):
        print(self.spec)

    def test(self):
        print("========= Testing ApplicationProvider in application_provider.py file ")
        self.dump()
        print("========= End Testing ============= ")
