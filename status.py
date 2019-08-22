import os
import display
import utime


def get_mac():
    if 'mac.txt' in os.listdir("."):
        f = open('mac.txt', 'r')
        mac = f.read()
        f.close()
        return mac
    else:
        return ''


def loop():
    while True:
        mac = get_mac()
        with display.open() as disp:
            disp.clear()
            disp.print('battery v')
            disp.print(str(os.read_battery()), posy=22)
            if mac != '':
                print('print mac')
                disp.print('mac', posy=44)
                disp.print(mac, posy=66)
            disp.update()
            disp.close()
        utime.sleep(1)


loop()
