from machine import Pin, PWM, ADC
import time

button = Pin(13, Pin.IN, Pin.PULL_DOWN)
buzzer = Pin(9, Pin.OUT)

rgb_red = PWM(Pin(6))  
rgb_green = PWM(Pin(7)) 
rgb_blue = PWM(Pin(8)) 
rgb_red.freq(1000)
rgb_green.freq(1000)
rgb_blue.freq(1000)

normal_led = Pin(14, Pin.OUT) 

pot_rgb = ADC(Pin(26))  
pot_lcd = ADC(Pin(27))  

RS = Pin(0, Pin.OUT)
EN = Pin(1, Pin.OUT)
D4 = Pin(2, Pin.OUT)
D5 = Pin(3, Pin.OUT)
D6 = Pin(4, Pin.OUT)
D7 = Pin(5, Pin.OUT)

servo = PWM(Pin(12))
servo.freq(50)
trigger = Pin(10, Pin.OUT)
echo = Pin(11, Pin.IN)
max_space = 6  

def lcd_command(cmd):
    RS.value(0)
    send_data(cmd, is_data=False)
    
def lcd_init():
    time.sleep(0.05)
    lcd_command(0x33)  
    lcd_command(0x32)  
    lcd_command(0x28)  
    lcd_command(0x0C) 
    lcd_command(0x06)  
    lcd_command(0x01)
    time.sleep(0.01)

def lcd_data(data):
    RS.value(1)
    send_data(data, is_data=True)

def send_data(value, is_data=True):
    RS.value(is_data)
    D4.value((value >> 4) & 0x01)
    D5.value((value >> 5) & 0x01)
    D6.value((value >> 6) & 0x01)
    D7.value((value >> 7) & 0x01)
    EN.value(1)
    time.sleep(0.001)
    EN.value(0)
    time.sleep(0.001)  
    D4.value(value & 0x01)
    D5.value((value >> 1) & 0x01)
    D6.value((value >> 2) & 0x01)
    D7.value((value >> 3) & 0x01)
    EN.value(1)
    time.sleep(0.001)
    EN.value(0)
    time.sleep(0.002)  

def lcd_clear():
    lcd_command(0x01)

def lcd_putstr(text):
    for char in text:
        lcd_data(ord(char))

def measure_distance():
    trigger.low()
    time.sleep_us(1)
    trigger.high()
    time.sleep_us(1)
    trigger.low()

    while echo.value() == 0:
        start = time.ticks_us()

    while echo.value() == 1:
        end = time.ticks_us()

    times = time.ticks_diff(end,start)
    distance = times * 0.0343 / 2  
    return distance

def move_servo(angle):
    duty = int((angle / 180) * 65535 * 0.1 + 65535 * 0.05) 
    servo.duty_u16(duty)

def rgb_led():
    global max_space
    pot_value = pot_rgb.read_u16()
    stage = pot_value // (65535 // 3)
    if stage == 0:
        red_value = 65535
        green_value = 0
        blue_value = 0
        normal_led.on()
    elif stage == 1:
        red_value = 0
        green_value = 65535
        blue_value = 0
        normal_led.off()
    else:
        red_value = 0
        green_value = 0
        blue_value = 65535
        normal_led.off()

    rgb_red.duty_u16(red_value)
    rgb_green.duty_u16(green_value)
    rgb_blue.duty_u16(blue_value)

def display_lcd():
    lcd_clear()
    if max_space == 0:
        lcd_putstr("Parking Full")  
    else:
        lcd_putstr(f"Vacant Spot: {max_space}")
    time.sleep(0.5)
    
def reset():
    if button.value() == 1:
        global max_space
        max_space = 6 
        print("System Reset")
        time.sleep(1)
        
def warning():
    for _ in range(3):
        buzzer.high()
        time.sleep(0.1)
        buzzer.low()
        time.sleep(0.1)
        
lcd_init()
while True:
    if max_space > 0:
        distance = measure_distance()
        if distance < 10:  
            if max_space > 0:
                max_space -= 1
                warning()  
                move_servo(90)
                time.sleep(2) 
                move_servo(0)
            time.sleep(1)
        rgb_led()
        display_lcd()
        reset()
    else:
        lcd_clear()
        lcd_putstr("Parking Full")
        time.sleep(0.5)
        reset()  
    time.sleep(0.1)


