pllama is a way to pretty print output from Ollama models in your terminal. 

Here is an example of what the output from pllama looks like. 

![Screenshot 2025-01-15 at 21 16 11](https://github.com/user-attachments/assets/c29f1f4c-b386-4cd5-8bb3-b988c9475e75)

pllama is currently a work in progress, and has some bugs. 

Some features I'd like to work on include:
- CLI input to pass in a prompt
- Model to be used
- Possibly a way to save/export chats

## Running pllama

pllama is currently using uv as the package manager and is also the way to run and install the script. 

You will need `uv` installed.

1. Clone the repo
2. Run `uv sync` from inside of the repo
3. Run `uv run main.py` to run the script

pllama is open to contributions. Please fork the project, create a new branch with the changes, and then submit a pull request. Thank you!
