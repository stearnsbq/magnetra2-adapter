from i2cpy import I2C
import vgamepad as vg

"""
basic i2c channel to controller output using vgamepad for testing purpose only. 

"""


MAGNETRA2_ADDR = 74

i2c = I2C()     

gamepad = vg.VX360Gamepad()

def build_command(channel):
    """
    Build ADS7830 command byte we need to see channels:
    Bit7 = 1 (single-ended mode)
    Bits6-4 = channel number (0-7)
    Bits3-2 = power-down bits (0b01 = ADC on)
    Bits1-0 = not used
    """
    return 0x80 | ((channel & 0x07) << 4) | 0x04

def read_channel(channel):
    cmd = build_command(channel)

    i2c.writeto(MAGNETRA2_ADDR, bytes([cmd]))

    result = i2c.readfrom(MAGNETRA2_ADDR, 1)

    return result[0]


try:
    while True:
        for ch in range(8):
            
            value = read_channel(ch)

            match ch:
                case 0 | 1:
                    # values range from 0 - 255 but center joystick is 128 x 128 y so we need to do the expansion here for the controller lib
                    x_axis_signed = int((read_channel(0) - 128) * 256) # expansion from 128 to -32768 to 32767
                    y_axis_signed = int((read_channel(1) - 128) * 256) # expansion from 128 to -32768 to 32767
                    gamepad.right_joystick(y_axis_signed, x_axis_signed)
                    gamepad.update()
                case 2:
                    gamepad.right_trigger((value - 68) * 2) # trigger starts at 68/67 ~ need to do the expansion here 
                    gamepad.update()
                case 3:
                    if value == 0:
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
                        gamepad.update()
                    else:
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
                        gamepad.update()
                case 4:
                    if value == 1:
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
                        gamepad.update()
                    elif value == 170:
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
                        gamepad.update()
                    elif value == 127 or value == 128:
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
                        gamepad.update()
                    else:
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
                        gamepad.update()
                case 5:
                    if value == 0:
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
                        gamepad.update()
                    else:
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
                        gamepad.update()
                case 6:
                    if value == 0:
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                        gamepad.update()
                    else:
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                        gamepad.update()
                case 7:
                    if value == 0:
                        gamepad.right_trigger(255)
                        gamepad.update()


        #print("-----")
        #time.sleep(0.5)

except KeyboardInterrupt:
    print("Stopping...")
    i2c.deinit()

