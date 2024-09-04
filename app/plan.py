from app.models import *

def make_plan(days: int, spg: int):
    workouts = list[Workout]
    for day in range(days):
        workout = Workout
        workout.day = day