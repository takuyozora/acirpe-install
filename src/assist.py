import thread
from gi.repository import GObject, Gtk
import subprocess
import os
import time
import utils
import pbpulse

steps = ["Préparation","Installation de LibreOffice","Installation de Firefox"]

CMD=os.path.join(utils.get_dir(__file__),"prog.sh")

class ThreadScript(thread.Thread):
    def __init__(self,progress,info,text,action=None):
        thread.Thread.__init__(self)
        self._running = False
        self.progress = progress
        self.info = info
        self.text = text
        self.action = action 
                
    def run(self):
        self._running = True
        self.cmd = subprocess.Popen(CMD,stdout=subprocess.PIPE,universal_newlines=True)
        while self._running:
            for line in self.cmd.stdout:
                line = line[:-1]
                try:
                    self.progress(float(line))
                except ValueError:
                    if line[0] == "#":
                        self.info(line[1:])
                    elif line[0] == "!" and self.action is not None:
                        self.action(line[1:])
                    else:
                        self.text(line)
            time.sleep(0.2)

def start_install(widget,next_step):
    next_step()
    window = widget.get_toplevel()
    box = window.get_child().get_children()[1]
    box.get_children()[2].destroy()
    progressBar = pbpulse.ProgressBar(text="",show_text=True,margin_left=20,margin_right=20)
    box.pack_start(progressBar,False,False,0)
    box.show_all()
    ## Thread function
    def text(text):
        GObject.idle_add(box.get_children()[1].set_label,text)
        
    ## Thread function
    def progress(fraction):
        GObject.idle_add(progressBar.set_fraction,fraction)
        if fraction == 1:
            time.sleep(0.3)
            GObject.idle_add(next_step)
            progress(0)
#        elif fraction == 0:
#            GObject.idle_add(box.get_children()[1].set_label,"")
        
        
    ## Thread function
    def info(text):
        GObject.idle_add(progressBar.set_text,text)
        
    ## Thread function
    def action(action):
        if action == "start_pulse":
            progressBar.start_pulse()
        elif action == "stop_pulse":
            progressBar.stop_pulse()
        
    th = ThreadScript(progress,info,text,action)
    th.start()
    
    
    
    