

from asyncio.windows_events import NULL
from inspect import modulesbyfile
from itertools import filterfalse
import random
from secrets import randbelow
import PySimpleGUI as sg
import wristbandDataCollection


class Person:
  def __init__(self, name, age, weight,sensorNumber):
    self.name = name
    self.age = age
    self.weight = weight
    self.sensorNumber = sensorNumber
    

def Main_window():
    numberOfPatients = 0
    menu_def = [['File', 
                ['New', 
                 'Delete']]]
    sg.set_options(font=("Arial Bold", 14))
    toprow = ['S.No.', 'Name', 'Age', 'Weight', 'Pulse', 'o2']
    rows = [[1, "No Patient", 00, 00, 00]]
    tbl1 = sg.Table(values=rows, headings=toprow,
   auto_size_columns=True,
   display_row_numbers=False,
   justification='center', key='_TABLE_',
   selected_row_colors='red on yellow',
   enable_events=True,
   expand_x=True,
   expand_y=True,
   enable_click_events=True)
            
    layout = [[sg.Menu(menu_def)],
              [sg.Text("Hello This is the main window for the program")],
              [sg.Text("To add a new patient, go to FILE >> NEW")],
              [sg.Text("Patient Information")],
              [tbl1]

              
              ]
  
    window = sg.Window("Main", layout).Finalize()
    
    ##uncomment to maximize window
    window.Maximize()
    choice = None
    loop_counter = 0
    while True:
        event, values = window.read(timeout = 300)
        loop_counter += 1
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "New":
            print("Launching new window")
            p1 = new_window()
            print(rows[0])
            if p1 != 0: ##Determine ig the new window was canceled or data is good in move into database. 
                if rows[0][1] == "No Patient":
                    rows= [[p1.sensorNumber, p1.name, p1.age, p1.weight,"N/A","N/A"]]
                    window.Element('_TABLE_').update(values=rows)
                    numberOfPatients +=1
                else:
                    ## need to find how to get table size or make index some how.  
                    rows.append([p1.sensorNumber, p1.name, p1.age, p1.weight,"N/A","N/A"])
                    window.Element('_TABLE_').update(values=rows)
                    numberOfPatients +=1
            else:
                print("No new patient added!")
        if loop_counter == 10:
           print(numberOfPatients)
           i = 0 
           while i < numberOfPatients:
            rows[i][4] = wristbandDataCollection.wristband_pulse(rows[i][0])
            rows[i][5] = wristbandDataCollection.wristband_o2(rows[i][0])
            print("PULSE: ", rows[i][4], "O2 SAT:", rows[i][4])
            print(rows[i][4])
            i+=1
           
           ## Write function to fetch data from sensor. 
           window.Element('_TABLE_').update(values=rows)
           loop_counter = 0
            
               
               
            ##window.Element('_LISTBOX_").update(values=[p1.name, p1.age, p1.weight])
            
        
    window.close()

def open_window(p1):
    menu_def = [['File', 
                ['New', 
                 'Delete']]]
            
    layout = [[sg.Menu(menu_def)],
              [sg.Text(p1.name, key="new")],
              [sg.Text(p1.age, key="new")],
              [sg.Text(p1.weight, key="new")]
              
              ]
  
    window1 = sg.Window(p1.name, layout)
    choice = None
    while True:
        event, values = window1.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        
    window1.close()
    
def new_window():


   
   layout = [  [sg.Text('Welcome to patient check in. Please fill out the following information')],
            [sg.Text('Enter patient Name:'), sg.InputText()],
            [sg.Text('Enter patient Age'), sg.InputText()],
            [sg.Text('Enter patient Weights'), sg.InputText()],
            [sg.Text('Enter patient Sensor Number'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
   window = sg.Window('Patient log', layout)  

# Event Loop to process "events" and get the "values" of the inputs
   while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            p1=0
            break
        if event == 'Ok':
            print('You entered ', values[0], "for name and " , values[1], " for age and ", values[2], "for weight. Patient sensor number : ", values[3])
            p1 = Person(values[0],values[1],values[2], values[3])
            break
        

   window.close()
   return p1
   


def service_func():
    layout = [  [sg.Text('Welcome to patient check in. Please fill out the following information')],
            [sg.Text('Enter patient Name:'), sg.InputText()],
            [sg.Text('Enter patient Age'), sg.InputText()],
            [sg.Text('Enter patient Weights'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Patient Viatals log', layout)  

# Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        print('You entered ', values[0], "for name and " , values[1], " for age and ", values[2], "for weight.")
        p1 = Person(values[0],values[1],values[2])
        open_window(p1)
        

    window.close()


Main_window()

   