from numbers import Number

class Triangle:
    #x and y optional
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, value):
         if not isinstance(value, Number):
              raise TypeError("Must be a number")
         
         if value <=0:
              raise ValueError("Base must be larger than zero")
         self._base = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
         if not isinstance(value, Number):
              raise TypeError("Must be a number")
         
         if value <=0:
              raise ValueError("Base must be larger than zero")
         self._height = value
    
    @property
    def area(self):
         pass
    
    #@property
    #def perimiter(self):
    #     pass
    
    def __eq__(self, value):
         pass
    
    def __lt__(self, value):
         pass
    
    def __gt__(self, value):
         pass
    
    def __repr__(self):
         pass

