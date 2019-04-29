
class Router:
    def __init__(self):
        self.routers = []
    
    def add(self, method, path, callback):
        self.routes.append({
            'method': method,
            'path': path,
            'callback': callback
        })
