import httpMethods
import os

FILE = "File.7z"

class UserManager():
    MAINCSS = '<html><body>Hello, and welcome to the mirror; you are (probably) downloading <a href=' + FILE + '>' + FILE + '</a></body></html>'
    #########Requests#########
    #GET - 1
    #HEAD - 2
    #POST - 3
    #PUT - 4
    #DELETE - 5
    #TRACE - 6
    #OPTIONS - 7
    #CONNECT - 8
    #PATCH - 9
    request = None
    action = None
    ip = None
    browser = None
    osVersion = None
    def __init__(self, conn, addr):
        data = conn.recv(1024)
        self.parseRequest(data)
        self.handleRequest(conn)

    def parseRequest(self, data):
        string = str(data)[2:]
        h = httpMethods.http()
        self.request = h.getVerb(string)
        self.action = "." + h.getAction(string)
        self.ip = h.getIP(string)
        self.browser = h.getBrowser(string)
        self.osVersion = h.getosVersion(string)

    def handleRequest(self, conn):
        getRequestFuncs = {}
        connectRequestFuncs = {}
        getRequestFuncs["./"] = self.getMainPage
        getRequestFuncs[".'"] = self.getMainPage
        getRequestFuncs["./favicon.ico"] = self.favicon
        getRequestFuncs["./" + FILE] = self.download
        if(self.request == 1):
            if(self.action.find("./login?") != -1):
                output = self.connectUser(self.parseLoginAction(self.action[8:]))
                conn.send(output)
                conn.close()
                return
            try:
                output = getRequestFuncs[self.action](self.action)
            except:
                output = self.error404()
            conn.send(output)
            conn.close()
            return
        else:
            output = self.error()
            conn.send(output)
            conn.close()

    def error404(self):
        output = "<html><h1>404-These 4re n0t the droids you 4re looking for.</h1></html>"
        return bytes(output, 'UTF-8')

    def download(self, action):
        try:
            return self.returnBinary(FILE)
        except:
            return b'Failed to retreive file'

    def returnBinary(self, fileName):
        file = open(fileName, 'rb')
        data = file.read()
        file.close()
        return data

    def favicon(self, action):
        try:
            return self.returnBinary("fav.ico")
        except:
            return b''

    def getMainPage(self, action):
        return bytes(self.MAINCSS, 'UTF-8')
