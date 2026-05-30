#importing necessary libraries
import os
from google import genai
from dotenv import load_dotenv

#this is the Gemini API key, it is stored in a .env file for security reasons
load_dotenv()
client= genai.Client(api_key = os.getenv("GEMINI_API_KEY"))


#function called ask that takes a prompt and returns the response from the Gemini API
def ask(prompt):
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt,
      # this is the configuration for the response, it limits the response to 100 tokens
      config={
            "max_output_tokens": 100 
            }
    )
    return response.text

