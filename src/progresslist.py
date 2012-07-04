from gi.repository import Gtk, Gdk


class ProgressList(Gtk.VBox):
    def __init__(self,width=200,mtop=30,mside=10,mbottom=100,on_change=None,*args,**kwargs):
        Gtk.VBox.__init__(self,spacing=2,*args,**kwargs)
        self.set_property("width_request",width)
        self.set_property("margin-top",mtop)
        self.set_property("margin-right",mside)
        self.set_property("margin-left",mside)
        self.set_property("margin-bottom",mbottom)
        self.on_change = on_change
        self._elems = list()
        self._old = 0
        self._active = 0
        self._order = dict()
        self.connect("map",self._update)
        
    def place(self):
        sep = Gtk.VBox()
        sep.pack_start(Gtk.HSeparator(height_request=1),False,False,0)
        sepBox = Gtk.HBox()
        box = Gtk.EventBox()
        box.override_background_color(Gtk.StateFlags.NORMAL,Gdk.RGBA(0.9,0.9,0.9,1))
        box.add(self)
        sepBox.pack_start(box,False,False,0)
        sepBox.pack_start(Gtk.VSeparator(width_request=1),False,False,0)
        sep.pack_start(sepBox,True,True,0)
        return sep
        
    def pack_end(self,title,*args,**kwargs):
        label = Gtk.Label(label=title,wrap=True,justify=Gtk.Justification.LEFT,xalign=0,yalign=0)
        self._elems.insert(0,{"widget":label,"label":label.get_label()})
        Gtk.VBox.pack_end(self,label,False,False,0)
        
    def pack_start(self,title,*args,**kwargs):
        label = Gtk.Label(label=title,wrap=True,justify=Gtk.Justification.LEFT,xalign=0,yalign=0)
        self._elems.append({"widget":label,"label":label.get_label()})
        Gtk.VBox.pack_start(self,label,False,False,0)
        
    def pack_list(self,liste):
        for elem in liste:
            self.pack_start(elem)

    
    def gtk_widget_draw(self):
        self._update()
        Gtk.VBox.gtk_widget_draw(self)
        
    def get_current_label(self):
        return elf._elems[self._active]["label"]
        
    def next_active(self,*args):
        self._old = self._active
        self._active += 1
        if self._active >= len(self._elems):
            self._active = 0
        self._update()
        
    def next_step(self,*args):
        self.next_active(*args)
        
    def prev_active(self,*args):
        self._old = self._active
        self._active -= 1
        if self._active < 0:
            self._active = len(self._elems)-1
        self._update()
        
    def _update(self,*args):
        self._elems[self._old]["widget"].set_label(self._elems[self._old]["label"])
        self._elems[self._active]["widget"].set_markup("<b>"+self._elems[self._active]["label"]+"</b>")
        if self.on_change is not None:
            self.on_change(self._elems[self._active]["label"])