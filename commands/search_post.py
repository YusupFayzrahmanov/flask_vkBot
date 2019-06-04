import requests
import command_system
import vkapi

def search_post(search_param):
   message_post, attachment = vkapi.get_search_posts(-76456136, search_param)
   message = 'Привет, друг!\nНайденный пост по слову "'+search_param+'":\n'+message_post
   correctedWord = ''
   similiarWord = ''
   spellUrl = 'https://speller.yandex.net/services/spellservice.json/checkText?text='+ search_param
   dictionaryUrl = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=dict.1.1.20190405T171046Z.058ac4c863fd430d.2e58e0de4d6594eb6b4f3b8ede4613e80d984563&lang=ru-ru&text='+search_param

   #spellResult = requests.get(spellUrl)
   if(message_post == "Ничего не найдено!"):
       spellResult = requests.get(spellUrl)
       print(spellResult.status_code)
       print(spellResult.json())
       if(len(spellResult.json()) != 0):
           correctedWord = spellResult.json()[0]['s'][0]
           search_param = correctedWord
           print(correctedWord)
           message_post, attachment = vkapi.get_search_posts(-76456136, correctedWord)
           message += '\n\n\n Возможно вы искали "'+correctedWord+'":\n'+message_post


   dictionaryUrl = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=dict.1.1.20190405T171046Z.058ac4c863fd430d.2e58e0de4d6594eb6b4f3b8ede4613e80d984563&lang=ru-ru&text='+search_param
   dictionaryResult = requests.get(dictionaryUrl)
   print('\n DICTIONARY')
   print(dictionaryResult.status_code)
   if(len(dictionaryResult.json()['def'])!=0):
       similiarWord = dictionaryResult.json()['def'][0]['tr'][0]['text']
       print(similiarWord)
       message_post, attachmen = vkapi.get_search_posts(-76456136, similiarWord)
       message += '\n\n\n Посты, найденные по похожему слову "'+similiarWord+'":\n'+message_post

   return message, attachment

search_post_command = command_system.Command()

search_post_command.keys = ['найти', 'найди', 'поиск', 'поищи']
search_post_command.description = 'Поиск постов по ключевому слову(слово через пробел).'
search_post_command.process = search_post
