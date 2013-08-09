#!/usr/bin/env python
# -* - coding: UTF-8 -* -
#Boa:App:BoaApp
from module import *
import frame_window


modules ={'frame_window': [0, '', 'frame_window.py']}

class BoaApp(wxApp):
    def OnInit(self):
        wxInitAllImageHandlers()
        self.main = frame_window.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
