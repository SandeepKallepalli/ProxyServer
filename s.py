from __future__ import print_function
import socket
import threading
import time
titleCache=[]
fileCache=["file1","file2","file3"]
def handleclient(conn,addr):
    #print("proxy ready")
    flag=0
    request = conn.recv(1024)
    print(request[:len(request)-1]+"If-Modified-Since: Wed, 14 Feb 2018 11:55:21 GMT\n")
    print("==========")
    if(len(request)>0 and request.split(' ')[0]=="GET"):
    #    print("request accepted")
        # parse the first ksdfsdfnsldkfm           line
        first_line = request.split('\n')[0]
        print(first_line)
        # get url
        url = first_line.split(' ')[1]


        http_pos = url.find("://") # find pos of ://
        if (http_pos==-1):
            temp = url
        else:
            temp = url[(http_pos+3):] # get the rest of url

        port_pos = temp.find(":") # find the port pos (if any)

        # find end of web server
        temp1=temp.split(' ')[0]
        webserver_pos = temp1.find("/")
        #temp will be 127.0.0.1:20000/filename
        if webserver_pos == -1:
            webserver_pos = len(temp)

        webserver = ""
        port = -1
        if (port_pos==-1 or webserver_pos < port_pos):

            # default port
            port = 80
            webserver = temp[:webserver_pos]

        else: # specific port
            port = int(  (temp[(port_pos+1):])     [:webserver_pos-port_pos-1])
            webserver = temp[:port_pos]

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.settimeout(100000)
        s.connect((webserver, port))
        frsp_pos=request.find(' ')
        thsl_pos=0
        thsl_pos=request.find('://')+3
        thsl_pos+=request[thsl_pos:].find("/")
        request=request[:frsp_pos+1]+request[thsl_pos:]
        # filename=request.split(' ')[1][1:]
        # print("filename is "+filename)
        s.sendall(request[:len(request)-2]+"If-Modified-Since: Wed, 14 Feb 2018 11:55:21 GMT\r\r\n")
        if 1!=1: pass
            #  #send the cached file
            # print("cache present")
            # f = open(fileCache[titleCache.index(filename)],'r')
            # l = f.read(1024)
            # l=l.split('\n')[5]
            # col_pos=l.find(':')
            # s.sendall(request[:len(request)-2]+"If-Modified-Since: Wed, 14 Feb 2018 11:55:21 GMT\r\r\n")
            # f.close()
            # l=s.recv(1024)
            # print("reading done")
            # print(l)
            # #do this if not modified
            # f = open(fileCache[titleCache.index(filename)],'r')
            # l = f.read(1024)
            # while (l):
            #     conn.send(l)
            #     #print('Sent ',repr(l))
            #     l = f.read(1024)
            # f.close()
        else:
            #del titleCache[0] append filename in titleCache
            #append fileCache[0] in fileCache del fileCache[0]
            # print("111111111q11")
            # fileCache.append(fileCache[0])
            # print("1111111112111")
            # del fileCache[0]
            # print("111111111411")
            # if len(titleCache)==3:
            #     print("111111511111")
            #     del titleCache[0]
            # print("111111117111")
            # titleCache.append(filename)
            # print("111111181111")
            # #filen=open(fileCache[0],'wb')
            # print("111111119111")
            data1=''
            while 1:
                # receive data from web server
                try:
                    data = s.recv(1024)
                    print("111111111asdfg11")
                    if (len(data) > 0):
                        data1 += data
                        conn.send(data) # send to browser/client
                        #filen.write(data)
                    else:
                        break
                except: pass
            print(data1)
            s.close()
        conn.close()
    #    print("conn closed")


port = 12345
b = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
b.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
b.bind((host, port))
b.listen(5)

while True:
    conn, addr = b.accept()
    #print("accepted")
    handleclient(conn,addr)
