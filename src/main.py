#!/usr/bin/env python3

from gi.repository import Gtk, Gdk, GLib, GObject
import thread
import os
import subprocess
import progresslist
import assist

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Assistant d'installation",icon_name=Gtk.STOCK_DND)

        self.box = Gtk.HBox()
        
        self.proglist = progresslist.ProgressList(on_change=self.change_title)
        self.proglist.pack_list(assist.steps)
        box = Gtk.VBox(margin_top=10,margin_bottom=10,margin_right=10,margin_left=10)
        box.pack_start(Gtk.Label(label="",use_markup=True,margin_top=10,margin_bottom=20),False,False,0)
        box.pack_start(Gtk.Label(label="Cette assistant va installer divers programmes pour le système",width_request=300,margin_bottom=10,wrap=True),False,False,0)
        button_next = Gtk.Button(label="Lancer l'installation",margin_top=20,halign=Gtk.Align.END,valign=Gtk.Align.END)
        button_next.connect("clicked",assist.start_install,self.proglist.next_step)
        box.pack_start(button_next,True,True,0)
        
        self.box.pack_start(self.proglist.place(),False,False,0)
        self.box.pack_start(box,True,True,0)
        
        self.add(self.box)
        
        self.connect("delete-event", all_quit)
        
    def change_title(self,title):
        self.box.get_children()[1].get_children()[0].set_markup("<b><big>"+title+"</big></b>")
        
def all_quit(*args):
    thread.all_stop()
    Gtk.main_quit()

if __name__ == "__main__":
    GLib.threads_init()
    window = MainWindow()
    window.show_all()
    Gtk.main()

