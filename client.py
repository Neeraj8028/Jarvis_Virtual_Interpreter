import openai

openai.api_key = "sk-None-oPeB8z1oKRiBOZ1QfX0dT3BlbkFJwag4h8xpDXNsO0PCx4dE"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant, skilled in general tasks like Alexa, news, YouTube, etc."},
        {"role": "user", "content": "what is coding"}
    ]
)

print(completion.choices[0].message['content'])
