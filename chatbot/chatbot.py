import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

messages = []

while True:
    try:
        user_input = input("You: ")
        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages= messages
        )
        messages.append(response["choices"][0]["message"].to_dict())
        # print(response["choices"][0]["message"]["content"])
        print("Assistant: ", response["choices"][0]["message"]["content"])
        # print("All Messages", messages)
    except KeyboardInterrupt: 
        print("Exiting...")
        break

print(response)