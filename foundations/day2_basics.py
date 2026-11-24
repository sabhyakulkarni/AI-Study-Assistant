#Numbers
# hours_per_topic = 3
# topics = ["APIs" , "RAG", "LLMs" "agents"]
# topics.append("evals")
# no_of_topics= len(topics)+1
# print(hours_per_topic * no_of_topics)

#Slicing and Strings
s = "Hello, I am going for my masters in fall 2027"
# print(s[1:])
# print(s[1:10:2])
# print(s[-1])
# print(s[-1:-1])
# print(s[::-1])
# print(s[-1:-49:-1])

command = "/ask What is Python?"
# print(command[5::1])

messages = ["Hi", "Hello!", "How are you?", "I need Python help", "Sure!"]
# print(messages[-2:])

turns = ["User 1", "Bot 1", "User 2", "Bot 2", "User 3", "Bot 3"]
# print(turns[0:5:2])

code = "AI-2026-BOT"
# print(code[-5:-9:-1])

# Split and Strip
raw_input = "   \n  Hello chatbot!   \t "
# print(raw_input.strip(" \n\t"))
# help(str.strip)

user_msg = "/summarize Explain quantum computing in simple words"
# print(user_msg[1:].split(" ",maxsplit=1))

topics_input = "python, ai ,  apis, chatbots"
s = topics_input.split(",")
# l=[]
# for i in s:
#     l.append(i.strip(" "))
# print(l)

filename = "my.project.notes.day1.pdf"
# print(filename.split(".")[-1])

#Asking user for some inputs
message = input(str("Ask Anything: "))
while(not any(char.isalpha() for char in message)):
    message = input(str("Type something: "))
