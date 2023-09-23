import openai
import os
import argparse

openai.organization = os.getenv("OAI_ORG")
openai.api_key = os.getenv("OAI_API_KEY")

def read_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
    return content

def interact_with_chatgpt(api_key, prompt, file_context):
    openai.api_key = api_key
    full_prompt = f"{file_context}\n{prompt}"
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=full_prompt,
      max_tokens=350
    )
    return response.choices[0].text.strip()

def main():
    parser = argparse.ArgumentParser(description="Interact with ChatGPT")
    parser.add_argument("filename", help="Path to the file containing context")
    args = parser.parse_args()

    file_content = read_file(args.filename)
    
    while True:
        user_prompt = input("Your prompt (or type 'quit' to exit): ")
        
        if user_prompt.lower() == 'quit':
            break

        response = interact_with_chatgpt(openai.api_key, user_prompt, file_content)
        print(f"ChatGPT: {response}")

if __name__ == "__main__":
    main()
