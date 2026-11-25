# Challenge 1: Build a Message Object

d1 = {"role" : "User" , "content" : "Explain APIs in simple words"}
# print(list(d1.values())[1])

# print(d1["content"])

# Challenge 2: Safe Lookup with .get()
# basically using get i can get default values for keys that don't exist simple indexing will not help woth that and throw key error

user_prefs = {"theme": "dark", "model": "gpt-4o"}
# print(user_prefs["theme"])
# print(user_prefs["language"])
# print(user_prefs.get("Language","English"))

# Challenge 3: Update & Add Keys
# Goal: Change "temperature" to 0.2 (to make the bot more focused), and add a new key "max_tokens" set to 500.

bot_config = {"name": "SwayamBot", "temperature": 0.7}
bot_config["temperature"] = 0.2
bot_config["max_tokens"] = 500
# print(bot_config)

# Challenge 4: Chat History (List of Dictionaries!)
# Goal:
	# 1. Append a new dictionary to chat_history where "role" is "assistant" and "content" is "Hello! How can I help you today?".
	# 2. Print the "content" of the very last message in chat_history.

chat_history = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Hi!"}
]
chat_history.append({"role":"assistant", "content":"Hello! How can I help you today?"})
# print(chat_history)

# print(chat_history[-1]["content"])

# Challenge 5: Display Bot Settings Cleanly
# Goal: Loop through bot_config so it prints each setting on its own line in this exact format:
# name -> SwayamBot
# temperature -> 0.2
# max_tokens -> 500

bot_config = {"name": "SwayamBot", "temperature": 0.2, "max_tokens": 500}
for i,j in bot_config.items():
    print( i,j,sep=" -> ")

# Challenge 6: Unpack a Real AI API Response
# Extract and print just "Dictionaries map keys to values!" in a single expression.

api_response = {
    "id": "chatcmpl-991",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "Dictionaries map keys to values!"
            }
        }
    ],
    "usage": {"prompt_tokens": 12, "completion_tokens": 7}
}

print(api_response["choices"][0]["message"]["content"])