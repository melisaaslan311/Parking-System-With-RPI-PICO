# Parking-System-With-RPI-PICO
🏎️Project Description
The Smart Parking System is an automated solution designed to manage parking availability using a Raspberry Pi Pico WH, an ultrasonic distance sensor, and a servo motor. The system detects incoming vehicles, displays available parking spaces on an LCD screen, and controls a barrier arm to regulate entry. The project also integrates an RGB LED for visual indication of parking status and allows for manual resetting using a push button.

🛠️Components Used
-Microcontroller: Raspberry Pi Pico WH
-Motor: Servo Motor
-Sensor: Ultrasonic Distance Sensor (HC-SR04)
-LEDs: RGB LED (Common Cathode) & Red LED
-Display: LCD Screen (16x2 with I2C module)
-Potentiometers: Two (for RGB color adjustment and LCD contrast control)
-Buzzer: For alert sounds
-Button: System reset button
-Power Supply: 5V USB power
-Software & Development Environment
-Programming Language: MicroPython
-IDE Used: Thonny IDE

🧾Features & Functionality
-Vehicle Detection: 
1)The ultrasonic sensor detects approaching vehicles within 10 cm.

-Automatic Barrier Control:
1)If a parking spot is available, the servo motor opens the barrier with a buzzer sound and closes after a short delay.
2)If the parking lot is full, the barrier remains closed, and the LCD displays "Parking Lot Full".

-Parking Status Indication:
1)The LCD screen updates dynamically with the number of available parking spaces.

-RGB LED Signals:
1)Green: 0 cars parked (empty lot)
2)Blue: 3-5 cars parked (moderately full)
3)Red + Purple LED: No space left (full lot)

-Manual Adjustments:
1)Potentiometer 1: Adjusts RGB LED colors.
2)Potentiometer 2: Controls LCD screen contrast.

-System Reset:
1)Pressing the reset button restores the parking capacity to 6 slots.
2)How It Works:

2.a)System Initialization:
--The microcontroller sets up the LCD, sensors, and motors.
--The initial parking capacity is displayed.
2.b)Vehicle Detection & Entry:
--If a vehicle is within 10 cm and there is available space:
--The barrier opens with a beep.
--The LCD updates the available slots.
--The barrier closes after a short delay.
--If the parking lot is full, the barrier remains closed, and the LCD shows "Parking Lot Full".

-Real-Time Monitoring:
1)The RGB LED and LCD continuously update to reflect parking status.

-Reset Mechanism:
1)Pressing the reset button restores parking availability to 6 slots.
![final_homework_bb](https://github.com/user-attachments/assets/3cba55ff-48c8-45f9-865f-d6674379f52b)



https://github.com/user-attachments/assets/7c1f0e93-c17c-4523-a3de-da709a6c15e8

