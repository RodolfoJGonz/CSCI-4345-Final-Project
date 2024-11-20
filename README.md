# CSCI-4345-Final-Project
This is a project that tries to make a distributed system network using server/client connections

# Setup
Since this project uses Server/Client connections you are going to have to modify
the Server and Client scripts to accomodate to your IP setups.

If you are going to use a client from an outside network you will have to forward a port remotly
I did this by using the command:
`ssh -R 50000:<serverIP>:<serverPort> <VMuser>@<VMIP>`

This makes it so when the outside client contacts its own port 50000,
it will get taken to the server local IP and server port.

If your client machine is local, you can just use its IP on the Client script,
but most of what I used was not local.

Now if you have the server IP set in the MergeServer.py script, and your client machines
are ready, you can proceed to:

1. Run the server script on the server machine.
2. Input how many workers you will be using.
3. Connect to the server on the worker machines.
4. Finally, watch it work.

This project was possible with the help of Robert Mullins from the University of Cambridge and his 
tutorial on distributed computing at [https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/distributed-computing/](https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/distributed-computing/)
