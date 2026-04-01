from gpiozero import PWMOutputDevice, DigitalOutputDevice, DigitalInputDevice


IN1 = DigitalOutputDevice(6)
IN2 = DigitalOutputDevice(5)
ENA = PWMOutputDevice(13)
IN3 = DigitalOutputDevice(15)
IN4 = DigitalOutputDevice(14)
ENB = PWMOutputDevice(18)
IR_G = DigitalInputDevice(23)
IR_D = DigitalInputDevice(24)
# ENC_G = 27
# ENC_D = 22
# DEL_J = DigitalOutputDevice(10)
# DEL_V = DigitalOutputDevice(9)
# SON_G_TRG = 8
# SON_G_ECH = 25
# SON_D_TRG = 21
# SON_D_ECH = 20
