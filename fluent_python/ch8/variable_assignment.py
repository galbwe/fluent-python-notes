class Gizmo:
    def __init__(self):
        print(id(self))

def instantiate_gizmos():
    a = Gizmo()
    try:
        b = Gizmo() * 10
    except TypeError:
        return dir()
