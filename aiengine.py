import g4f
import os

# Read user input from '~prompt.txt'
with open('~prompt.txt', 'r', encoding='utf-8') as file:
    input_prompt = file.read()

# Use the input prompt to generate a response from the GPT-3 model
response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": input_prompt}],
    stream=False,
)

# Extract the AI's response content from the response object
ai_response = response

# Check if 'aianswer.txt' exists, and overwrite or create accordingly
with open('aianswer.txt', 'w', encoding='utf-8') as file:
    file.write(ai_response)
