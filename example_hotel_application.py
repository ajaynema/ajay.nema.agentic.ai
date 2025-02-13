from application_provider import ApplicationProvider
from ajay_nema_ai_crew import AjayNemaAICrew
from dotenv import load_dotenv

load_dotenv()

ApplicationProvider.get_instance().init("example/hotel")
request = "validate all the specification"
engine = AjayNemaAICrew(request)
engine.run()