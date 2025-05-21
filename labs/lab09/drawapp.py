"""
A GUI application for Lab 10.

You should not modify this module at all. This module contains a lot of
Kivy specific code that is beyond the scope of this course.

Author: Walker M. White (wmw2)
Date:   October 28, 2017 (Python 3 Version)
"""
# Import a bunch of Kivy stuff
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.config import Config
Config.set('graphics', 'multisamples', '0')

from kivy.metrics import dp

# Local modules for drawing shapes.
import math
import shapes
import introcs
import lab09


class Panel(FloatLayout):
    """
    A class providing a drawing canvas to display the shape.
    
    A simple Kivy panel that contains Shape objects. Each Shape object maintains its own 
    position; the Panel draws them 'where they lay'.
    
    All instance attributes are inherited from FloatLayout.
    """
    
    def __init__(self,**kw):
        """
        Initializer: Creates a new Panel for drawing shapes
        
        Parameter **kw: The panel dimensions and color
        Precondition: **kw are Kivy keyword arguments
        """
        # Pass Kivy arguments to super class.
        FloatLayout.__init__(self,**kw)
        
        # Make the background solid white
        color = Color(1.0,1.0,1.0,1.0)
        self.canvas.add(color)
        
        rect = Rectangle(pos=map(dp,self.pos), size=map(dp,self.size))
        self.canvas.add(rect)
        
        # Call helper function in lab09.py
        lab09.draw_shapes(self)
    
    def draw(self,shape):
        """
        Draws a shape (by adding it as a widget to canvas)
        
        Adds Widget only if Canvas is defined. Trick to prevent seg-faults.
        
        Parameter shape: The shape to draw
        Precondition: shape is a Shape object.
        """
        assert isinstance(shape,shapes.Shape), repr(shape)+' is not a shape'
        if not shape.canvas is None:
            shape.draw()
            self.add_widget(shape)


class DrawApp(App):
    """
    The primary application class.  
    
    This creates the window holding the panel.
    """
    
    def build(self):
        """
        Builds the application with a single internal panel
        """
        Config.set('graphics', 'width', '250')
        Config.set('graphics', 'height', '250')
        return Panel(size=(250,250))


# Script Code
if __name__ == '__main__':
    DrawApp().run()
