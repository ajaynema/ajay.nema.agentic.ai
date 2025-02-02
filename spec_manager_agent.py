from base_agent import BaseAgent


class SpecManagerAgent(BaseAgent):
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls._instance.__init__()
        return cls._instance

    def __init__(self):
        super().__init__("spec_manager_agent")
        self.init()

    def test(self):
        print("========= Testing SpecManagerAgent in spec_manager_agent.py file ")
        spec_manager = SpecManagerAgent().get()
        print("========= End Testing ============= ")

