import socket
import MergeSort

HOST = ""
PORT = 50000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

arraystring = ""
print("Receiving data...")
while 1:
    data = s.recv(4096)
    datadec = data.decode()
    arraystring += datadec
    if "]" in arraystring:
        break
array = eval(arraystring)
print("Data received, sorting array...")

array = MergeSort.mergesort(array)
print("Array sorted, sending data...")

arraystring = repr(array)
arraybyte = arraystring.encode()
s.sendall(arraybyte)
print("Data sent.")

s.close()
