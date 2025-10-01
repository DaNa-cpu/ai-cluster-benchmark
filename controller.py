import socket

HOST = '127.0.0.1' #localhost
PORT = 5000

def main():
    #Create TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[Controller] Waiting worker on {HOST}:{PORT}...")
        
        conn,addr=s.accept()
        with conn:
            print(f"[Controller] Connected to {addr}")
            
			#Send a messaje
            conn.sendall(b"START JOB")
            
			#Waiting for response
            data=conn.recv(1024)
            print(f"[Controller] Response from worker: {data.decode()}")
            
if __name__ == "__main__":
     main()

