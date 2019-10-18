# Add your Python code here. E.g.
import microbit
#imports the microbit radio library
import radio

radio.on()
#configures the channel on which channel to transmit information
radio.config(channel=10)

height = 1

while True:
    #get´s x and y values from the micobit
    x = microbit.accelerometer.get_x()
    y = microbit.accelerometer.get_y()
    
    #lights up the main pixels
    microbit.display.set_pixel(2, 2, 9)
    microbit.display.set_pixel(0, 4, 9)
    
    #if the y or x value are larger or smaller than 180, send message and display pixel
    if y > 180:
        microbit.display.set_pixel(2, 3, 9)
        microbit.display.set_pixel(2, 1, 0)
        microbit.display.set_pixel(1, 2, 0)
        microbit.display.set_pixel(3, 2, 0)
        radio.send("down")
       
    elif y < -180:
        microbit.display.set_pixel(2, 3, 0)
        microbit.display.set_pixel(2, 1, 9)  
        microbit.display.set_pixel(1, 2, 0)
        microbit.display.set_pixel(3, 2, 0)
        radio.send("up")
        
    elif x > 180:
        microbit.display.set_pixel(2, 3, 0)
        microbit.display.set_pixel(2, 1, 0)  
        microbit.display.set_pixel(1, 2, 9)
        microbit.display.set_pixel(3, 2, 0)
        radio.send("left")
       
    elif x < -180:
        microbit.display.set_pixel(2, 3, 0)
        microbit.display.set_pixel(2, 1, 0) 
        microbit.display.set_pixel(1, 2, 0)
        microbit.display.set_pixel(3, 2, 9)
        radio.send("right")
        
    #if both values correspond, send messsage
    if x > 180 and y > 180:
        microbit.display.set_pixel(2, 3, 9)
        microbit.display.set_pixel(2, 1, 0) 
        microbit.display.set_pixel(1, 2, 0)
        microbit.display.set_pixel(3, 2, 9)
        radio.send("br")
    
    if x < -180 and y < -180:
        microbit.display.set_pixel(2, 3, 0)
        microbit.display.set_pixel(2, 1, 9) 
        microbit.display.set_pixel(1, 2, 9)
        microbit.display.set_pixel(3, 2, 0)
        radio.send("tl")
    
    if x < -180 and y > 180:
        microbit.display.set_pixel(2, 3, 9)
        microbit.display.set_pixel(2, 1, 0) 
        microbit.display.set_pixel(1, 2, 9)
        microbit.display.set_pixel(3, 2, 0)
        radio.send("bl")
    
    if x > 180 and y < -180:
        microbit.display.set_pixel(2, 3, 0)
        microbit.display.set_pixel(2, 1, 9) 
        microbit.display.set_pixel(1, 2, 0)
        microbit.display.set_pixel(3, 2, 9)
        radio.send("tr")   
        
      #if a button is pressed, send message and delay  
    if microbit.button_a.was_pressed():
        height += 1
        radio.send("plus")
        microbit.sleep(50)
        
    if microbit.button_b.was_pressed():
        height -= 1
        radio.send("minus")
        microbit.sleep(50)
        
