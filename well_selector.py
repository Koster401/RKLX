# WellSelector.py by Rasmus Köster Larsen (RKLX)
# First version

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ctypes import windll
from tkinter.tix import *
import os
import argparse


class WellSelector:

    """ This class contains the code for the well selector GUI """

    def __init__(self,
                 master,
                 plate_format = "8x12",
                 info_text = "",
                 title = "WellSelector"):

        """"Create all widgets needed for the WellSelector GUI

        Keyword arguments:
        master -- the top level widget
        plate_format -- The microplate format (default "8x12")
        info_text -- The heading text on the WellSelector (default "")
        title -- The text in the window header (default "WellSelector")

        """

        #Here we very stupidly try to input values if our script arguments were None
        if plate_format == None:
            plate_format = "8x12"

        if info_text == None:
            info_text = ""

        if title == None:
            title = "WellSelector"

        #Resizing of the window not allowed
        master.resizable(False, False)    
        
        self.style = ttk.Style()
        self.style.configure('TFrame', background = 'white')
        self.style.configure('TLabel', background = 'white')
        self.style.configure('TCheckbutton', background = 'white')
        master.configure(background = 'white')

        self.tip = Balloon(master)
        
        #Creating the title        
        master.title(title)

        #Creating the top level widget
        self.label = ttk.Label(master,
                               text = info_text,
                               font = ("bold"))

        #Creating the header widget and placing it
        self.label.grid(row = 0,
                        column = 0,
                        padx = 5,
                        pady = 5,
                        sticky = 'sw')

        #Creating the WellSelector frame and placing it
        self.frame = Frame(master,
                           highlightbackground = "lightgrey",
                           highlightthickness = 1,
                           background = 'white')
        self.frame.grid(row = 1,
                        column = 0,
                        padx = 5,
                        pady = 5,
                        ipadx = 10,
                        ipady = 10)
        #Calculating the plateformat
        self.plate_xloc = plate_format.index("x")
        self.plate_nrows = int(plate_format[0:self.plate_xloc])
        self.plate_ncols = int(plate_format[self.plate_xloc+1:])

        #Writing down the alphabet like an ape
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
        self.check_value = IntVar()
        
        #Creating and placing the letter labels of the plate
        for i in range(self.plate_nrows):
            ttk.Label(self.frame, text = self.letters[i]).grid(row = i + 1,
                                                               column = 0,
                                                               padx = 2,
                                                               sticky = "w")
        #Creating and placing the number labels of the plate
        for i in range(self.plate_ncols):
            ttk.Label(self.frame, text = str(i + 1)).grid(row = 0,
                                                          column = i + 1,
                                                          sticky = "s")

        #Making empty variables and lists
        self.check_button_counter = 0
        self.check_button_variable_list = []
        self.well_list = []
        global check_button_list
        global well_list

        #Creating and placing the checkboxes
        for i in range(self.plate_ncols):
            for j in range(self.plate_nrows):
                self.well = f"{self.letters[j]}{i+1}"
                self.well_list.append(self.well)
                self.check_button_variable_list.append(IntVar())
                self.check_button = Checkbutton(self.frame,
                                                variable = self.check_button_variable_list[self.check_button_counter],
                                                selectcolor="blue",
                                                indicatoron=False,
                                                width = 3,
                                                height = 1)
                self.check_button.grid(row = j + 1,
                                       column = i + 1,
                                       ipadx = 2,
                                       ipady = 2,
                                       padx = 2,
                                       pady = 2)
                self.tip.bind_widget(self.check_button,
                             balloonmsg = self.well)
                
                self.check_button_counter += 1

        #Updating the list of checkbutton variables
        check_button_list = self.check_button_variable_list
        well_list = self.well_list
        
        #Creating and placing the Done button
        ttk.Button(master,
                   text = "Done",
                   command = lambda: [self.done(), master.destroy()]).grid(row = 2,
                                                                           column = 0,
                                                                           padx = 5,
                                                                           pady = 5)

        
        #This fixes grainy widgets
        windll.shcore.SetProcessDpiAwareness(1)
    
    def done(self):
        
        """"This function retrieves the state of the check_button_list and writes it to an outputfile"""

        #Getting the list of checkbutton variables
        global check_button_list
        self.check_button_state_list = []

        #Finding the script location and defining our outputfile
        self.dir_output = f"{os.path.dirname(os.path.realpath(__file__))}\Output.csv"

        #Opening the outputfile and writing the header
        self.f = open(self.dir_output, "w")
        self.f.write("Well;State\n")

        #Going through the list of checkbutton variables and fetching the checkbutton state
        #Writing the well ID and the checkbox state in the outputfile
        for i in range(len(check_button_list)):
            self.check_button_value = check_button_list[i].get()
            print(f"{well_list[i]}: {self.check_button_value}")
            self.f.write(f"{well_list[i]}; {self.check_button_value}\n")
        self.f.close()
        
def main():

    """This function fetches any arguments passed with the script and parses them to the WellSelector class"""

    # Construct the argument parser
    ap = argparse.ArgumentParser()
    
    # Add the arguments to the parser
    ap.add_argument("-plate_format",
                    "--foperand",
                    required=False,
                    help="first operand")
    ap.add_argument("-info_text",
                    "--soperand",
                    required=False,
                    help="second operand")
    ap.add_argument("-title",
                    "--toperand",
                    required=False,
                    help="third operand")
    args = vars(ap.parse_args())

    #This fixes grainy widgets
    windll.shcore.SetProcessDpiAwareness(1)

    root = Tk()

    
    
    #Running the WellSelector class with the fetched script arguments
    app = WellSelector(root,
                       args["foperand"],
                       args["soperand"],
                       args["toperand"])

    root.mainloop()
    
if __name__ == "__main__": main()
