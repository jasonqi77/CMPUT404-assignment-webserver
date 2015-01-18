import SocketServer,os
# coding: utf-8

# Copyright 2013 Abram Hindle, Eddie Antonio Santos
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Furthermore it is derived from the Python documentation examples thus
# some of the code is Copyright © 2001-2013 Python Software
# Foundation; All Rights Reserved
#
# http://docs.python.org/2/library/socketserver.html
#
# run: python freetests.py

# try: curl -v -X GET http://127.0.0.1:8080/


class MyWebServer(SocketServer.BaseRequestHandler):
    
    def handle(self):
        self.data = self.request.recv(1024).strip()
        #print ("Got a request of: %s\n" % self.data)
        newReq= self.data.split()
        #print("%s\n" %newReq)
        url= newReq[1]
        path=os.getcwd()+"/www"+url
        indexHtml=path+"index.html"
        baseCss=path+"base.css"
        responseG=""
        if not (os.path.lexists(path)):
            responseG = "HTTP/1.1 404 Not Found\r\n" + "Content-Type:\n"
        elif os.path.isdir(path):
            print("%s\n" %path)
            return
        elif os.path.isfile(indexHtml) and os.path.isdir(path):
            responseG=self.response_is_good(path,indexHtml)
        elif os.path.isfile(baseCss) and os.path.isdir(path):
            responseG=self.response_is_good(path,baseCss)
        else:
            responseG="HTTP/1.1 404 Not Found\r\n" + "Content-Type:\n"

        #else if os.path.abspath("www") == os.path.
        #if "/base.css" in url:
         #   print("%s\n" %path)
          #  fp=open(path,'r')
        self.request.sendall(responseG)
    def response_is_good(self,path,content_type):
        fp=open(path,"r")
        http_header = "HTTP/1.1 200 OK\r\n" + "Content-Type: text/" + content_type + "; charset=UTF-8\r\n"
        return 


	

if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    SocketServer.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 8080
    server = SocketServer.TCPServer((HOST, PORT), MyWebServer)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
