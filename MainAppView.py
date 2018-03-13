#!/usr/bin/env python 
# -*- coding: utf-8 -*-


import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

from PIL import Image, ImageTk

import Tkinter as tk
import tkFont
import serial.tools.list_ports

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

    def serial_ports(self):    
        ports = serial.tools.list_ports.comports()
        for port in ports:
            print port
        return serial.tools.list_ports.comports()

    # on change dropdown value
    def change_dropdown(self, *args):
        print( self.FPGA_port.get() )

    def init_attributes(self):
        self.upArrowImage = Image.open("up_arrow.jpg")
        self.upArrowPhoto = ImageTk.PhotoImage(self.upArrowImage)

    def createWidgets(self):
        """Create the set of initial widgets.

     

        """
        #create Window Geometry
        #self.geometry("170x200")

        # Create Font because Python is dumb sometimes

        # Create the labels

        # Title
        self.title = tk.Label(
                self, text = "iota Biosciences: Dust Development")
        self.title.grid( row=0, column=0,columnspan=50, sticky = tk.E+tk.W )

        # Transmit Parameters
        self.parameter_frame = tk.Frame(self)
        self.parameter_frame.grid(row=1,column=0, sticky=tk.N)

        self.transmit_banner = tk.Label(
                    self.parameter_frame, text = "Transmit Parameters")
        self.transmit_banner.grid( row = 0, sticky = tk.E+tk.W)
        f_underline = tkFont.Font(self.transmit_banner, self.transmit_banner.cget("font"))
        f_underline.configure(underline = True)
        self.transmit_banner.configure(font=f_underline)

        # Transmit Frequency
        self.f_pulse_banner = tk.Label(
                    self.parameter_frame, text = "Transmit Frequency")
        self.f_pulse_banner.grid( row = 1, column = 0)

        self.f_pulse_entry = tk.Entry(self.parameter_frame)
        self.f_pulse_entry.grid( row = 1, column = 1)
        self.f_pulse_entry.insert(10,"2.25e6")
      
        # Pulse Repition Frequency
        self.f_repition_banner = tk.Label(
                    self.parameter_frame, text = "Pulse Repition Frequency")
        self.f_repition_banner.grid( row = 2, column = 0)


        self.f_repition_entry = tk.Entry(self.parameter_frame)
        self.f_repition_entry.grid( row = 2, column = 1)
        self.f_repition_entry.insert(10,"1e3")

        # N Pulses Frequency
        self.pulses_banner = tk.Label(
                    self.parameter_frame, text = "Number of Pulses")
        self.pulses_banner.grid( row = 3, column = 0)

        self.pulses_entry = tk.Entry(self.parameter_frame)
        self.pulses_entry.grid( row = 3, column = 1)
        self.pulses_entry.insert(10,"5")

        # Serial Port Drop Down Menu
        self.FPGA_port_banner= tk.Label(
            self.parameter_frame, text = "FPGA Port")
        self.FPGA_port_banner.grid( row = 4, column = 0)

        # frame to combine FPGA port info inside frame_parameter
        self.FPGA_frame = tk.Frame(self.parameter_frame)
        self.FPGA_frame.grid(row=4,column=1, sticky=tk.E+tk.W)

        availablePorts = self.serial_ports()
        self.FPGA_port = tk.StringVar(self)
        self.FPGA_port.set("Choose Port")
        self.FPGA_port_menu = tk.OptionMenu(
                    self.FPGA_frame, self.FPGA_port, *availablePorts)
        self.FPGA_port_menu.grid( row=0, column = 0)
        self.FPGA_port.trace('w', self.change_dropdown)

        self.FPGA_connect = tk.Button(self.FPGA_frame)
        self.FPGA_connect["text"] = "Connect"
        self.FPGA_connect.grid(row=0, column=1)

        # Create the three buttons
        button_row = 5
        self.sendTx = tk.Button(self.parameter_frame)
        self.sendTx["text"] = "Send Tx"
        self.sendTx.grid(row=button_row, column=0)

        self.stop = tk.Button(self.parameter_frame)
        self.stop["text"] = "Stop"
        self.stop.grid(row=button_row, column=1)
     
        self.three = tk.Button(self.parameter_frame)
        self.three["text"] = "1"
        self.three.grid(row=button_row, column=2)

        self.four = tk.Button(self.parameter_frame)
        self.four["text"] = "2"
        self.four.grid(row=button_row, column=3)

        # Up arrow button for positioning system
        self.upArrow = tk.Button(self.parameter_frame, compound=tk.TOP, width=155, height=55, image=self.upArrowPhoto)
        self.upArrow.grid(row = 6, sticky = tk.E+tk.W)



        # Plot Canvas
        self.plot_frame =tk.Frame(self)
        self.plot_frame.grid(row=1,column=2)
        self.data_figure = Figure(figsize=(5,5), dpi=100)
        self.data_figure_subplot = self.data_figure.add_subplot(111)
        self.data_figure_subplot.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        self.data_canvas = FigureCanvasTkAgg(self.data_figure, self.plot_frame)
        self.data_canvas.draw()
        self.data_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.toolbar = NavigationToolbar2TkAgg(self.data_canvas, self.plot_frame)
        self.toolbar.update()
        self.data_canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)






    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        # option is needed to put the main label in the window
        self.init_attributes()
        self.createWidgets()

        
    


