# Half-CodeInterpreter_gpt4free_embedded

This project aims to integrate the [Half-codeInterpreter](https://github.com/jackfood/Half-codeInterpreter) into the free generative AI provided by [gpt4free](https://github.com/xtekky/gpt4free).

This repository contains Python scripts for an AI chat engine that interacts with the GPT-3.5 model and allows code execution. The project consists of three main scripts:

start.py: This script serves as the user interface for the AI chat engine. It takes user input, communicates with the GPT-3.5 model, and handles code execution.

extractpython.py: This script is responsible for extracting Python code blocks from the responses generated by the AI and saving them to a file. It also detects and extracts pip install commands and package names.

aiengine.py: This script interfaces with the GPT-3.5 model using the g4f library to generate AI responses based on user input.


## Getting Started

To get started, follow these steps:

1. Visit the [gpt4free](https://github.com/xtekky/gpt4free) GitHub repository and install the PyPI package in your Python environment:

   - pip install -U g4f

2. Clone or download this repository and put it in the same g4f Python directory.

3. Run the following command:

   - python ~start.py

Follow the on-screen instructions. You can enter text input, and the AI will respond accordingly. It can also auto execute Python code by including it within triple backticks or (python) and (). The Python code will be executed, and the result will be displayed.

## Important Notes
Do note that the stability depends on the free provider from [gpt4free](https://github.com/xtekky/gpt4free).

To exit the chat engine, type 'exit' when prompted for input.

Extracted Python code blocks are saved in aipythonanswer.txt, and pip.txt contains any extracted pip install package names which links to installpip.py.

installpip.py, is designed to automate the installation of Python packages specified in the pip.txt file. It reads the package name from pip.txt, attempts to install the package(s) using pip, and then removes the pip.txt file (to avoid repeatition)

Make sure you have the necessary Python environment and libraries installed to execute the code generated by the AI.

Exercise caution when executing code obtained from external sources.

## Integration

The main goal of this project is to integrate the Half-codeInterpreter into the gpt4free generative AI. Work is in progress to combine the capabilities of both projects for enhanced functionality.

## Contributing

We welcome contributions! If you want to contribute to this project, please follow our contribution guidelines.
