from crewai import LLM


class LLMProvider():
    _instance = None
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls._instance.__init__()
        return cls._instance

    def __init__(self):
        self.llm = None
        self.init()

    def init(self):
        self.llm = LLM(model="gpt-4o-mini")
        #self.llm = LLM(model="ollama/deepseek-r1:1.5b", base_url="http://localhost:11434", api_key="ollama")

    def get_default_llm(self):
        return self.llm

    def test(self):
        self.init()
        print("========= Testing LLMProvider in llm_provider.py file ")
        print(self.get_default_llm())
        print("========= End Testing ============= ")
