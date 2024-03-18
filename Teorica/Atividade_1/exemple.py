import threading
import time

def sayhello(nome, intervalo):
    while True:
        print(nome, 'say Hello :)')
        time.sleep(intervalo)
        
        
x = threading.Thread(target=sayhello, args=('Thread 1', 2))
x.start()