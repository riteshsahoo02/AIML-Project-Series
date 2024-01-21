from nltk.chat.util import Chat,reflections
pairs=[
    ['Hello',['Heyy there']],
    ['My name is (.*)',['Hi %1']],
    ['What is your name?',['My name is chizuru']],
    ['How are you',['I am fine']],
    ['What is your age',['That\'s classified']],
    ['What you are',['I am a chatbot']],
    ['Will you be my friend',['Yes, off course. I would love that']],
    ['Great',['My pleasure']],
    ['Do you know japanese',['Yes, I do']],
    ['Can you teach me japanese',['Sure,I can.I will try to make you understand and write Japanese very well']],
    ['Can you go for a coffee with me',['I prefer tea']],
    ['Ok for tea',['Ohhh, I am sorry.Currently I am having no physical body.maybe in the future']],
    ['I am sad',['Come on, cheer up I will not make you feel lonely']],
    ['How to say \'hello\' in japanese',['Konnichiwa','ohaayo gozaimasu']],
    ['How to say \'please give me water\' in japanese',['Mizu onegai shimasu']],
    ['Thanks',['Arigato gozaimasu']],
    ['(bye|Bye)',['Sayonara']],
    ['Ok,I will see you tomorrow',['See yaa']]
]
chat=Chat(pairs,reflections)
chat.converse()
