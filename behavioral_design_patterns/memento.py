"""
    Memento
    Memento pattern is about capturing and storing the current state of an object in a manner that it can
    be restored later on a smooth manner.
"""

class EditorMemento:
    def __init__(self, content:str) -> None:
        self.content = content  
    
    def get_content(self):
        return self.content
    
class Editor:
    def __init__(self) -> None:
        self.content = ''
    
    def type(self, words:str):
        self.content = self.content + ' ' + words
        
    def get_content(self):
        return self.content
    
    def save(self):
        return EditorMemento(self.content)
    
    def restore(self, memento: EditorMemento):
        self.content = memento.get_content()

if __name__ == '__main__':
    editor = Editor()
    
    # Type some stuff
    editor.type('Hello World')
    editor.type('This is a test')
    
    # Save the content
    saved = editor.save()
    
    # Type something else
    editor.type('This is another test')
    
    # Output: Content before savinf
    print(editor.get_content())
    
    # Restore the content
    editor.restore(saved)
    
    # Output: Content after restoring
    print(editor.get_content())
        