from base_agent import BaseAgent


class SpecManagerAgent(BaseAgent):
    def __init__(self):
        super().__init__("spec_manager_agent")
        self.init()

    def test(self):
        print("========= Testing SpecManagerAgent in spec_manager_agent.py file ")
        spec_manager = SpecManagerAgent().get()
        print("========= End Testing ============= ")

