import openai

openai.api_key = ""

message = {"role":"user", "content": input("\n******************************************\nWelcome to this chat, to exit, send \"###\".\n******************************************\n\nYou:")};

conversation = [{"role": "system", "content": "DIRECTIVE_FOR_gpt-3.5-turbo"}]

while(message["content"]!="###"):
    conversation.append(message)
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation) 
    message["content"] = input(f"\nChatGPT: {completion.choices[0].message.content} \n\nYou:")
    print()
    conversation.append(completion.choices[0].message)
