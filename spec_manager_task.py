from base_task import BaseTask
from spec_manager_agent import SpecManagerAgent


class ValidateSpecTask(BaseTask):
    def __init__(self, agent):
        super().__init__("validate_spec_task", agent)
        self.init()


class GetSpecTask(BaseTask):
    def __init__(self, agent):
        super().__init__("get_spec_task", agent)
        self.init()


class SpecManagerTask:
    def __init__(self):
        self.agent = SpecManagerAgent()
        self.tasks = dict()
        self.init()

    def init(self):
        validate_spec_task = ValidateSpecTask(self.agent)
        get_spec_task = GetSpecTask(self.agent)
        get_spec_task_name = get_spec_task.get_name()
        validate_spec_task_name = validate_spec_task.get_name()
        self.tasks[validate_spec_task_name] = validate_spec_task
        self.tasks[get_spec_task_name] = get_spec_task

    def get_tasks(self):
        return self.tasks

    def dump(self):
        print(self.tasks)

    def test(self):
        print("========= Testing SpecManagerTask in spec_manager_task.py file ")
        self.dump()
        print("========= End Testing ============= ")
