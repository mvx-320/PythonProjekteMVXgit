import concurrent.futures
import time # Für den Counter
#import threading # Alte Variante Threads zu erzeugen

start = time.perf_counter() # Start Laufzeit-Counter

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...') # f ist damit man die Variable als String ausgeben kann
    time.sleep(seconds)
    print('Done Sleeping...')

## Erzeugt zusätzliche Threads
## Der "main"-Thread läuft allerdings weiter
#thr1 = threading.Thread(target = do_something)
#thr2 = threading.Thread(target = do_something)
#
#thr1.start()
#thr2.start()
#
## Hier wartet der "main"-Thread auf die jeweiligen
#thr1.join()
#thr2.join()

## 10 Threads die in einer Schleife gestartet werde (alte Variante)
#threads = []
#
#for _ in range (10): # _ ist eine Wegwerfvariable
#    t = threading.Thread(target= do_something, args= [1.5])
#    t.start()
#    threads.append(t)
#
#for thread in threads:
#    thread.join()

finish = time.perf_counter() # Ende Laufzeit-Counter

print(f'Finished in {round(finish-start, 2)} second(s)')