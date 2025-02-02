from spec_manager_agent import SpecManagerAgent
from spec_provider import SpecProvider
from config_provider import  ConfigProvider

SpecProvider("example/school").test()
spec_manager_agent = SpecManagerAgent().test()
ConfigProvider().test()