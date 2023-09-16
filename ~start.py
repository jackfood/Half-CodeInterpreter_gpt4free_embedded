import subprocess
import os
import time

while True:
    # Ask for user input
    user_input = input("Enter your input (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        break  # Exit the loop if the user types 'exit'

    # Write the user input to a file called '~prompt.txt' as UTF-8, creating a new one or overwriting if it exists
    with open('~prompt.txt', 'w', encoding='utf-8') as file:
        file.write(user_input)

    # Introduce a 0.2-second delay
    time.sleep(0.2)

    # Path to the batch script
    batch_script_path = r'D:\Python\~CodeInterpereterwithGPTTest\Scripts\aiengine.bat'

    # Start the batch script and wait for it to complete
    process = subprocess.Popen(batch_script_path, shell=True)
    process.wait()

    # Check if 'aianswer.txt' exists and read its contents
    if os.path.exists('aianswer.txt'):
        with open('aianswer.txt', 'r', encoding='utf-8') as file:
            ai_response = file.read()
        print("AI Response:")
        print(ai_response)
    else:
        print("Error: 'aianswer.txt' does not exist.")
