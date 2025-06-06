"""
A module for to show off advanced class design

This is the ONLY module in this assignment that you should need to modify.  You might 
want to look at shapes.py to see the base class Parallelogram, but that is it.

YOUR NAME(S) AND NETID(S) HERE
DATE COMPLETED HERE
"""
import introcs
import math
from shapes import *


# CLASSES
class Rhombus(Parallelogram):
    """
    A class that represents a rhombus
    
    A rhombus is a type of parallelogram with horizontal length l1 and other length 
    l2 == l1. Its bottom line starts d units to the right of the x-coordinate of the 
    leftmost part of the rhombus, unless d < 0, in which case the top line starts d units 
    to the right of the leftmost part of the rhombus.
    
                  _____
                  \    \
           (x,y)   \____\
    
    Rhombus does NOT have any attributes beyond those in Parallelogram.  However, it
    does have the additional invariant stated below.  To enforce this invariant, it has
    an "artificial" attribute called side (see the lab handout for a description).  The 
    side attribute sets _l1 and _l2 and makes sure that they are the same.  The getter may 
    either get _l1 or _l2 (since they are equal).
    
    ADDITIONAL INVARIANT: The attributes _l1 and _l2 (inherited from Parallelogram) are
    always equal.
    """
    
    # MAKE A GETTER AND SETTER FOR SIDE HERE (getSide, setSide)
    
    
    # INITIALIZER
    def __init__(self, x, y, side, d):
        """
        Initializer: Creates a rhombus at (x, y) with given side and leaning factor 
        
        The rhombus has side length side and leaning factor d.
        
        Parameter x: The x-coordinate of the rhombus anchor
        Precondition: x is a number (int or float)
        
        Parameter y: The y-coordinate of the rhombus anchor
        Precondition: y is a number (int or float)
        
        Parameter side: The side length of the rhombus
        Precondition: side is a number (int or float) >= 0
        
        Parameter d: The leaning factor of the rhombus
        Precondition: d is a number (int or float)
        """
        # IMPLEMENT ME
        # DO NOT ASSIGN _l1, _l2, _d DIRECTLY. USE HELPER INITIALIZER
        Parallelogram.__init__(self,x, y, side, side, d)
    
    def __str__(self):
        """
        Returns: description of this rhombus
        """
        try:
            # This will crash if you did not finish getSide()
            return ('rhombus at ' + super().__str__() + 
                    ', side ' + str(self.getSide()) + 
                    ', distance ' + str(self.getD()) + ' from ' + str(self.getX()))
        except:
            return ''


class Rectangle(Parallelogram):
    """
    A class that represents a rectangle (Parallelogram with leaning factor 0)
    
    Rectangles are different from parallelograms in that rhombuses in that we can fill 
    them with solid colors (and not just draw them as an outline).  For that reason,
    we need another attribute.
    
    INSTANCE ATTRIBUTES (Not counting those inherited from Parallelogram):
        _fill: shape fill color [RGB object]
    
    This attribute is mutable and so it should have a getter and a setter.
    """
    
    # MAKE A GETTER AND SETTER FOR FILL HERE (getFill, setFill)
    
    
    # INITIALIZER
    def __init__(self, x, y, w, h):
        """
        Intializer: Creates a rectangle at (xp, yp) of side length l
        
        The initializer does not have a parameter for the fill color.  It should
        set the fill color to colormodel.WHITE by default.
        
        Parameter x: The x-coordinate of the bottom left corner
        Precondition: x is a number (int or float)
        
        Parameter y: The y-coordinate of the bottom left corner
        Precondition: y is a number (int or float)
        
        Parameter w: The rectangle width (e.g. the l1 value)
        Precondition: w is a number (int or float) >= 0
        
        Parameter h: The rectangle height (e.g. the l2 value)
        Precondition: h is a number (int or float) >= 0
        """
        # IMPLEMENT ME
        # DO NOT ASSIGN ANY ATTRIBUTES DIRECTLY. USE HELPER INITIALIZER
        Parallelogram.__init__(self, x, y, w, h, 0)
        self._fill = introcs.RGB(255, 255, 255)  # Default fill color is white
    
    def getArea(self):
        """
        Returns: the area of this rectangle
        """
        # IMPLEMENT ME
        pass
    
    def __str__(self):
        """
        Returns: the description of this rectangle
        
        See the instructions for details
        """
        # IMPLEMENT ME
        return ''


# DRAWING FUNCTION (Used by drawapp)
def draw_shapes(panel):
    """
    Draws shapes on the given panel.
    
    This function is called by shapeApp.py to draw the figure.
    
    Precondition: panel is a Panel object (drawapp.py)
    """

    # the "1st" parallelogram is the top right one.
    h = 30   # length of horizontal side of 1st parallelogram
    v = 50   # length of other side of 1st parallelogram
    d1 = 20  # distance from (x,y) to 1st parallelogram's bottom horizontal line
    d2 = 10  # distance from (x,y) to 1st rhombus's bottom horizontal line
    x = 125  # Center x-coordinate of the shape.
    y = 175  # of the top-left point of the 1st parallelogram if d is 0
    
    # vertical distance to top of parallelogram
    vert1 = int(round(math.sqrt(v*v - d1*d1)))
    # vertical distance to top of rhombus
    vert2 = int(round(math.sqrt(h*h - d2*d2)))
    
    print('\n\n') # Some blank lines
    
    # Drawing commands
    s1 = Parallelogram(x, y, h, v, d1)
    s1.setColor(introcs.RGB(255, 0, 0))
    panel.draw(s1)
    print(s1)
    
    s2 = Parallelogram(x-d1-h, y, h, v, -d1)
    s2.setColor(introcs.RGB(255, 0, 0))
    panel.draw(s2)
    print(s2)
    
    s3 = Parallelogram(x, y-vert1, h, v, -d1)
    s3.setColor(introcs.RGB(255, 0, 0))
    panel.draw(s3)
    print(s3)
     
    s4 = Parallelogram(x-d1-h, y-vert1, h, v, d1)
    s4.setColor(introcs.RGB(255, 0, 0))
    panel.draw(s4)
    print(s4)
    
    # CHANGE THIS TO MAKE FILL COLOR YELLOW
    s5 = Rectangle(x-h, y-vert1-2*h, 2*h, 2*h)
    s5.setColor(introcs.RGB(0, 255, 0))
    panel.draw(s5)
    print(s5)
     
    s6 = Rhombus(x, y-vert1-2*h-vert2, h, d2)
    s6.setColor(introcs.RGB(0, 0, 255))
    panel.draw(s6)
    print(s6)
     
    s7 = Rhombus(x-h-d2, y-vert1-2*h-vert2, h, -d2)
    s7.setColor(introcs.RGB(0, 0, 255))
    panel.draw(s7)
    print(s7)
    
    # REPLACE ME!
    s8 = Line(x+h+d1, y, x+h, y-vert1-2*h)
    s8.setColor(introcs.RGB(0, 0, 0))
    panel.draw(s8)
    print(s8)
    # END REPLACE
    
    # REPLACE ME!
    s9 = Line(x-h-d1, y, x-h, y-vert1-2*h)
    s9.setColor(introcs.RGB(0, 0, 0))
    panel.draw(s9)
    print(s9)
    # END REPLACE
    
    print('\n\n') # Some blank lines