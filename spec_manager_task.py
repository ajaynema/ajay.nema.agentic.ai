from base_task import BaseTask
from spec_manager_agent import SpecManagerAgent, GetSpecAgent, ValidateSpecAgent
from spec_manager_tool import GetSpecificationTool


class ValidateSpecTask(BaseTask):
    def __init__(self):
        super().__init__("validate_spec_task", ValidateSpecAgent.get_instance(), [])
        self.init()


class GetSpecTask(BaseTask):
    def __init__(self):
        super().__init__("get_spec_task", GetSpecAgent.get_instance(), [GetSpecificationTool()])
        self.init()


class SpecManagerTask(BaseTask):
    def __init__(self):
        super().__init__("spec_manager_task", SpecManagerAgent.get_instance(), [])
        self.set_human_input(True)
        self.init()
