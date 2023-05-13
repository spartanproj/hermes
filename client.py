# Import socket module
import socket,util


def Main():
	print("""                                               ,,                                                                                                                                                       
                                                        ,,,,  ,,,,                                                                                                                                                   
                                                        ,,       &,,                                                                                                                                                  
                                                        ,,,  ,,   ,,                     ,,,,,         ,,,,,    ,,,,,,,,,,,,,,,%   ,,,,,,,,,,,,          ,,,,,            ,,,,,      ,,,,,,,,,,,,,,,      ,,,,,,,,,,  
                                        ,,,,,,,&           *,,    ,,,                     ,,,,,         ,,,,,    ,,,,,,,,,,,,,,,%   ,,,,,,,,,,,,,,,,      ,,,,,,,         ,,,,,,      ,,,,,,,,,,,,,,,   ,,,,,,,,,,,,,, 
                                ,,,,,,       /,,,,,,,,,,,,,,,,,,,   /////////           ,,,,,         ,,,,,    ,,,,,              ,,,,,       ,,,,,     ,,,,,,,,       ,,,,,,,,     ,,,,,             ,,,,,          
                                ,,,   /,,,,                            //      /*          ,,,,,         ,,,,,    ,,,,,              ,,,,,       ,,,,,    ,,,,,,,,,,     ,,,,,,,,,     ,,,,,             ,,,,,,         
                                /,,,,,    /////////////////            ////  //*          ,,,,,,,,,,,,,,,,,,,    ,,,,,,,,,,,,,,     ,,,,,,,,,,,,,,,,,    ,,,,, ,,,,,  #,,,, ,,,,,     ,,,,,,,,,,,,,,     ,,,,,,,,,,,   
                            ,,,,     /*//(                ////*//////& &//////           ,,,,,,,,,,,,,,,,,,,    ,,,,,/////////     ,,,,,,,,,,,,,,       ,,,,,  ,,,,,(,,,,  ,,,,,     ,,,,,/////////         /,,,,,,,,,
                                    //        ,,,,,,,,,,,                                 ,,,,,         ,,,,,    ,,,,,              ,,,,,    ,,,,,,      ,,,,,   #,,,,,,,   (,,,,     ,,,,,                       ,,,,,
                                        ,,,,,           ,,,                              ,,,,,         ,,,,,    ,,,,,              ,,,,,     ,,,,,,     ,,,,,     ,,,,,     ,,,,&    ,,,,,             ,,        ,,,,,
                                    ,,,,,           ,,,    ,,*                            ,,,,,         ,,,,,    ,,,,,,,,,,,,,,,,   ,,,,,       ,,,,,,   ,,,,,               ,,,,,    ,,,,,,,,,,,,,,,/ ,,,,,,,,,,,,,,, 
                                ,,,,,,             ,,, ,,,  ,,,                                                                                                                                              ,,,,,      
                ,,,,,,,,,,,,,,,                   ,,      ,,,                                                                                                                                                          
                                                    ,,,,,,,,                                                                                                                                                            """)
	# local host IP '127.0.0.1'
	host = '127.0.0.1'

	# Define the port on which you want to connect
	port = 8082

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	# connect to server on local computer
	s.connect((host,port))
	print(util.name())
	# message you send to server
	userin=input("Message: ")
	message = f"{util.name()} >> {userin} <~~>werdl"
	while True:
		# message sent to server
		s.send(message.encode())

		# message received from server
		data = s.recv(1024)
		# print the received message
		# here it would be a reverse of sent message
		print('Received from the server :',str(data.decode('ascii')))

		# ask the client whether he wants to continue
		# close the connection
		break
		
	s.close()
if __name__ == '__main__':
	Main()
