# Your code goes here
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

prompt_template_str = """
Your task is to explain the concept of **{concept}** to me in a way that is:

1. Clear and intuitive
2. Concise (in under 100 words)
3. Tailored specifically to me and what I already know

Use the following information about me to personalize your explanation:

- Role: AI Engineer
- Goal: Building LLM-powered applications end-to-end from scratch
- Background: Software engineering and AI development

The personalization should be subtle and natural. Avoid forced references that don't genuinely enhance understanding.
"""

# Create a prompt template
prompt_template = PromptTemplate.from_template(prompt_template_str)

# Define the input variable
concept = "Scaling Laws"

# Format the prompt
prompt = prompt_template.format(concept=concept)

print(prompt)

# Create a model interface
model = init_chat_model("gpt-4o-mini", model_provider="openai")

# Call the model with the prompt
response = model.invoke(prompt)

# Print the generated content
print(response.text)

