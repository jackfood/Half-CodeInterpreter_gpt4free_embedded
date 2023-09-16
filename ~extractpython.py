import os

# Try to read the AI's response from 'aianswer.txt'
try:
    with open('aianswer.txt', 'r', encoding='utf-8') as file:
        ai_response = file.read()
except FileNotFoundError:
    print("Error: 'aianswer.txt' not found")
    ai_response = None

if ai_response is not None:
    # Find and extract content between triple backticks (```python) and (```)
    start_markers = ["```python", "```"]
    end_marker = "```"
    start_index = -1
    for marker in start_markers:
        start_index = ai_response.find(marker)
        if start_index != -1:
            start_marker = marker
            break

    end_index = ai_response.find(end_marker, start_index + len(start_marker))

    if start_index != -1 and end_index != -1:
        python_content = ai_response[start_index + len(start_marker):end_index]

        # Check if 'aipythonanswer.txt' exists and compare its content with python_content
        aipythonanswer_path = 'aipythonanswer.txt'
        utf8_path = 'utf8.txt'

        try:
            with open(aipythonanswer_path, 'r', encoding='utf-8') as aipython_file:
                existing_content = aipython_file.read()
            
            if existing_content != python_content:
                # If python_content is different, delete 'aipythonanswer.txt' and create a new one
                try:
                    os.remove(aipythonanswer_path)
                    with open(aipythonanswer_path, 'w', encoding='utf-8') as python_file:
                        python_file.write(python_content)
                    with open(utf8_path, 'w', encoding='utf-8') as utf8_file:
                        utf8_file.write(python_content)
                    print("Python content updated in 'aipythonanswer.txt' and saved to 'utf8.txt'")
                except FileNotFoundError:
                    print("Error: 'aipythonanswer.txt' not found")
            else:
                print("Python content in 'aipythonanswer.txt' is the same as extracted content.")
        except FileNotFoundError:
            # If 'aipythonanswer.txt' doesn't exist, create it and save python_content to it
            with open(aipythonanswer_path, 'w', encoding='utf-8') as python_file:
                python_file.write(python_content)
            print("Python content extracted and saved to 'aipythonanswer.txt'")
            with open(utf8_path, 'w', encoding='utf-8') as utf8_file:
                utf8_file.write(python_content)
            print("Python content saved to 'utf8.txt'")
    else:
        print("No Python code found between triple backticks in 'aianswer.txt'")
else:
    print("No AI response found in 'aianswer.txt'")
