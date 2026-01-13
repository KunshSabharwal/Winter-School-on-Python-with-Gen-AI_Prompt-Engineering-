from pydantic import BaseModel

class Test(BaseModel):
    success: bool
    session_id: str
    response: dict

print(Test.model_json_schema())

'''
{'properties': {'success': {'title': 'Success', 'type': 'boolean'}, 'session_id': {'title': 'Session Id', 'type': 'string'},
 'response': {'additionalProperties': True, 'title': 'Response', 'type': 'object'}}, 'required': ['success', 'session_id', 'response'], 
 'title': 'Test', 'type': 'object'}

The above output from this program was given to ChatGPT and with a prompt to generate a json function.
Image - Chatgpt Image for Prompt Engineering - Pydantic Output.png
'''