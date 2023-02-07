import blynklib
from sense_hat import SenseHat
from BlynkTimer import BlynkTimer
from tuya_bulb_control import Bulb


BLYNK_AUTH = 'YOURKEYGOESHERE'

CLIENT_ID = ''
SECRET_KEY = ''
DEVICE_ID = ''
REGION_KEY = 'eu'

bulb = Bulb(
    client_id=CLIENT_ID,
    secret_key=SECRET_KEY,
    device_id=DEVICE_ID,
    region_key=REGION_KEY
)


sense = SenseHat()

#clear sensehat and intialise light_state
sense.clear()

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)
 
# Create BlynkTimer Instance
timer = BlynkTimer()

# Define sense.clear function 
def senseClear():
    sense.clear()

# register handler for virtual pin V1 write event
@blynk.handle_event('write V1')
def write_virtual_pin_handler(pin, value):
    print('V1:'+ str(value))
    r=int(value[0]) # or you could do this: value = list(map(int, value))
    g=int(value[1])
    b=int(value[2])
    # Change the color of the bulb
    bulb.set_colour_v2(rgb=(r, g, b))

# register handler for virtual pin V2 (Turn light on/off) write event
@blynk.handle_event('write V2')
def write_virtual_pin_handler(pin, value):
    print('V2:'+ str(value))
    if value[0]=="1":
        sense.clear(0,255,0)
        timer.set_timeout(1, senseClear)
        # Turn on the bulb
        bulb.turn_on()

    else:
        sense.clear(255,0,0)
        timer.set_timeout(1, senseClear)
        # Turn off the bulb
        bulb.turn_off()


while True:
    blynk.run()
    timer.run()
