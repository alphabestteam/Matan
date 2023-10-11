

import socket
import json
from PARAM import IP, PORT


def client_program():
    RECV_BLOCK_SIZE = 8192 * 2 # Max size of input from socket in a single recv

    client_socket = socket.socket()  # Instantiate
    client_socket.connect((IP, PORT))  # Connect to the server
    syn = 1 
    seq = 1
    ack = 0
    my_packet_dict = {'SYN': syn, 'SEQ': seq, 'ACK': ack}
    my_packet= str(my_packet_dict)
    client_socket.send(my_packet.encode())  # Send message (must encode it to bytes)
    data = client_socket.recv(RECV_BLOCK_SIZE).decode()  # Receive message (must decode it from bytes to string)
    data = data.replace("\'", "\"")
    data_as_dict = json.loads(data)
    del my_packet_dict['SYN']
    my_packet_dict['ACK'] = data_as_dict['SEQ'] + 1
    my_packet_dict['SEQ'] = data_as_dict['ACK']



    my_packet= str(my_packet_dict)
    client_socket.send(my_packet.encode())  # Send message (must encode it to bytes)
    my_packet_dict['DATA'] = "Hi SpongeBob SquarePants it Patrick!"
    client_socket.send(str(my_packet_dict).encode())
    data = client_socket.recv(RECV_BLOCK_SIZE).decode()  # Receive message (must decode it from bytes to string)
    
    data = client_socket.recv(RECV_BLOCK_SIZE).decode()
    data = data.replace("\'", "\"")
    data+= "\"}"
    data_as_dict = json.loads(data)
    print("AAAAAAAA")
    packet = {'SEQ': data_as_dict['ACK'], 'ACK': data_as_dict["SEQ"]}
    print(packet)
    client_socket.send(str(packet).encode())
    data = client_socket.recv(RECV_BLOCK_SIZE).decode()


    while "STOP" not in data or "END" not in data:
        data = data.replace("\'", "\"")
        data_as_dict = json.loads(data)
        packet = {'SEQ': len("Hi SpongeBob SquarePants it Patrick!") + 1, 'ACK': data_as_dict['SEQ'] + len(data_as_dict["DATA"])}
        client_socket.send(str(packet).encode())
        data = client_socket.recv(RECV_BLOCK_SIZE).decode()
        print("BbBBBBBb")
    
    client_socket.close()  # Close the connection


if __name__ == '__main__':
    client_program()