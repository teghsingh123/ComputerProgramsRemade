from pynput.keyboard import Key,Listener

shiftcount = 0
altcount = 0
ctrlcount = 0



def on_press(key):
    print("{0} pressed".format(
        key
    ))

def on_release(key):
    print("{0} released".format(
        key
    ))

    global shiftcount
    if key == Key.shift:
        shiftcount += 1

    global ctrlcount
    if key == Key.ctrl:
        ctrlcount += 1

    global altcount
    if key == Key.alt:
        altcount += 1

    if key == Key.esc:
        print("Number of Shifts: " + str(shiftcount) + "\nNumber of Alts: " + str(altcount) + "\nNumber of Ctrls: " + str(ctrlcount))
        return False

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
