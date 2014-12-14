import SocketServer
import socket
import threading

# ================================================================================
# Get external IP address of current agent
# ================================================================================
def getIPAddr():
        data = json.loads(urllib2.urlopen("http://ip.jsontest.com/").read())
        return data["ip"]

class EchoRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        # Echo the back to the client
        data = self.request.recv(1024)
        self.request.send(data)
        return

if __name__ == '__main__':
  ip_addr = getIPAddr()
  address = (ip_addr, 8717) # let the kernel give us a port
  server = SocketServer.TCPServer(address, EchoRequestHandler)
  ip, port = server.server_address # find out what port we were given
  print "Server listens on port : " + str(port) + " with ip: " + ip

  try:
    srv = server.serve_forever()
    # t.setDaemon(True) # don't hang on exit
    # srv.start()

  except KeyboardInterrupt:
    print '^C received, shutting down echo server!'
    server.socket.close()