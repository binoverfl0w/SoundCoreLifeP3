from bluetooth import discover_devices
from LifeP3Client import  LifeP3Client, CommandType
import os

client = None
commandlist = None

def main():
    global client, commandlist
    mac = chooseBTDevice()
    client = LifeP3Client(mac)
    commandlist = client.getCommandList()
    client.open()
    while True:
        cmd = displayMenu()
        if (cmd == 0):
            break
        client.send(cmd)
    client.close()
    
def chooseBTDevice():
    devList = discover_devices(lookup_names=True)
    i = 0
    for (mac, name) in devList:
        print(f"{i}) {name}: {mac}")
    dev = int(input("Choose your SoundCore LifeP3 device: "))
    return devList[dev][0]

def displayMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("- MENU -")
    print("1) Change noise cancellation mode")
    print("2) Change equalizer mode")
    print("0) Exit")
    choice = int(input("Choose your action: "))
    if (choice == 0):
        return 0
    cmd = displaySubMenu(choice)
    if (cmd == 0):
        displayMenu()
    return cmd    

def displaySubMenu(choice):
    global commandlist
    commands = None
    if (choice == 1):
        commands = [v for v in commandlist if v.type == CommandType.NOISE]
    elif (choice == 2):
        commands = [v for v in commandlist if v.type == CommandType.EQUALIZER]
    else:
        print("Not a valid choice!")
    i = 1
    for command in commands:
        print(f"{i}) {command.desc}")
        i += 1
    print("0) Go back")
    choice = int(input("Select a mode: "))
    if (choice == 0):
        return 0
    return commands[choice - 1]

if __name__ == "__main__":
    main()