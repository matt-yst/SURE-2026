from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json
from pydantic import BaseModel, Field
import os
from anthropic import Anthropic
from dotenv import load_dotenv 
from dotenv import load_dotenv 

#CONSTANTS
URL = "https://shelly-api-docs.shelly.cloud/gen2/ComponentsAndServices/Light"
JSON = "search-doc.json"
load_dotenv()

CLAUDE_KEY = os.getenv("API_KEY")


client = Anthropic(api_key = CLAUDE_KEY)


client = Anthropic(api_key = CLAUDE_KEY)

#TESTING STUFFS

with open (JSON, "r", encoding="utf-8") as f: 
    data = json.load(f)

pattern = r"\b[A-Z][A-Za-z0-9_]+\.[A-Z][A-Za-z0-9_]+\b"

class Method(BaseModel):
    name: str
    parameters: dict[str, str]

class Component(BaseModel):
    name: str
    methods: list[Method] 


counter = 0
filtered_data = ""
for item in data:
    if item.get('type') == 1:
        matches = re.findall(pattern, item.get('title'))
        if matches:
            filtered_data += (item.get('title') + " - " + item.get('content'))
            # filtered_data += matches
            filtered_data += '\n'
            filtered_data += '\n'
            counter += 1
    if counter >= 100:
        break
        
message = client.messages.create(
    max_tokens=1000,
    messages=[
        {
        "role": "user",
        "content": "Extract all the components and their methods from the following text: " + str(filtered_data),
        }
    ],
    model="claude-opus-4-8",
)

# response = client.messages.count_tokens(
#     model="claude-opus-4-8",
#     messages=[{
#         "role": "user",
#         "content": "Extract all the components and their methods from the following text: " + filtered_data,
#     }],
# )
# print(response.input_tokens)

print(message.content[0].text)
print(message.usage)
