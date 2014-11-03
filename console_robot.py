import sys
from time import sleep
from ctypes import *

FindWindow = windll.user32.FindWindowW
PostMessage = windll.user32.PostMessageW
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101
WM_CHAR = 0x0102

#virtual-key codes
VK = {
    "TAB": 0x09,
    "RETURN": 0x0D,
}

class Window:
    def __init__(self, wnd):
        self.wnd = wnd
        self.msg_delay = 0.02

    def set_msg_delay(self, delay):
        self.msg_delay = delay

    def _postmsg(self, msg, w, l):
        PostMessage(self.wnd, msg, w, l)
        sleep(self.msg_delay)
        
    def keyup(self, w, l=0):
        self._postmsg(WM_KEYUP, w, l)
        
    def keydown(self, w, l=0):
        self._postmsg(WM_KEYDOWN, w, l)

    def char(self, w, l=0):
        if type(w) == str:
            for c in w:
                if c == '\n':
                    c = VK["RETURN"]
                elif c == '\r':
                    continue
                else:
                    c = ord(c)
                self._postmsg(WM_CHAR, c, l)
        else:
            self._postmsg(WM_CHAR, w, l)

def find_console(title=0):
    while True:
        w = FindWindow("ConsoleWindowClass", title)
        if w != 0:
            return Window(w)
        sleep(0.5)

def main():
    if len(sys.argv) != 2:
        print("Usage: robot.py <key stroke script>")
        return 1
    key_script = sys.argv[1]
    exec(compile(open(key_script).read(), key_script, 'exec'))

if __name__ == "__main__":
    sys.exit(main())
