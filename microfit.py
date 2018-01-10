from microbit import*
steps = 0 

while True:
    
    display.show(str(steps))
    gesture = accelerometer.current_gesture()
    if gesture == "left":  
        steps = steps + 1
        sleep(1000)