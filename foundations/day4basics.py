# def prntN()

# Postional arguments prntN(name,age)---> while calling prntN("sabhya",22) --> order matters
# Keyword Arguments prntN(name,age)--> while calling prntN(age=22, name="sabhya") -->order doesnt matter 
# Default Arguments prntN(a, b =30)  --> if b is not passes while calling then default = 30 else whatvever user has passed overrides this.
# Variable Length Arguments (*args--> stores as tuple multiple positional arguments, **kwargs--> stores as dict mutiple keyword arguments)

# Challenge 1: Build a Message Formatter Function
def makeMessage(role,text):
    return {"role":role,"text":text}

# print(makeMessage("user","hi"))


# Challenge 2: Function with a Default Parameter
def ask_bot(prompt, model="gpt-4o-mini"):
    print("Sending ",prompt,"to ",model)

# ask_bot("hi")
# ask_bot("hi","gemini-2.5-flash")

# Challenge 3: Safe API Response Parser (try/except)

api_response = {
    "id": "chatcmpl-991",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "Dictionaries map keys to values !",
                "error" :"Rate limit exceeded"
            }
        }
    ],
    "usage": {"prompt_tokens": 12, "completion_tokens": 7}
}
def extract_reply(api_response):
    try:
        return api_response["choices"][0]["message"]["error"]
    except Exception:
       return "Sorry couldnt process"

print(extract_reply(api_response))

bad_response = {"error": "Rate limit exceeded"}  #there is no ["choices"] key so even if you add error: rate limit exceeded into api_response, it doesnt point to big dict up
print(extract_reply(bad_response))


# Challenge 4: Safe Number Input for Bot Settings
# try:
#     max_tokens = int(input("Enter maximum number of tokens you wnat the bot to use: "))

# except Exception:
#     print("Enter valid integer ",ValueError)

# finally:
#     print("Using",max_tokens,"tokens")



