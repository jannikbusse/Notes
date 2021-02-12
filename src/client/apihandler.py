import requests
import json

url = "http://127.0.0.1:5000"
posturl = '/todo/api/v1.0/notes'
deleteurl = "/todo/api/v1.0/notes/delete"
get_notes_url = "/todo/api/v1.0/notes"



def delete_note(id):
    send = {"id" : id}
    x = requests.post(url + deleteurl, json = send)
    return x

def send_note(thread, content, channel):
    send = {'thread': thread, 'content': content, 'channel': channel}
    x = requests.post(url + posturl, json = send)
    return x

def get_notes(thread):
    send = {'thread': thread}
    x = requests.get(url + get_notes_url, json = send)

    return json.loads(x.content)

     




