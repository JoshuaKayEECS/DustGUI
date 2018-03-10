#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk

from MainAppController import MainAppController

def main():

    controller = MainAppController()

    # Build Gui and start it
    root = tk.Tk()
    root.title('Ultrasound Controller')

    controller.init_view(root)


    print 'Bye Bye'

    controller.close()



if __name__ == "__main__":
    main()