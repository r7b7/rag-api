from dataclasses import dataclass, field
from typing import Dict

import adalflow as adal

@dataclass
class QueryOutput(adal.DataClass):
    response: str = field()
    __output_fields__ = ["response"] 


prompt_template =  r"""<SYS>
You are a helpful assistant.
<OUTPUT_FORMAT>
{{output_format_str}}
</OUTPUT_FORMAT>
</SYS>
User: {{input_str}}"""

class QueryGenerator(adal.Component):
    def __init__(self, model_client: adal.ModelClient, model_kwargs: Dict):
        super().__init__()

        parser = adal.DataClassParser(data_class=QueryOutput, return_data_class=True)
        self.generator = adal.Generator(
            model_client=model_client,
            model_kwargs=model_kwargs,
            template=prompt_template,
            prompt_kwargs={"output_format_str": parser.get_output_format_str()},
            output_processors=parser
        )

    def call(self, query: str):
        return self.generator.call({"input_str": query})