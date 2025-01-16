# OpenAI Multi-User Chat Management Example

from openai import OpenAI
import time

# OpenAI API Configuration
GPTAPI_KEY = ""  # Your OpenAI API key
PRDOJECT_ID = ""  # Your project ID
ORGANIZATION_ID = ""  # Your organization ID
ASSISTANT_ID = ""  # Optional: Existing assistant ID (if any)

# Dictionary to manage users and their thread IDs
users = {
    # Example: 'user_1': 'thread_id'
}

# Initialize OpenAI client
client = OpenAI(
    api_key=GPTAPI_KEY,
    organization=ORGANIZATION_ID,
    project=PRDOJECT_ID
)

# Create or retrieve assistant
try:
    my_assistant = client.beta.assistants.retrieve(
        assistant_id=ASSISTANT_ID
    )
except:
    my_created_assistant = client.beta.assistants.create(
        instructions="You are a good speaker",  # Main instruction for the assistant
        name="Good Speaker",  # Assistant's name
        model="gpt-4o"  # GPT model version
    )
    ASSISTANT_ID = my_created_assistant.id

# Function to start the program
def start_program():
    user = input("Enter the name of the user: ")

    if user in users:
        print(f"Welcome back, {user}!")
    else:
        thread = client.beta.threads.create()
        users[user] = thread.id
        print(f"New thread created for user: {user}")

    while True:
        text = input(f"{user}: ")

        if text.lower() in ['exit', 'stop']:
            print("Conversation is over.")
            break

        # Send a message
        message = client.beta.threads.messages.create(
            thread_id=users[user],
            content=text,
            role="user"
        )

        # Process the message using GPT
        run = client.beta.threads.runs.create(
            thread_id=users[user],
            assistant_id=ASSISTANT_ID
        )

        # Allow time for processing
        time.sleep(3)

        # Retrieve the assistant's response
        messages = client.beta.threads.messages.list(
            thread_id=users[user],
            run_id=run.id
        )

        # Print the assistant's response
        for msg in messages.data:
            if hasattr(msg, 'content') and msg.content:
                for block in msg.content:
                    if block.type == 'text' and hasattr(block, 'text'):
                        print(f"Assistant: {block.text.value}")

if __name__ == '__main__':
    start_program()
