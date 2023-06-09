from typing import List

from langchain import PromptTemplate
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate
from langchain.prompts.chat import BaseStringMessagePromptTemplate, HumanMessagePromptTemplate


def filter_messages_by_type(messages: List[BaseStringMessagePromptTemplate], type) -> List[str]:
    return [msg.prompt.template for msg in messages if isinstance(msg, type)]


INSTRUCTION_INPUT_RESPONSE_PROMPT_TEMPLATE = """\
### Instruction:

{system_msg}

### Input:

{user_msg}

### Response:
"""

def chat_to_standard_prompt(chat_prompt: ChatPromptTemplate) -> PromptTemplate:
    system_msg = filter_messages_by_type(chat_prompt.messages, SystemMessagePromptTemplate)[0]
    user_msg = filter_messages_by_type(chat_prompt.messages, HumanMessagePromptTemplate)[0]  # todo we assume just one system and user message here

    template = INSTRUCTION_INPUT_RESPONSE_PROMPT_TEMPLATE.format(system_msg=system_msg, user_msg=user_msg)

    return PromptTemplate(
        template=template,
        input_variables=chat_prompt.input_variables
    )
