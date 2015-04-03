import sys
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from pyapp import app

PORT = 80

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(PORT)
IOLoop.instance().start()
