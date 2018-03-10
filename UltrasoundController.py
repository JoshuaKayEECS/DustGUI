
import time 
import serial

class UltrasoundController:

	f_clk = 50e6
	f_pulse = 2.8e6
	f_repition = 1e3
	compare_pulse = int(round(f_clk/(f_pulse*2)))
	compare_repition = int(round(f_clk/f_repition))
	n_pulse = int(2*5)
	#ser = serial.Serial(
	#		port = 'COM5',
	#		baudrate = 50000
	#		)

	def __init__(self,comPort):
		#self.ser = serial.Serial(
		#			port = comPort,
		#			baudrate = 50000
		#			)
		#if self.ser.isOpen() :
		print "Port Open During Initilization"

	def closePort(self):
		self.ser.close()
		if not self.ser.isOpen() :
			print "Port Closed"

	def TxParameters(self,f_pulse,f_repition,pulses):
		self.f_pulse = f_pulse
		self.f_repition = f_repition
		self.compare_pulse = int(round(self.f_clk/(self.f_pulse*2)))
		self.compare_repition = int(round(self.f_clk/self.f_repition))
		self.n_pulse = int(2*pulses)


		if self.ser.isOpen() :
			print "Port Open After Initilization"

		commands = ['0','1','2','3','4','5','6','7']
		i = 0

		for c in commands:
			self.ser.write(c)
			out = ''
			#time.sleep(1)

			# send first byte of compare_pulse
			if i == 1:
				tx_byte = self.compare_pulse & 0xFF
				self.ser.write(chr(tx_byte))
				print "Sent> ", hex(tx_byte)
			# send 2nd byte of compare_pulse
			if i == 2:
				tx_byte = (self.compare_pulse >> 8) & 0xFF
				self.ser.write(chr(tx_byte))
				print "Sent> ", hex(tx_byte)
	
			# send 1st byte of compare_repition
			if i == 3:
				tx_byte = (self.compare_repition) & 0xFF
				self.ser.write(chr(tx_byte))
				print "Sent> ", hex(tx_byte)

			# send 2nd byte of compare_repition
			if i == 4:
				tx_byte = (self.compare_repition >> 8) & 0xFF
				self.ser.write(chr(tx_byte))
				print "Sent> ", hex(tx_byte)

			# send 3rd byte of compare_repition
			if i == 5:
				tx_byte = (self.compare_repition >> 16) & 0xFF
				self.ser.write(chr(tx_byte))
				print "Sent> ", hex(tx_byte)

			# send n_pulse
			if i == 6:
				tx_byte = self.n_pulse & 0xFF
				self.ser.write(chr(tx_byte))
				print "Sent> ", hex(tx_byte)
	
			#time.sleep(1)
			rx_int = -1
			while self.ser.inWaiting() > 0:
				rx = self.ser.read(1)
				if(rx == c):
					out += rx
				else:
					rx_int = ord(rx)

			if rx_int != -1:
				print "Echo> ", hex(rx_int)
			if out != '':
				print "Received> " + out

			i = i + 1
		
	def stop(self):

		if self.ser.isOpen() :
			print "Port Open After Initilization"

		commands = ['0']
		c = '0'
		self.ser.write(c)
		
		#for c in commands:
		#	self.ser.write(c)
		#	out = ''

#			while self.ser.inWaiting() > 0:
#				out += out
#			
#
###			i = i + 1
