# Read the AI's response from 'aianswer.txt'
with open('aianswer.txt', 'r', encoding='utf-8') as file:
    ai_response = file.read()

# Find and extract content between triple backticks (```python) and (```)
start_marker = "```python"
end_marker = "```"
start_index = ai_response.find(start_marker)
end_index = ai_response.find(end_marker, start_index + len(start_marker))

if start_index != -1 and end_index != -1:
    python_content = ai_response[start_index + len(start_marker):end_index]

    # Save the extracted Python content to 'aipythonanswer.txt' as UTF-8
    with open('aipythonanswer.txt', 'w', encoding='utf-8') as python_file:
        python_file.write(python_content)

    print("Python content extracted and saved to 'aipythonanswer.txt'")
else:
    print("No Python code found between triple backticks in 'aianswer.txt'")
