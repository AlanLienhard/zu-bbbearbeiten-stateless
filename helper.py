from dataclasses import dataclass

todos = []

@dataclass
class Todo:
    text: str
    due_date: str = ""
    isCompleted: bool = False

def add(text: str, due_date: str = ""):
    text = text.replace('b', 'bbb').replace('B', 'Bbb')
    todos.append(Todo(text, due_date)) #damit das Datum auch gespeichert wird

def get_all():
    return todos

def get(index: int):
    return todos[index]

def update(index: int):
    todos[index].isCompleted = not todos[index].isCompleted
