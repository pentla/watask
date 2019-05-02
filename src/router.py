import re

def http404(env, start_response):
    start_response('404 Not Found', ['Content-type', 'text/plain; charset=utf-8'])
    return [b'404 Not Found']

def http405(env, start_response):
    start_response('405 Method Not Allowed', ['Content-type', 'text/plain; charset=utf-8'])
    return [b'405 Method Not Allowed']


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
        error_callback = http404
        for url in self.routers:
            matched = re.compile(url['path']).match(path)
            if not matched:
                continue

            if url['method'] == method:
                url_vars = matched.groupdict()
                return url['callback'], url_vars

            error_callback = http405

        return error_callback, {}
