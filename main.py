import openai
import os
import argparse

openai.organization = os.getenv("OAI_ORG")
openai.api_key = os.getenv("OAI_API_KEY")
openai.Model.list()

def read_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
    return content

def interact_with_chatgpt(api_key, prompt, file_context):
    openai.api_key = api_key

    # Incorporate file contents into the prompt
    full_prompt = f"{file_context}\n{prompt}"

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=full_prompt,
      max_tokens=150  # You can adjust this as needed
    )

    return response.choices[0].text.strip()

def main():
    parser = argparse.ArgumentParser(description="Interact with ChatGPT")
    parser.add_argument("filename", help="Path to the file containing context")
    parser.add_argument("-p", "--prompt", help="Prompt string to add to user_prompt")
    args = parser.parse_args()


     # Read the file content
    file_content = read_file(args.filename)

    # Your prompt (what you want to ask ChatGPT)
    if args.prompt:
        user_prompt = args.prompt
    else:
        user_prompt = "Based on the above context, can you answer this question?"

    # Interact with ChatGPT
    response = interact_with_chatgpt(openai.api_key, user_prompt, file_content)
    print(response)

if __name__ == "__main__":
    main()
