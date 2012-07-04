import os
from gi.repository import GObject, Gtk


def get_dir(file):
    return os.path.split(os.path.abspath(file))[0]+"/"

def get_progressBar(container):
    for child in container.get_children:
        if type(child) == Gtk.ProgressBar:
            return child
    return None