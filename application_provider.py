import yaml


class ApplicationProvider:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls._instance.__init__()
        return cls._instance

    def __init__(self):
        self.path = None
        self.spec = None

    def init(self, path):
        self.path = path
        with open(self.path + '/application.yaml', 'r') as f:
            self.spec = yaml.load(f, Loader=yaml.SafeLoader)

    def get_path(self):
        return self.path

    def get_name(self):
        return self.spec['name']

    def dump(self):
        print(self.spec)

    def test(self):
        print("========= Testing ApplicationProvider in application_provider.py file ")
        self.dump()
        print("========= End Testing ============= ")
