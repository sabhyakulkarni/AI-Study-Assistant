import json
chat_history = [
    {"role" : "user" , "content" : "Hi, help me understand JSON?"},
    { "role" : "gpt" , "content" : "Sure ! At what level are you?"}   
]

# with open("history.json","w") as f:
#     json.dump(chat_history,f,indent=4)


# def load_history(filename):
#     try:
#         f = open(filename,"r") 
#         return json.load(f)

#     except FileNotFoundError:
#         return []

# print(load_history("history.json"))
# print(load_history("his.json"))


# Challenge 1: Handle an Empty/Broken JSON File
def load_history(filename):
    try:
        f = open(filename,"r") 
        return json.load(f)

    except Exception:
        return []

# print(load_history("broken.json"))


# Challenge 2: Parse a Raw API JSON String 
# loads -> load string, it loads a string in dict format you dont even need dict
raw_response = '{"model": "gemini-2.5-flash", "reply": "JSON strings need parsing!", "tokens_used": 18}'
# print(raw_response)
# op = dict (json.loads(raw_response))
# op = dict(raw_response)
op =  json.loads(raw_response)
print(op["reply"])