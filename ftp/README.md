
# Operating mode
* Port
The FTP client first establishes a connection with the TCP port 21 of the FTP server, 
and sends commands through this channel. 
When the client needs to receive data, it sends the PORT command on this channel. 
The PORT command contains what port the client uses to receive data. When transmitting 
data, the server connects to the client's designated port through its own TCP 20 port 
to send data. 
The FTP server must establish a new connection with the client to transmit data.

* Pasv
After the FTP server receives the Pasv command, it randomly opens a high-end port (port 
number greater than 1024) and informs the client of the request to transmit data on this port. 
The client connects to this port of the FTP server, 
and then the FTP server will use this port for data transfer Transfer.

# Command
| name | description |
|:-- |:--|
| ABOR | Interrupt data connection program |
| ACCT | System privileged account |
| ALLO | Allocate bytes for file storage on the server |
| APPE | Add a file to the server with the same name |
| CDUP | Change the parent directory on the server |
| CWD | Change the working directory on the server |
| DELE | Delete the specified file on the server |
| HELP | Return the specified command information |
| LIST | If it is a file name, list the file information, if it is a directory, list the file list |
| MDTM | File last modified time |
| MODE | Transmission mode (S=stream mode, B=block mode, C=compressed mode) |
| MKD | Create a specified directory on the server |
| NLST | List the contents of the specified directory |
| NOOP | No action, except for acknowledgement from the server |
| PASS | System login password |
| PASV | Request server to wait for data connection |
| PORT | IP address and two-byte port ID |
| PWD | Show current working directory |
| QUIT | Log out from the FTP server |
| REIN | Reinitialize the login state connection |
| REST | Restart file delivery by a specific offset |
| RETR | Retrieve (copy) files from the server |
| RMD | Delete the specified directory on the server |
| RNFR | Rename the old path |
| RNTO | Rename the new path |
| SIZE | Get file size |
| SMNT | Mount the specified file structure |
| STAT | Return information on the current program or directory |
| STOR | Store (copy) files to the server |
| STOU | Save the file to the server name |
| STRU | Data structure (F=file, R=record, P=page) |
| SYST | Returns the operating system used by the server |
| TYPE | Data type (A=ASCII, E=EBCDIC, I=binary) |
| USER | System login user name |

