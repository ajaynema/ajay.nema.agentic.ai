from crewai import LLM


class LLMProvider():
    def get_default_llm(self):
        return LLM(model="ollama/deepseek-r1:7b", base_url="http://localhost:11434", api_key="ollama")

