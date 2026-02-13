# Universal Magnetra2 Adapter
Magnetra2 uses an i2c protocol over a TRRS 3.5mm jack. The controllers each have a TI ADS7830 A/D converter chip that has 8 channels and can be read via i2c.  

## Controller Channel Mappings Below:

CH0 - Joystick Y (128 = centered)

CH1 - Joystick X (128 = centered)

CH2 - Analog Trigger (68/67 = centered)

CH3 - B Button (0 = pressed, 255 = unpressed)

CH4 - Ladder value:

    1 = Joystick Press 

    128/127~ = D PAD Up / trackpad up

    170 = Steam Menu

CH5 - D PAD Down / trackpad Down (0 = pressed, 255 = unpressed)

CH6 - A Button (0 = pressed, 255 = unpressed)

CH7 - Right Trigger Press (0 = pressed, 255 = unpressed)

Datasheet: 
https://www.ti.com/lit/ds/symlink/ads7830.pdf?ts=1770950272024&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FADS7830


## Equipment used: 

[HiLetgo CH341T USB i2c bridge](https://www.amazon.com/dp/B0CDWWN79M)

[BOJACK Bread Board](https://www.amazon.com/dp/B08Y59P6D1)

[BOJACK Resistors (for pull up)](https://www.amazon.com/dp/B08FD1XVL6)

    - Used 10kOhm but I believe 4.7kOhms as will work fine 

