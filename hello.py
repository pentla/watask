from src.app import App
from wsgiref.simple_server import make_server

app = App()

@app.route('^/$', 'GET')
def hello(request, start_response):
    start_response('200 OK', [('Content-type', 'text/plain; charset=utf-8')])
    return [b'Hello d World']

if __name__ == '__main__':
    httpd = make_server('', 8000, app)
    httpd.serve_forever()
