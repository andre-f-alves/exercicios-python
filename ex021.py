print('Tocando um MP3')
from playsound import playsound
música = input('Que música você quer ouvir? ')
print('Em exibição: {}'.format(música))
playsound(música)
