import time
import board
import busio
import digitalio
import time

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface


score_button=digitalio.DigitalInOut(board.GP5) #Initalize score_button and attach it to GP3
ball_count_button=digitalio.DigitalInOut(board.GP12) #Initalize ball_count_button and attach it to GP2
score_button.direction = digitalio.Direction.INPUT
ball_count_button.direction = digitalio.Direction.INPUT
score_button.pull = digitalio.Pull.UP

score_button.value
print(score_button.value)

# Initialize the score variable
score = 0
# Initialize the ball count variable to 3 because the gamestarts with three balls
ball_count= 3

# Initialize I2C bus.
# The Raspberry Pi pico has a number of pin pairs that can be used for I2C.
# One pin is SCL (clock) and the other is SDA (data).  See
# a pin diagram at
i2c = busio.I2C(board.GP1, board.GP0)

# Talk to the LCD at I2C address 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=20)
lcd.set_backlight(True)

while True:
    lcd.clear()
    # Start at the first line, fifth column (numbering from zero).
    lcd.set_cursor_pos(0, 1)
    lcd.print("Hello")
    lcd.print("Hello")
    lcd.print("Hello")
    # Start at the first line, fifth column (numbering from zero).
    lcd.set_cursor_pos(1, 2)
    lcd.print("Score: ")
    lcd.print(str(score))
    time.sleep(4)


    lcd.clear()
    lcd.set_cursor_pos(0, 1)
    lcd.print("Ball Count")
    lcd.set_cursor_pos(1, 2)
    lcd.print("#:")
    #Prints
    lcd.print(str(ball_count))
    time.sleep(2)

    lcd.clear()

    if score_button.value == False:
        score= score+5   #Increases ball count value by 1 when pressed
    if ball_count_button.value == False:
        ball_count=ball_count+1

    # Make the screen scroll sideways
    for i in range (0,20):
        lcd.shift_display(1)
        time.sleep(.25)

    # Bump the score for the next iteration of the loop
    #Increases Score value by 5 when pressed



