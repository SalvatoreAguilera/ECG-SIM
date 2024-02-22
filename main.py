
from tkinter import *
 
root = Tk() 
  
root.geometry( "300x300" ) 
  
def newWindow(): 
    window = Tk()
    window.geometry( "800x200" )
    window.title( clicked.get() )
    window.configure( background='black' )
  
options = [ 
    "Normal Rhytms", 
    "Other", 
    "Other", 
    "other", 
    "Other", 
    "Other", 
    "Other"
] 
  
clicked = StringVar() 
  
clicked.set( " Heart Rhytms " ) 
  
drop = OptionMenu( root , clicked , *options ) 
drop.pack() 
  
button = Button( root , text = " Start " , command = newWindow ).pack() 
  
  
 
root.mainloop()