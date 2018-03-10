
from MainAppView import MainAppView
from UltrasoundController import UltrasoundController


class MainAppController(object):  


    def nothing(self):
        print "nothing"

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
        self.view.three["command"] = self.nothing
        self.view.four["command"] = self.nothing

        # Start the gui 
        self.view.start_gui()

    def close(self):
        self.us.closePort()
        


