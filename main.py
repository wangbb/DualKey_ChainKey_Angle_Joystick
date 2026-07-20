import os, sys, io
import M5
from M5 import *
from chain import KeyChain
from chain import JoystickChain
from hardware import RGB
import time
from usb.device.keyboard import Keyboard 
from chain import AngleChain
from chain import ChainBus
from usb.device.hid import KeyCode



rgb = None
keyboard = None
bus2 = None
chain_key_0 = None
chain_angle_0 = None
chain_joystick_0 = None


Dual_AFlag = None
ChainBtn_Flag = None
Dual_BFlag = None
JStick_Flag = None
value = None
lastTime = None
lastValue = None
x = None
y = None


def btnA_wasClicked_event(state):
  global rgb, keyboard, bus2, chain_key_0, chain_angle_0, chain_joystick_0, Dual_AFlag, ChainBtn_Flag, Dual_BFlag, JStick_Flag, value, lastTime, lastValue, x, y
  Dual_AFlag = True


def chain_key_0_click_event(args):
  global rgb, keyboard, bus2, chain_key_0, chain_angle_0, chain_joystick_0, Dual_AFlag, ChainBtn_Flag, Dual_BFlag, JStick_Flag, value, lastTime, lastValue, x, y
  ChainBtn_Flag = True


def btnB_wasClicked_event(state):
  global rgb, keyboard, bus2, chain_key_0, chain_angle_0, chain_joystick_0, Dual_AFlag, ChainBtn_Flag, Dual_BFlag, JStick_Flag, value, lastTime, lastValue, x, y
  Dual_BFlag = True


def chain_joystick_0_click_event(args):
  global rgb, keyboard, bus2, chain_key_0, chain_angle_0, chain_joystick_0, Dual_AFlag, ChainBtn_Flag, Dual_BFlag, JStick_Flag, value, lastTime, lastValue, x, y
  JStick_Flag = True


def setup():
  global rgb, keyboard, bus2, chain_key_0, chain_angle_0, chain_joystick_0, Dual_AFlag, ChainBtn_Flag, Dual_BFlag, JStick_Flag, value, lastTime, lastValue, x, y

  M5.begin()
  BtnA.setCallback(type=BtnA.CB_TYPE.WAS_CLICKED, cb=btnA_wasClicked_event)
  BtnB.setCallback(type=BtnB.CB_TYPE.WAS_CLICKED, cb=btnB_wasClicked_event)

  rgb = RGB()
  time.sleep(3)
  keyboard = Keyboard()
  bus2 = ChainBus(2, tx=6, rx=5)
  chain_joystick_0 = JoystickChain(bus2, 1)
  chain_joystick_0.set_click_callback(chain_joystick_0_click_event)
  chain_key_0 = KeyChain(bus2, 2)
  chain_key_0.set_click_callback(chain_key_0_click_event)
  chain_angle_0 = AngleChain(bus2, 3)
  Dual_AFlag = False
  Dual_BFlag = False
  ChainBtn_Flag = False
  JStick_Flag = False
  lastTime = time.ticks_ms()
  rgb.set_color(0, 0x3366ff)
  rgb.set_color(1, 0x000066)
  value = chain_angle_0.get_adc8()
  lastValue = chain_angle_0.get_adc8()


def loop():
  global rgb, keyboard, bus2, chain_key_0, chain_angle_0, chain_joystick_0, Dual_AFlag, ChainBtn_Flag, Dual_BFlag, JStick_Flag, value, lastTime, lastValue, x, y
  M5.update()
  if (time.ticks_diff((time.ticks_ms()), lastTime)) > 30:
    value = chain_angle_0.get_adc8()
    lastTime = time.ticks_ms()
    if value - lastValue > 2:
      lastValue = value
      if keyboard.is_open():
        keyboard.input(KeyCode.EQUAL)
    elif value - lastValue < -2:
      lastValue = value
      if keyboard.is_open():
        keyboard.input(KeyCode.MINUS)
    x = int(chain_joystick_0.get_x())
    y = int(chain_joystick_0.get_y())
    if x != 0 or y != 0:
      if x > 40:
        if keyboard.is_open():
          keyboard.input(KeyCode.RIGHT)
      elif x < -40:
        if keyboard.is_open():
          keyboard.input(KeyCode.LEFT)
      if y > 40:
        if keyboard.is_open():
          keyboard.input(KeyCode.UP)
      elif y < -40:
        if keyboard.is_open():
          keyboard.input(KeyCode.DOWN)
    if Dual_AFlag == True:
      Dual_AFlag = False
      if keyboard.is_open():
        keyboard.input(KeyCode.PAGEUP)
    if Dual_BFlag == True:
      Dual_BFlag = False
      if keyboard.is_open():
        keyboard.input(KeyCode.PAGEDOWN)
    if ChainBtn_Flag == True:
      ChainBtn_Flag = False
      if keyboard.is_open():
        keyboard.input(KeyCode.DELETE)
    if JStick_Flag == True:
      JStick_Flag = False
      if keyboard.is_open():
        keyboard.input(KeyCode.INSERT)


if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      bus2.deinit()
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")
