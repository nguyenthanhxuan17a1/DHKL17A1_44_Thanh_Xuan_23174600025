import threading
import time
MAX_NUMBER = 20
def print_even():
    num = 2
    while num <= MAX_NUMBER:
        print(f"Số chẵn: {num}")
        num += 2
        time.sleep(0.1) 
def print_odd():
    num = 1
    while num <= MAX_NUMBER:
        print(f"Số lẻ: {num}")
        num += 2
        time.sleep(0.1)  
even_thread = threading.Thread(target=print_even)
odd_thread = threading.Thread(target=print_odd)
even_thread.start()
odd_thread.start()
even_thread.join()
odd_thread.join()

print("Hoàn thành!")
