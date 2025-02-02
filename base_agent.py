from llm_provider import LLMProvider
from config_provider import ConfigProvider
from crewai import Agent


class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.agent = None
        self.config = ConfigProvider().get_agent_config(name)
        self.llm = LLMProvider().get_default_llm()

    def init(self):
        self.agent = Agent(
            config=self.config,
            verbose=True,
            llm=self.llm,
            allow_delegation=False)

    def get(self):
        return self.agent
