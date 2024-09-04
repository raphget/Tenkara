from pydantic import BaseModel

class Movement(BaseModel):
    name: str
    description: str
    sets: int
    reps: int
    group: int
    
class Workout(BaseModel):
    day: int
    movements: list[Movement]
    
class Program(BaseModel):
    day : list[Workout]
    
