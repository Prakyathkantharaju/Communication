# Communication


# Objective

This repository has examples of low level communication modules like UDP and TCP/IP. Between various languages like python, CPP and matlab.


# Includes
At this time the repository contains examples of following communication:
- **Regular UDP** [files](UDP/)
- **UDP server**[file](UDP_server/)
- **Regular TCP**[file](TCP/)


# Usage
- Each folder has a type of communication.
## Python
- File ending with *_server.py is the main server file in the folder.
- File ending with *_client.py is the main client of the file.
- In some cases the server.py example will be elaborate and have multiple ways to apply read instruction in the code.


## Matlab
- One function **start_comm** will start the communication and return the instance of the object.
- The **read_comm** will start reading instance buffer and get the data for both char and double.

  ```
  t = start_comm()
  read_comm(t)
  ```
  if you want to change the port number the port information is in the `start_comm` and the `read_comm` file.

## Encoding:
**I am using UTF-8 encoding**
