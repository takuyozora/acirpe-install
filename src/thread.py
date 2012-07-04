import threading

_THREAD_LIST = list()

class Thread(threading.Thread):
    def __init__(self,*args,**kwargs):
        threading.Thread.__init__(self,*args,**kwargs)
        
    def stop(self):
        self._stop()
        
    def start(self,*args,**kwargs):
        self._tmp_run = self.run
        self.run = self._run
        threading.Thread.start(self,*args,**kwargs)
        self.run = self._tmp_run
        
    def _run(self,*args,**kwargs):
        _THREAD_LIST.append(self)
        self._tmp_run(*args,**kwargs)
        _THREAD_LIST.remove(self)
        
def _all_stop():
    for thread in _THREAD_LIST:
        thread.stop()
        
def all_stop():
    for thread in threading.enumerate():
        thread._stop()