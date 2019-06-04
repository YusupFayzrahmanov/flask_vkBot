import command_system
import vkapi

def maestro(param):
   # Получаем случайную картинку из паблика
   attachment = vkapi.get_random_wall_picture(-65853336 )
   message = 'Вот тебе маэстро :)\nВ следующий раз я пришлю другого евГЕНИЯ.'
   return message, attachment

cat_command = command_system.Command()

cat_command.keys = ['маэстро', 'гений', 'евгений', 'лучший', 'великий', 'неповторимый']
cat_command.description = 'Пришлю картинку с маэстро'
cat_command.process = maestro
