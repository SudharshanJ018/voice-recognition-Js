import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
listener = sr.Recognizer()
engine =pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()



    except:
        pass

def send_email(receiver,subject,message):
    server =smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('sudharshanj474@gmail.com','Sudharshan@10')
    email=EmailMessage()
    email['from']='sudharshanj474@gmail.com'
    email['to']=receiver
    email['subject']=subject
    email.set_content(message)
    server.send_message(email)




email_list={
    'red': 'Cvenkatesh.btech@gmail.com',
    'pink':'chennakrishnasai@gmail.com',
    'srinivas':'srinivasj474@gmail.com'


}

def get_email_info():
    talk('to whom you want to send email')
    name = get_info()
    recevier=email_list[name]
    print(recevier)
    talk('what is the subject of your email')
    subject =get_info()
    talk('Tell me the text in your email')
    message=get_info()
    send_email(recevier,subject,message)

get_email_info()
