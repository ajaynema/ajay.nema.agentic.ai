from llm_provider import LLMProvider
from config_provider import ConfigProvider
from crewai import Task


class BaseTask:
    def __init__(self, name, agent, tools=None):
        self.name = name
        self.agent = agent
        self.task = None
        self.tools = tools
        self.human_input = False
        self.config = ConfigProvider.get_instance().get_task_config(name)

    def init(self):
        self.task = Task(
            description=self.config["description"],
            agent=self.agent.get(),
            verbose=True,
            tools=self.tools,
            human_input=self.human_input,
            expected_output=self.config["expected_output"]
        )

    def set_human_input(self, human_input):
        self.human_input = human_input

    def get(self):
        return self.task

    def get_name(self):
        return self.name
