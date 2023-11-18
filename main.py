from openai import OpenAI

gptapi = 'ТВОЙ_КЛЮЧ_АПИ_ВСТАВЬ_СЮДА'
client = OpenAI(api_key=gptapi, )

print('-------------VOPROS------------->>>')
vopros = str(input('Задай мне любой вопрос и получи крутой ответ! \n Ваш вопрос: '))
completion = client.chat.completions.create(
    messages=[{"role": "user", "content": vopros, }],
    model="gpt-3.5-turbo",)

print("<<<----------OTVET----------------")
otvet = completion.choices[0].message.content
print(otvet)
