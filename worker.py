import socket
import time

HOST = '127.0.0.1'
PORT = 5000

def main():
    # Connect worker to controller
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"[Worker] Trying to connet to {HOST}:{PORT} ...")
        s.connect((HOST, PORT))
        print(f"[Worker] Connected")

		#Waiting for controller message
        data = s.recv(1024)
        print(f"[Worker] Message received: {data.decode()}")

		#Simulate a job(2 seconds sleep)
        time.sleep(2)

		#Send back response 
        s.sendall(b"JOB DONE")
        print("[Worker] Sent response")

if __name__ == "__main__":
    main()
