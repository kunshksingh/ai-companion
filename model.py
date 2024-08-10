from openai import OpenAI
client = OpenAI()

class GPT_Engine:
    '''

     messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "You are awesome"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Hello how are you?"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "Hello! I'm just a computer program, so I don't have feelings, but I'm here and ready to help you with anything you need. How can I assist you today?"
        }
      ]

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
                                "max_tokens": 150, 
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
    def clear(self):
        self.messages = []

        



    