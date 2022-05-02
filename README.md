# WellSelector

This script allows users to select wells from a microplate format.

When running the script it uses the default settings to generate a GUI in a 8x12 format with no label text and the windowtitle "WellSelector".

You can change the what parameters are being fed to WellSelector under main #Setting default script parameters for WellSelector. If the script receives no arguments it will default to these settings.

You can run the script from the commandline or from other programs and parse the arguments -plate_format, -info_text and -title. 

- The -plate_format tells the GUI how many rowsXColumns that the microplate overview needs to have.
- The -info_text tells the GUI what to write as a header over the microplate overview.
- The title tells the GUI what the name of the window running the GUI should be.

Example of running the GUI through powershell in the script directory: *.\well_selector.py -plate_format "8x12" -info_text "Choose your target wells" -title "WellSelector"

When pressing the button "Done", 3 things will happen:

1. The well ID and the state of each checkbutton, with selected being 1 and unselected being 0, is printed to the console
2. The same list is written to the outputfile Output.csv in a csv format
3. The Gui is closed

Hopefully this is all what is needed for you to succesfully use the WellSelector GUI

- Rasmus
