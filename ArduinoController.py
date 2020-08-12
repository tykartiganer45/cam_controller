import os
from serial import Serial
from time import sleep

serial = Serial('/dev/ttyACM0', 115200)


def power(toggle):
  if toggle == 1:  # Power On
    serial.write(' p'.encode())
    sleep(4.0)
    print("Power ON")
  elif toggle == 0:  # Power off
    serial.write(' o'.encode())
    sleep(4.0)
    print("Power OFF")
  else:
    raise Exception('Not a valid input')


def zoomin(magnitude):
  serial.write(' check'.encode())
  val = str(serial.readline().decode().strip('\r\n'))
  if val == '0' and magnitude >= 0 and magnitude <= 100:  # Zoom In
    magnitude = magnitude * 0.03;
    magnitudeStr = str(magnitude)
    serial.write((magnitudeStr + ' zi').encode())
    sleep(magnitude)
    print("Zoom In Done")
  elif val == '1' and magnitude >= 0 and magnitude <= 100:
    raise Exception('The cameras are in transfer mode')



def zoomout(magnitude):
  serial.write(' check'.encode())
  val = str(serial.readline().decode().strip('\r\n'))
  if val == '0' and magnitude >= 0 and magnitude <= 100:  # Zoom Out
    magnitude = magnitude * 0.03;
    magnitudeStr = str(magnitude)
    serial.write((magnitudeStr + ' zo').encode())
    sleep(magnitude)
    print("Zoom out Done")
  elif val == '1' and magnitude >= 0 and magnitude <= 100:
    raise Exception('The cameras are in transfer mode')


def startrecord():
  serial.write(' check'.encode())
  val = str(serial.readline().decode().strip('\r\n'))
  if val == '0':
    serial.write(' r'.encode())
    print("Started Recording")
  elif val == '1':
    raise Exception('The cameras are in transfer mode')

def stoprecord():
  serial.write(' check'.encode())
  val = str(serial.readline().decode().strip('\r\n'))
  if val == '0':
    serial.write(' s'.encode())
    print("Recording Stopped")
  elif val == '1':
    raise Exception('The cameras are in transfer mode')


def recordandcapture(seconds, snaps):
  serial.write(' check'.encode())
  val = str(serial.readline().decode().strip('\r\n'))
  if val == '0': 
    startrecord()
    i = 0
    while i < snaps:
      sleep(seconds / snaps)
      serial.write(' c'.encode())
      print("Capture Done")
      i = i + 1
    sleep(1.0)
    stoprecord()
    print("Recording Done")
  elif val =='1':
    raise Exception('The cameras are in transfer mode') 


def capture():
  serial.write(' check'.encode())
  val = str(serial.readline().decode().strip('\r\n'))
  if val == '0': 
    serial.write(' c'.encode())
    print("Capture Done")
  elif val =='1':
    raise Exception('The cameras are in transfer mode') 


def menu():
  serial.write(' check'.encode())
  val = str(serial.readline().decode().strip('\r\n'))
  if val == '0': 
    serial.write(' m'.encode())
    print("In Menu")
  elif val =='1':
    raise Exception('The cameras are in transfer mode') 


def ex():
  serial.write(' check'.encode())
  val = str(serial.readline().decode().strip('\r\n'))
  if val == '0': 
    serial.write(' e'.encode())
    print("Execute")
  elif val =='1':
    raise Exception('The cameras are in transfer mode')


def move():
  serial.write(' check'.encode())
  val = str(serial.readline().decode().strip('\r\n'))
  if val == '0': 
    serial.write(' mr'.encode())
    print('Move')
  elif val =='1':
    raise Exception('The cameras are in transfer mode')


def home():
  serial.write(' check'.encode())
  val = str(serial.readline().decode().strip('\r\n'))
  if val == '0': 
    serial.write(' home'.encode())
    sleep(16.0)
    print("Cameras are ready to record")
  elif val =='1':
    raise Exception('The cameras are in transfer mode')

