import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import serial

ser = serial.Serial("COM9", 9600, timeout = 1)
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def retrieveData0():
    ser.write(b'1')
    data = ser.readline().decode('ascii')
    return data

def retrieveData1():
    ser.write(b'2')
    data = ser.readline().decode('ascii')
    return data

def retrieveData2():
    ser.write(b'3')
    data = ser.readline().decode('ascii')
    return data

def retrieveData3():
    ser.write(b'4')
    data = ser.readline().decode('ascii')
    return data

def retrieveData4():
    ser.write(b'5')
    data = ser.readline().decode('ascii')
    return data

def retrieveData5():
    ser.write(b'6')
    data = ser.readline().decode('ascii')
    return data

def retrieveData6():
    ser.write(b'7')
    data = ser.readline().decode('ascii')
    return data

def retrieveData7():
    ser.write(b'8')
    data = ser.readline().decode('ascii')
    return data

def retrieveData8():
    ser.write(b'9')
    data = ser.readline().decode('ascii')
    return data

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Kate' in command:
                command = command.replace('Kate', '')
                print(command)

    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what' in command:
        person = command.replace('what', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'when' in command:
        person = command.replace('when', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'turn' in command:
        if 'on' in command:
            if 'fan' in command:
                print(retrieveData3())
                talk("Turning on the fan")
            elif 'light' in command:
                print(retrieveData2())
                talk("Turning on the light")
            elif 'dim' in command:
                print(retrieveData1())
                talk("Dimming the light")
            elif 'out light' in command:
                print(retrieveData7)
                talk("Turning on garden lights")
        elif 'off' in command:
            if 'fan' in command:
                print(retrieveData4())
                talk("Turning off the fan")
            elif 'light' in command:
                print(retrieveData0())
                talk("Turning off the light")
            elif 'out light' in command:
                print(retrieveData8())
                talk("Turning off garden lights")
    elif 'unlock' in command:
        if '1234' in command:
            print(retrieveData5())
            talk("Door unlocked")
        else:
            talk("Wrong code")
    elif 'lock' in command:
        print(retrieveData6())
        talk("Door locked")
    else:
        talk('Please say the command again.')

while True:
    run_alexa()