import spec_manager_agent
from spec_manager_agent import GetSpecAgent, ValidateSpecAgent, SpecManagerAgent

from spec_manager_task import SpecManagerTask, GetSpecTask, ValidateSpecTask
from crewai import Crew


class AjayNemaAICrew:
    def __init__(self, request):
        self.request = request
        self.tasks = []
        self.agents = []
        self.init()

    def init(self):
        self.load_agents()
        self.load_tasks()

    def load_agents(self):
        self.agents.append(GetSpecAgent.get_instance().get())
        self.agents.append(ValidateSpecAgent.get_instance().get())


    def load_tasks(self):
        self.tasks.append(SpecManagerTask().get())
        self.tasks.append(GetSpecTask().get())
        self.tasks.append(ValidateSpecTask().get())

    def run(self):
        crew = Crew(
            agents=self.agents,
            tasks=self.tasks,
            memory=False,
            manager_agent=SpecManagerAgent.get_instance().get(),
            verbose=False)

        crew.kickoff()
