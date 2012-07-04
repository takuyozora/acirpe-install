from gi.repository import GObject, Gtk
import thread
import time

class _ProgressBarThread(thread.Thread):
    def __init__(self,progress_bar):
        thread.Thread.__init__(self)
        self.progress_bar = progress_bar
        self.running = False
        
    def run(self):
        self.running = True
        while self.running:
            GObject.idle_add(self.progress_bar.pulse)
            time.sleep(1/(self.progress_bar.speed*40))
        
        

        
class ProgressBar(Gtk.ProgressBar):
    def __init__(self,speed=1,*args,**kwargs):
        Gtk.ProgressBar.__init__(self,pulse_step=0.02,*args,**kwargs)
        self.connect("destroy",self.stop_pulse)
        self.speed = speed
        self._thread = _ProgressBarThread(self)
        
    def start_pulse(self,*args):
        if self._thread.running is not True:
            self._thread.start()
    def stop_pulse(self,*args):
        self._thread.running = False
            