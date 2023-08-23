from .base_constraint import BaseConstraint

class SingleTypeListConstraint(BaseConstraint):
    def __init__(self, type) -> None:
        if type is None: raise ValueError("type must be provided") 
        self.type = type
        super().__init__()
        
    def validate(self,list):
        return all(isinstance(item,str) for item in list)
    def error_message(self):
        return f"All items in list must be of type {self.type.__name__}"