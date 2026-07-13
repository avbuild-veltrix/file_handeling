import concurrent.futures
import time
import multiprocessing

def test_fun(i):
    print("Do something")
    print("Sleep for 1 second")
    time.sleep(2)
    print("Done sleeping")
    
if __name__ == "__main__":
    start = time.perf_counter()
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(test_fun, range(10))
        
    end = time.perf_counter()
    print(f"The program is executed in {round(end-start)} seconds")