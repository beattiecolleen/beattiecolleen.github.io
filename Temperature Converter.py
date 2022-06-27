#temperature converter

from tkinter import*

def convert():
    #input
    temp_f = float(tf_fahrenheit.get())
    
    #calculations
    temp_c = (temp_f - 32) * 5/9
    #output
    lb_celsius_output.config(text = '%8.2f'%(temp_c))
    
#GUI
window = Tk()
window.title('Temperature Converter')

#first line of GUI
lb_fahrenheit = Label(window, anchor = W, text = 'Temperature in Fahrenheit: ')
lb_fahrenheit.grid(row = 0, column = 0)
tf_fahrenheit = Entry(window)
tf_fahrenheit.grid(row = 0, column = 1)

#second line of GUI
lb_celsius = Label(window, anchor = W, text = 'Temperature in Celsius: ')
lb_celsius.grid(row = 1, column = 0)
lb_celsius_output = Label(window, bg = 'white', relief = SUNKEN, width = 20, anchor = W)
lb_celsius_output.grid(row = 1, column = 1)

#Button
bt_convert = Button(window, bg = 'salmon', text = 'convert to Celsius', command = convert)
bt_convert.grid (row = 2, column = 2)