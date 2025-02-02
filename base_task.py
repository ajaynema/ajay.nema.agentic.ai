from llm_provider import LLMProvider
from config_provider import ConfigProvider
from crewai import Task


class BaseTask:
    def __init__(self, name, agent):
        self.name = name
        self.agent = agent
        self.task = None
        self.config = ConfigProvider().get_task_config(name)

    def init(self):
        self.task = Task(
            description=self.config["description"],
            agent=self.agent.get(),
            verbose=True,
            expected_output=self.config["expected_output"]
        )

    def get(self):
        return self.task

    def get_name(self):
        return self.name
