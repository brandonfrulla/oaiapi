# README for ChatGPT Interaction Script
 ______  ______  __   __  _____       __      ______  ______  __  __    
/\  ___\/\  ___\/\ "-.\ \/\  __-.    /\ \    /\  __ \/\  __ \/\ \/ /    
\ \___  \ \ \___\ \ \-.  \ \ \/\ \   \ \ \___\ \ \/\ \ \ \/\ \ \  _"-.  
 \/\_____\ \_____\ \_\\"\_\ \____-    \ \_____\ \_____\ \_____\ \_\ \_\ 
  \/_____/\/_____/\/_/ \/_/\/____/     \/_____/\/_____/\/_____/\/_/\/_/ 
                                                                        
## Overview

This script provides a command-line interface to interact with OpenAI's GPT-3 model, specifically the "text-davinci-003" model. It allows the user to provide a text file as context and then engage in a conversation with ChatGPT based on that context.

## Requirements

- Python 3.x
- OpenAI Python package
- API key from OpenAI

## Environment Variables

- OAI_ORG: Your OpenAI organization ID (optional)
- OAI_API_KEY: Your OpenAI API key

## Functions

### read_file(filename: str) -> str

Reads a file and returns its content as a string.

#### Parameters
- filename: Path to the file you want to read.

#### Returns
- Content of the file as a string.

### interact_with_chatgpt(api_key: str, prompt: str, file_context: str) -> str

Interacts with the GPT-3 model and returns its response.

#### Parameters
- api_key: OpenAI API key.
- prompt: User-provided prompt.
- file_context: Context provided from a file.

#### Returns
- davinci's response as a string.

### main()

The entry point of the script. Handles argument parsing and user interaction loop.

## How to Use

1. Set up your environment variables (OAI_ORG and OAI_API_KEY).
2. Run python <script_name>.py <filename> where <filename> is the path to your context file.
3. You will be prompted to input your questions or statements.
4. Type 'quit' to exit the script.

## Example Usage

```bash
$ export OAI_API_KEY=your-api-key-here
$ python interact_with_chatgpt.py my_context.txt
Your prompt (or type 'quit' to exit): How are you?
ChatGPT: I'm just a computer program, so I don't have feelings. How can I assist you today?
```

## Notes
The script uses argparse for command-line argument parsing.
The OpenAI API key and organization can be set as environment variables.
The maximum token limit for GPT-3's response is set to 150.