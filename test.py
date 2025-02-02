from spec_manager_agent import SpecManagerAgent
from spec_provider import SpecProvider
from config_provider import  ConfigProvider
from spec_manager_task import SpecManagerTask
from application_provider import ApplicationProvider

ApplicationProvider("example/school").test()
ConfigProvider().test()
SpecProvider("example/school").test()
spec_manager_agent = SpecManagerAgent().test()
spec_manager_task = SpecManagerTask().test()