def format():
  serial.write(' check'.encode())
  val = str(serial.readline().decode().strip('\r\n'))
  if val == '0': 
    serial.write(' format'.encode())
    sleep(40.0)
    print("SD Cards Formatted")
  elif val =='1':
    raise Exception('The cameras are in transfer mode')


def ft():
  serial.write(' check'.encode())
  val = str(serial.readline().decode().strip('\r\n'))
  if val == '0': 
    serial.write(' ft'.encode())
    sleep(45.0)
    print("SD Cards Formatted")
  elif val =='1':
    raise Exception('The cameras are in transfer mode')

def control(value):
  serial.write(' check'.encode())
  val = str(serial.readline().decode().strip('\r\n'))
  if val == '0': 
    valueStr = str(value)
    val = value - 1
    valStr = str(val)
    serial.write((valStr + ' con').encode())
    print("Controlling camera " + valueStr)
  elif val =='1':
    raise Exception('The cameras are in transfer mode')
9600

def transfer(toggle):
  serial.write(' check'.encode())
  val = str(serial.readline().decode().strip('\r\n'))
  if val == '0' and toggle == 1:  # Turn on Transfer
    serial.write(' ton'.encode())
    sleep(10.0)
    print("Transfer Mode On")
  elif val == '1' and toggle == 0:  # Turn off Transfer
    serial.write(' toff'.encode())
    sleep(2.0)
    print("Transfer Mode Off, command to Recording Screen")
  elif val == '1' and toggle == 1:
    raise Exception("Already in transfer mode")
  elif val == '0' and toggle == 0:
    raise Exception("Transfer mode already shut off")
  else:
    raise Exception("not a valid input")


def mount():
  mountCmd = 'sudo ./mount_cameras.sh'
  os.system(mountCmd)


def save():
  saveCmd = 'node /home/svcontroller/copy_scripts/app.js /media/svcontroller/cam_1:/home/svcontroller/Desktop/transfer/cam_1 /media/svcontroller/cam_2:/home/svcontroller/Desktop/transfer/cam_2 /media/svcontroller/cam_3:/home/svcontroller/Desktop/transfer/cam_3 /media/svcontroller/cam_4:/home/svcontroller/Desktop/transfer/cam_4 /media/svcontroller/cam_5:/home/svcontroller/Desktop/transfer/cam_5 /media/svcontroller/cam_6:/home/svcontroller/Desktop/transfer/cam_6 /media/svcontroller/cam_7:/home/svcontroller/Desktop/transfer/cam_7 /media/svcontroller/cam_8:/home/svcontroller/Desktop/transfer/cam_8 /media/svcontroller/cam_9:/home/svcontroller/Desktop/transfer/cam_9 /media/svcontroller/cam_10:/home/svcontroller/Desktop/transfer/cam_10 /media/svcontroller/cam_11:/home/svcontroller/Desktop/transfer/cam_11 /media/svcontroller/cam_12:/home/svcontroller/Desktop/transfer/cam_12 /media/svcontroller/cam_13:/home/svcontroller/Desktop/transfer/cam_13 /media/svcontroller/cam_14:/home/svcontroller/Desktop/transfer/cam_14'
  os.system(saveCmd)


def rmlocal():
  removeCmd = './delete_local.sh'
  os.system(removeCmd)

def manex():
    serial.write(' manex'.encode())
    sleep(50.0)
    print("Manual Exposure Set")

def steady():
    serial.write(' steady'.encode())
    sleep(54.0)
    print("Manual Exposure Set")

def expos(exposure_amount):
    print(exposure_amount)
    serial.write('{exposure_amount} mp'.format(exposure_amount=exposure_amount).encode())
    time = exposure_amount*3 + 4
    sleep(time)
    print("Increased exposure by {exposure_amount}".format(exposure_amount=exposure_amount))

def exneg(exposure_amount):
    print(exposure_amount)
    serial.write('{exposure_amount} mn'.format(exposure_amount=exposure_amount).encode())
    time = exposure_amount*3 + 4
    sleep(time)
    print("Decreased exposure by {exposure_amount}".format(exposure_amount=exposure_amount))

def autoex():
    serial.write(' autoex'.encode())
    sleep(50.0)
    print("Manual Exposure Set")
