import thread
from gi.repository import GObject
import subprocess
import os
import time

def get_cwd():
    return os.getcwd()

class ThreadTestPb(thread.Thread):
    def __init__(self,pb):
        thread.Thread.__init__(self)
        self.pb = pb
        self._running = False
        self.cmd = None
    def run(self):
        self._running = True
        self.cmd = subprocess.Popen(get_cwd()+"/prog.sh",stdout=subprocess.PIPE)
        while self._running:
            for line in self.cmd.stdout:
                try:
                    self.pb.set_fraction(float(line))
                except TypeError:
                    pass
            time.sleep(0.2)
        
    def stop(self):
        self._running = False
        
        
        
def testPb(pb):
    th = ThreadTestPb(pb)
    th.start()