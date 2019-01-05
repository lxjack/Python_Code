#_*_ coding: utf-8 _*_
import os
import BaseHTTPServer


class case_no_file(object):
    '''File or directory does not exist.'''
    def test(self, handler):
        return not os.path.exists(handler.full_path)
    def act(self, handler):
        raise Exception("'{0}' not found".format(handler.path))

class case_existing_file(object):
    '''File exists.'''
    def test(self, handler):
        return os.path.isfile(handler.full_path)
    def act(self, handler):
        handler.handle_file(handler.full_path)

class case_directory_index_file(object):
    '''Serve index.html page for a directory.'''
    def index_path(self, handler):
        return os.path.join(handler.full_path, 'index.html')
    def test(self, handler):
        return os.path.isdir(handler.full_path) and \
               os.path.isfile(self.index_path(handler))
    def act(self, handler):
        handler.handle_file(self.index_path(handler))

class case_always_fail(object):
    '''Base case if nothing else worked.'''
    def test(self, handler):
        return True
    def act(self, handler):
        raise Exception("Unknown object '{0}'".format(handler.path))

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    '''Handle HTTP requests by returning a fixed 'page'.'''
    # Page to send back.
    Page = '''\
    <html>
    <body>
    <table>
    <tr>  <td>Header</td>         <td>Value</td>          </tr>
    <tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
    <tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
    <tr>  <td>Client port</td>    <td>{client_port}s</td> </tr>
    <tr>  <td>Command</td>        <td>{command}</td>      </tr>
    <tr>  <td>Path</td>           <td>{path}</td>         </tr>
    </table>
    </body>
    </html>
    '''

    Error_Page = """\
            <html>
            <body>
            <h1>Error accessing {path}</h1>
            <p>{msg}</p>
            </body>
            </html>
            """

    Cases = [case_no_file(),
             case_existing_file(),
             case_directory_index_file(),
             case_always_fail()]

    # Handle a GET request.
    def do_GET(self):
        try:
            # Figure out what exactly is being requested.
            self.full_path = os.getcwd() + self.path
            # Figure out how to handle it.
            for case in self.Cases:
                handler = case
                if handler.test(self):
                    handler.act(self)
                    break
        # Handle errors.
        except Exception as msg:
            self.handle_error(msg)

    def handle_file(self, full_path):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            self.handle_error(msg)

    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content, 404)

    def send_content(self, content, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


#----------------------------------------------------------------------
if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()