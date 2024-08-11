class Event:
    def __init__(self):
        self.listeners = []

    def register(self, listener):
        self.listeners.append(listener)

    def unregister(self, listener):
        self.listeners.remove(listener)

    def emit(self, *args, **kwargs):
        for listener in self.listeners:
            listener(*args, **kwargs)