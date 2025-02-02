from base_task import BaseTask
from spec_manager_agent import SpecManagerAgent


class ValidateSpecTask(BaseTask):
    def __init__(self):
        super().__init__("validate_spec_task", SpecManagerAgent.get_instance())
        self.init()


class GetSpecTask(BaseTask):
    def __init__(self):
        super().__init__("get_spec_task", SpecManagerAgent.get_instance())
        self.init()


class SpecManagerTask:
    _instance = None
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls._instance.__init__()
        return cls._instance

    def __init__(self):
        self.tasks = dict()
        self.init()

    def init(self):
        validate_spec_task = ValidateSpecTask()
        get_spec_task = GetSpecTask()
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
