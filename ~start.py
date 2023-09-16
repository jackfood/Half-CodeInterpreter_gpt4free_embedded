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

    # Path to the batch script
    batch_script_path = os.path.join(current_directory, 'aiengine.bat')
    batch_script_path_extractpy = os.path.join(current_directory, '~extractpython.bat')

    # Start the batch script and wait for it to complete
    process = subprocess.Popen(batch_script_path, shell=True)
    process.wait()

    # Check if 'aianswer.txt' exists and read its contents
    aianswer_file_path = os.path.join(current_directory, 'aianswer.txt')
    if os.path.exists(aianswer_file_path):
        with open(aianswer_file_path, 'r', encoding='utf-8') as file:
            ai_response = file.read()
        print("AI Response:")
        print(ai_response)
    else:
        print("Error: 'aianswer.txt' does not exist.")
