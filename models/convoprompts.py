from openai import OpenAI
from config import translate_key
client = OpenAI(api_key=translate_key)

def getConvo(userinfo):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {
      "role": "system",
      "content": "I will give you a context. Generate some text that is conversation between multiple people"
    },
    {
      "role": "user",
      "content": userinfo
    }
  ],
    
    max_tokens=1200,
    )
    return response.choices[0].message.content

def getTranslated(language,text):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {
      "role": "system",
      "content": "I will share text and get it translated into "+language
    },
    {
      "role": "user",
      "content": text
    }
  ],
    
    max_tokens=1200,
    )
    return response.choices[0].message.content
