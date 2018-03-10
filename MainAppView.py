#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import Tkinter as tk
import webbrowser 

class MainAppView(tk.Frame):
    """Encapsulates of all the GUI logic.

   

    Attributes:
        master: where to open the Frame, by deafult root window
        title: Main Label
     
        one: Button 
        two: Button 
        three: Button 

    """

    width = 100 
    height = 200
    
    def start_gui(self,ok = True):
        """Starts the GUI, if everything ok , to change

        """
        
        if ok:
            self.mainloop()
        else:
            self.master.destroy()

    def createWidgets(self):
        """Create the set of initial widgets.

     

        """
        #create Window Geometry
        #self.geometry("170x200")


        # Create the labels

        # Title
        self.title = tk.Label(
                self, text = "iota Biosciences: Dust Development")
        self.title.grid( row=0, column=0,columnspan=50, sticky = tk.E+tk.W )

        # Transmit Parameters
        self.transmit_banner = tk.Label(
                    self, text = "Transmit Parameters")
        self.transmit_banner.grid( row = 1, column = 0)

        # Transmit Frequency
        self.f_pulse_banner = tk.Label(
                    self, text = "Transmit Frequency")
        self.f_pulse_banner.grid( row = 2, column = 0)

        self.f_pulse_entry = tk.Entry(self)
        self.f_pulse_entry.grid( row = 2, column = 1)
        self.f_pulse_entry.insert(10,"2.25e6")
      
        # Pulse Repition Frequency
        self.f_repition_banner = tk.Label(
                    self, text = "Pulse Repition Frequency")
        self.f_repition_banner.grid( row = 3, column = 0)


        self.f_repition_entry = tk.Entry(self)
        self.f_repition_entry.grid( row = 3, column = 1)
        self.f_repition_entry.insert(10,"1e3")

        # N Pulses Frequency
        self.pulses_banner = tk.Label(
                    self, text = "Number of Pulses")
        self.pulses_banner.grid( row = 4, column = 0)

        self.pulses_entry = tk.Entry(self)
        self.pulses_entry.grid( row = 4, column = 1)
        self.pulses_entry.insert(10,"5")


        # Create the three buttons

        self.sendTx = tk.Button(self)
        self.sendTx["text"] = "Send Tx"
        self.sendTx.grid(row=5, column=0)

        self.stop = tk.Button(self)
        self.stop["text"] = "Stop"
        self.stop.grid(row=5, column=1)
     
        self.three = tk.Button(self)
        self.three["text"] = "Task 3"
        self.three.grid(row=5, column=2)

        self.four = tk.Button(self)
        self.four["text"] = "Task 4"
        self.four.grid(row=5, column=3)





    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        # option is needed to put the main label in the window
        self.createWidgets()

        
    


