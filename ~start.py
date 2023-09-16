import subprocess
import os
import time

while True:
    # Ask for user input
    user_input = input("Enter your input (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        break  # Exit the loop if the user types 'exit'

    # Get the current working directory
    current_directory = os.getcwd()

    # Construct the path to the '~prompt.txt' file in the current directory
    prompt_file_path = os.path.join(current_directory, '~prompt.txt')

    # Write the user input to the '~prompt.txt' file as UTF-8
    with open(prompt_file_path, 'w', encoding='utf-8') as file:
        file.write(user_input)

    # Introduce a 0.2-second delay
    time.sleep(0.2)

    # Path to the Python scripts (replace .bat with .py)
    python_script_path_aiengine = os.path.join(current_directory, 'aiengine.py')
    python_script_path_extractpy = os.path.join(current_directory, '~extractpython.py')

    # Start aiengine.py and wait for it to complete
    process_aiengine = subprocess.Popen(['python', python_script_path_aiengine], shell=True)
    process_aiengine.wait()

    # Check if 'aianswer.txt' exists and read its contents
    aianswer_file_path = os.path.join(current_directory, 'aianswer.txt')
    if os.path.exists(aianswer_file_path):
        with open(aianswer_file_path, 'r', encoding='utf-8') as file:
            ai_response = file.read()

        # Execute ~extractpython.py if needed
        print("AI Response:")
        print(ai_response)
        process_extractpy = subprocess.Popen(['python', python_script_path_extractpy], shell=True)
        process_extractpy.wait()

        # Check if aipythonanswer.txt is not empty
        aipythonanswer_path = 'aipythonanswer.txt'
        if os.path.exists(aipythonanswer_path) and os.path.getsize(aipythonanswer_path) > 0:
            with open(aipythonanswer_path, 'r', encoding='utf-8') as aipython_file:
                python_script_content = aipython_file.read()
            
            # Run the Python script from aipythonanswer.txt
            try:
                exec(python_script_content)
                print("Python script in 'aipythonanswer.txt' executed successfully.")
                
                # Clear the contents of aipythonanswer.txt
                with open(aipythonanswer_path, 'w', encoding='utf-8') as aipython_file:
                    aipython_file.truncate(0)
            except Exception as e:
                print("Error executing Python script from 'aipythonanswer.txt':", str(e))
                # Copy the error response
                error_response = str(e)
                print("Error Response:", error_response)

                # Loop for the next input when asking for user input
                user_input = input("Enter your input (or type 'exit' to quit): ")
                continue

    else:
        print("Error: 'aianswer.txt' does not exist.")
