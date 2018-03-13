
from MainAppView import MainAppView
from UltrasoundController import UltrasoundController


class MainAppController(object):  


    def J(self):
        print "Josh is Cool"
    
    def V(self):
        print "Vicky is cool"

    def stopCommand(self):
        self.us.stop()

    def TxParametersButton(self):
        self.us.TxParameters(f_pulse=0.5e6,f_repition=1e3,pulses=5)


    def init_view(self,root):
        """Initializes GUI view

            In addition it bindes the Buttons with the callback methods.

           
        """
        self.view = MainAppView(master=root)

        self.us = UltrasoundController(comPort = 'COM4')   

        print "After Initialization"
    
        # Bind buttons with callback methods
        self.view.sendTx["command"] = self.TxParametersButton
        self.view.stop["command"] = self.stopCommand
        self.view.three["command"] = self.J
        self.view.four["command"] = self.V

        # Start the gui 
        self.view.start_gui()

    def close(self):
        self.us.closePort()
        


