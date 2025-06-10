import datetime
import os

def log_prompt(user_message, assistant_message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = f"prompts/session_{timestamp}.md"

    with open(file_path, "w") as file:
        file.write(f"# User Message\n{user_message}\n\n")
        file.write(f"# Assistant Message\n{assistant_message}\n\n")

import requests

def log_prompt(user_message, assistant_message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = f"prompts/session_{timestamp}.md"

    with open(file_path, "w") as file:
        file.write(f"# User Message\n{user_message}\n\n")
        file.write(f"# Assistant Message\n{assistant_message}\n\n")

# Automatically log prompts
user_message = input("Enter user message: ")
assistant_message = input("Enter assistant message: ")
log_prompt(user_message, assistant_message)

response = requests.post("https://example.com/log-prompt", json={"user_message": user_message, "assistant_message": assistant_message})
if response.status_code == 200:
    print("Prompt logged successfully")
else:
    print("Failed to log prompt")
>>>>>>> REPLACE
