from spec_manager_agent import SpecManagerAgent
from spec_provider import SpecProvider
from config_provider import  ConfigProvider
from spec_manager_task import SpecManagerTask
from application_provider import ApplicationProvider
from llm_provider import  LLMProvider

ApplicationProvider.get_instance().init("example/school")
ApplicationProvider.get_instance().test()
ConfigProvider.get_instance().test()
LLMProvider.get_instance().test()
SpecProvider.get_instance().test()
spec_manager_agent = SpecManagerAgent.get_instance()
spec_manager_agent.test()

spec_manager_task = SpecManagerTask.get_instance()
spec_manager_task.test()

