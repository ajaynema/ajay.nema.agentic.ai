import yaml


class ConfigProvider:
    def __init__(self):
        self.agents_config = None
        self.load_config()

    def load_config(self):
        self.load_agents()

    def load_agents(self):
        with open('config/agents.yaml', 'r') as f:
            self.agents_config = yaml.load(f, Loader=yaml.SafeLoader)

    def get_agent_config(self, agent):
        return self.agents_config[agent]

    def dump(self):
        print(self.agents_config)

    def test(self):
        print("========= Testing ConfigProvider in config_provider.py file ")
        self.dump()
        print("========= End Testing ============= ")