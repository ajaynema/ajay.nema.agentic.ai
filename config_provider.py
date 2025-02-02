import yaml


class ConfigProvider:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls._instance.__init__()
        return cls._instance

    def __init__(self):
        self.agents_config = None
        self.tasks_config = None

    def init(self):
        self.load_config()

    def load_config(self):
        self.load_agents()
        self.load_tasks()

    def load_agents(self):
        with open('config/agents.yaml', 'r') as f:
            self.agents_config = yaml.load(f, Loader=yaml.SafeLoader)

    def load_tasks(self):
        with open('config/tasks.yaml', 'r') as f:
            self.tasks_config = yaml.load(f, Loader=yaml.SafeLoader)

    def get_agent_config(self, agent):
        return self.agents_config[agent]

    def get_task_config(self, task):
        return self.tasks_config[task]

    def dump(self):
        print(self.agents_config)
        print(self.tasks_config)

    def test(self):
        print("========= Testing ConfigProvider in config_provider.py file ")
        self.init()
        self.dump()
        print("========= End Testing ============= ")
