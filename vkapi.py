import vk
import random
import settings

session_group = vk.Session(settings.group_token)
api_group = vk.API(session_group, v=5.92)

session_app = vk.Session(settings.service_token)
api_app=vk.API(session_app, v=5.92)

def get_random_wall_picture(group_id):
    max_num = api_app.photos.get(owner_id=group_id, album_id='wall', count=0, access_token=settings.service_token)['count']
    num = random.randint(1, max_num)
    photo = api_app.photos.get(owner_id=str(group_id), album_id='wall', count=1, offset=num, access_token=settings.service_token)['items'][0]['id']
    attachment = 'photo' + str(group_id) + '_' + str(photo)
    return attachment


def send_message(user_id, message, attachment=""):
    api_group.messages.send(acces_token=settings.group_token,user_id=user_id,random_id=random.randint(0,9999), message=message, attachment=attachment)

def get_search_posts(group_id, search_param):
    group_post = api_app.wall.search(acces_token=settings.service_token,owner_id=str(group_id),query=search_param,owners_only=0,count=2)


    print(group_post)
    post_attachment =""
    if(group_post['count'] == 0):
        out_message = "Ничего не найдено!"
    elif(group_post['items'][0]['post_type'] != 'post'):
        out_message = "Ничего не найдено!"
    else:
        print(group_post['items'][0]['id'])
        post_comments = api_app.wall.getComments(acces_token=settings.service_token, owner_id = str(group_id),post_id=group_post['items'][0]['id'],need_likes=0,count = 5, sort='desc')
        print("\n \n COMMENTS:")
        print(post_comments)
        if post_comments['count'] == 0:
            out_comments = "\nКомментарии отсутсвуют."
        else:
            out_comments = ''
            print(post_comments)
            for i in range(len(post_comments['items'])):
                out_comments +='# '+str(i+1)+ ') '+ post_comments['items'][i]['text']+'\n'
            #out_comments = post_comments['items'][0]['text']
        if 'attachments' in group_post['items'][0].keys():
            attachment_type = group_post['items'][0]['attachments'][0]['type']
            post_attachment = attachment_type + str(group_id) + '_' + str(group_post['items'][0]['attachments'][0][attachment_type]['id'])
        post_message = group_post['items'][0]['text']
        out_message = "Пост:\n" + post_message + "\n Комментарий:\n" + out_comments

    return out_message,post_attachment
