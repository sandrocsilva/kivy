import keyboard
while True:
    try:
        print("Estou em Looping!")
        if keyboard.is_pressed('q'):
            break
    except:
        break