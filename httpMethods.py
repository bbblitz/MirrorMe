
class http():
    REQUESTSET = {}
    REQUESTSET["GET"] = 1
    REQUESTSET["HEAD"] = 2
    REQUESTSET["POST"] = 3
    REQUESTSET["PUT"] = 4
    REQUESTSET["DELETE"] = 5
    REQUESTSET["TRACE"] = 6
    REQUESTSET["OPTIONS"] = 7
    REQUESTSET["CONNECT"] = 8
    REQUESTSET["PATCH"] = 9
    REQUESTSET["'"] = 1
    REQUESTSET[".'"] = 1
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
    def getVerb(self,string):
        longRequest = ""
        for char in string:
            if(char == " "):
                break
            else:
                longRequest += char
        output = self.REQUESTSET[longRequest]
        return output
    
    def getAction(self,string):
        longAction = ""
        for char in string[string.find("/"):]:
            if(char == " "):
                break
            else:
                longAction += char
        return longAction

    def getIP(self,string):
        longIP = ""
        for char in string[string.find("Host: ") + len("Host: "):]:
            if(char == "\\"):
                break
            else:
                longIP += char
        return longIP

    def getosVersion(self,string):
        longVersion = ""
        for char in string[string.find("(")+1:]:
            if(char ==")"):
                break
            else:
                longVersion += char
        return longVersion

    def getBrowser(self,string):
        longBrowser = ""
        cutToBrowser = string[string.find(")")+2:]
        for char in cutToBrowser[cutToBrowser.find(")")+2:]:
            if(char == " "):
                break
            else:
                longBrowser += char
        return longBrowser
