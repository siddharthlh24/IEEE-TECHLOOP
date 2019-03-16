from pynput.keyboard import Key, Controller

keyboard = Controller()

# Press and release space
keyboard.press(Key.cmd)
keyboard.press(Key.print_screen)
keyboard.release(Key.cmd)
keyboard.release(Key.print_screen)



#use keyboard event listener to generate key combinations for multiple functions
#such as brightness, volume etc.
#one issue is 'Fn' is not detected


#make them control each other's games etc.
