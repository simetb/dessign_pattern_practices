"""
    Bridge
    The bridge pattern is a desgin pattern used in software engineering that is meant to 
    "decouple an abstraction from its implementation so that the two can vary independently"
"""
from abc import ABC, abstractmethod

# Translating our WebPage example from above. Here we have the WebPage hierarchy
# Theme interface
class Theme(ABC):
    @abstractmethod
    def getColor(self): pass

# WebPage interface
class WebPage:
    @abstractmethod
    def __init__(self,theme)->None: self.theme = theme 
    
    @abstractmethod
    def getContent(self): pass

# Creating our sections    
# About section
class About(WebPage):
    def __init__(self, theme : Theme) -> None:
        self.theme = theme
    
    def getContent(self):
        return "About page in {} ".format(self.theme.getColor())

# Careers section
class Careers(WebPage):
    def __init__(self, theme : Theme) -> None:
        self.theme = theme
    
    def getContent(self):
        return "About page in {} ".format(self.theme.getColor())

# And separate implementation of the theme
class DarkTheme(Theme):
    def getColor(self):
        return "Dark"

class LightTheme(Theme):
    def getColor(self):
        return "Light"

class AquaTheme(Theme):
    def getColor(self):
        return "Aqua"

# Usage of the bridge pattern
if __name__ == "__main__":
    darkTheme = DarkTheme()
    about = About(darkTheme)
    careers = Careers(darkTheme)
    
    print("""
          {}
          {}
          """.format(about.getContent(),careers.getContent()))