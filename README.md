# OpenAI Multi-User Chat Example ✨

This repository demonstrates how to use OpenAI's API to manage multiple chat threads with context retention. It eliminates the need for external file storage by managing threads in memory, simplifying the implementation process.

## 🔧 Features
- **Multi-User Management**: Handle multiple users, each with their own chat thread.
- **Context Retention**: Maintain conversation continuity within threads.
- **Real-Time Interaction**: Seamless communication with OpenAI's GPT models.
- **Customizable Assistant**: Define instructions, name, and model for your assistant.

## 🚀 Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/openaiAPI-Context-Chat.git
   cd openaiAPI-Context-Chat
   ```

2. **Install Dependencies**:
   Make sure Python is installed, then install the required libraries:
   ```bash
   pip install openai
   ```

3. **Set API Credentials**:
   Edit the script to add your OpenAI API key, project ID, and organization ID:
   ```python
   GPTAPI_KEY = "your-api-key"
   PRDOJECT_ID = "your-project-id"
   ORGANIZATION_ID = "your-organization-id"
   ```

4. **Run the Script**:
   Start the program:
   ```bash
   python main.py
   ```

5. **Interact with the Assistant**:
   - Enter a username to create or retrieve a thread.
   - Type your messages to interact with the assistant.
   - Type `exit` or `stop` to end the conversation.

## 🔎 How It Works

- **Assistant Creation**: If no assistant exists, the script creates one with specified instructions, name, and model.
- **Thread Management**: Each user is assigned a unique thread ID, stored in memory.
- **Message Flow**:
  1. User inputs a message.
  2. The script sends the message to the API.
  3. The assistant processes and responds based on the thread's context.

## 🔧 Example Usage

```plaintext
Enter the name of the user: Alice
New thread created for user: Alice
Alice: Hello!
Assistant: Hi Alice! How can I assist you today?
Alice: What's the weather like?
Assistant: I'm unable to access live weather data, but let me know if you need any general information.
```

## 🔒 Notes
- Ensure your OpenAI API key has the necessary permissions.
- Adjust `time.sleep()` for optimal response processing time if needed.

## ⚖️ License
This project is licensed under the MIT License. Feel free to use and modify it to suit your needs. 🚀

