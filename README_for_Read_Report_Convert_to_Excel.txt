##  This code was written by Barry Guglielmo. Python 3.6.3 used on a windows 10 machine. Module used: Openpyxl.


##  OBJECTIVE_________________________________________________________________________________________
##  The purpose of this code is to compile the Report.TXT files that are generated by Agilent OpenLab
##  when integrating the chromatograms collected from our GC. It simply takes all integrated reports
##  and pastes them into an Excel Template. Believe it or not, this saves us a fair amount of tedium.



##  HOW TO RUN THIS CODE ______________________________________________________________________________
##  So long as you have python 3.6 or later downloaded you will only have to download one module called
##  openpyxl. To download openpyxl open a command prompt (cmd) ?this can be found by typing “cmd” in your
##  computers search bar? In your command prompt type “pip install openpyxl”, if prompted that other modules
##  are necessary or other modules have not been found do the same “pip install” method for those modules.
##
##  Right Click File Run with IDLE 3.6.3 or Later. When the IDLE screen shows up simply press F5, or go to the
##  Run -> Run Module on the top of the screen. When prompted by python shell type in file name. For example
##  File name  might be 032118S. Then the shell will prompt for the name you want to save the output excel sheet
##  as. I typically type the same name again 032118S.

## !!!! The only part of the code you need to change are the Paths to Fetch and Write data and the Sheet name to paste to !!!! ##
## !!!!                     Be sure to use forward slashes / for Path names                                               !!!! ## 
## !!!!                  You will see the Paths in the Top section of the Code                                            !!!! ##
