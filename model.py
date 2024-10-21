from openai import OpenAI
from decouple import config
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

class GPT_Engine:
    '''

     messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Hello, how are you?"
        }
      ]
    },
 
   
    '''
    def __init__(self):
        self.messages = []

    def add_message(self, message, message_role="user", message_type="text"):
        self.messages.append({
            "role": message_role,
            "content": [
                {
                    "type": message_type,
                    "text": message
                }
            ]
        })
    def top(self):
        for i in reversed(self.messages):
            if i['role'] == 'assistant':
                return i['content'][0]['text']
        return None
    
    def generate_response(self, params={ 
                                "temperature": 1, 
                                "max_tokens": 256, 
                                "top_p": 1, 
                                "frequency_penalty": 0, 
                                "presence_penalty": 0, 
                                "stop": None,
                                "response_format":{ 
                                    "type": "text"
                                } 
                                }):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=self.messages,
            temperature=params["temperature"],
            max_tokens=params["max_tokens"],
            top_p=params["top_p"],
            frequency_penalty=params["frequency_penalty"],
            presence_penalty=params["presence_penalty"],
            stop=params["stop"],
            response_format=params["response_format"]
        )
        self.add_message(response.choices[0].message.content, message_role="assistant")
    def clear(self):
        self.messages = []

        



    