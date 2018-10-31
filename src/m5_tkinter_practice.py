"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Achintya Gupta.
"""  # TO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # TO: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
    root = tkinter.Tk()



    # ------------------------------------------------------------------
    # TO: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------
    frame = ttk.Frame(root, padding=10)
    frame.grid()
    # ------------------------------------------------------------------
    # TO: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------
    button = ttk.Button(frame,text='Pointless Button')
    numkeeper=Obj()

    # ------------------------------------------------------------------
    # TO: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    button['command']=(lambda:
                       do_stuff(numkeeper))
    button.grid()
    # ------------------------------------------------------------------
    # TO: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------
    entrybox = ttk.Entry(frame)
    entrybox.grid()
    button2 = ttk.Button(frame,text='Less Pointless Button')
    button2['command']=(lambda:
                       do_more_stuff(entrybox))
    button2.grid()
    # ------------------------------------------------------------------
    # TO: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    entrybox2=ttk.Entry(frame)
    entrybox2.grid()
    button3=ttk.Button(frame,text='Even Less Pointless Button')
    button3['command']=(lambda:
                        do_even_more_stuff(entrybox,entrybox2))
    button3.grid()

    # ------------------------------------------------------------------
    # TODO: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------

    root.mainloop()
class Obj(object):
    def __init__(self):
        self.num=0
def do_stuff(Obj):
    Obj.num=Obj.num+1
    print('Warning! Pointless')
    print(Obj.num, 'pointless')
def do_more_stuff(entry):
    if entry.get()=='ok':
        print('Hello')
    else:
        print('Goodbye')
def do_even_more_stuff(entry1,entry2):
    for _ in range(int(entry2.get())):
        print(entry1.get())


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
