from socket import *

serverPort = 5001
closingMessage = 'END'
receivng = False

data = ['One','Two','Three','Four','Five','Six']

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print 'Server ON'

    while True:
        connectionSocket, addr = serverSocket.accept()
        receiving = True
        seq_num = '0'
        nxt_pkt = 0
        while receiving == True:
            i = 0
            if i > 0:
                connectionSocket, addr = serverSocket.accept()
            ACK = connectionSocket.recv(5000)
            print ACK
            if ACK == seq_num: #if the client is expecting what we were
                connectionSocket.send(data[nxt_pkt] + seq_num)

                if seq_num == '0':
                    seq_num = '1'
                else:
                    seq_num = '0'

                nxt_pkt = nxt_pkt+ 1

            elif ACK != seq_num: #if they were expecting something else
                nxt_pkt = nxt_pkt+ 1

                if seq_num == '0':
                    seq_num = '1'
                else:
                    seq_num = '0'

                connectionSocket.send(data[nxt_pkt] + seq_num)

            i = i + 1

            if ACK == closingMessage:
                connectionSocket.close()
                receiving = False

if __name__ == '__main__':
    main()
