
from crewai.tools import BaseTool
from spec_provider import SpecProvider


class GetSpecificationTool(BaseTool):
    name: str = "get specification"
    description: str = "get specification of the request specification {name}"

    def _run(self, name: str) -> str:
        # Your tool's logic here
        print(name)
        return SpecProvider.get_instance().get_spec(name)
