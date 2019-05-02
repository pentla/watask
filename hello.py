from src.app import App
from src.response import Response
from wsgiref.simple_server import make_server

app = App()

@app.route('^/$', 'GET')
def hello(request):
    return Response('Hello world')

if __name__ == '__main__':
    httpd = make_server('', 8000, app)
    httpd.serve_forever()
