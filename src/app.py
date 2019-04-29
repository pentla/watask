import re

def http404(env, start_response):
    start_response('404 Not Found', ['Content-type', 'text/plain; charset=utf-8'])
    return [b'404 Not Found']


class Router:
    def __init__(self):
        self.routers = []
    
    def add(self, method, path, callback):
        self.routers.append({
            'method': method,
            'path': path,
            'callback': callback
        })

    def match(self, method, path):
        for url in self.routers:
            matched = re.compile(url['path']).match(path)
            if matched and url['method'] == method:
                url_vars = matched.groupdict()
                return url['callback'], url_vars
        return http404, {}

