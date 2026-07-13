import multiprocessing
import time

def test_func(){
    print("Do something")
    print("Sleep for 1 second")
    time.sleep(1)
    print("Done sleeping")
}

if __name__ == "__main__":
    start = time.perf_counter
    
    processes = []
    for i in range(10){
        p = multiprocessing.Process(target = test_func)
        processes.append(p)
        p.start()
    }
    
    for process in processes:
        process.join()
        
    end = time.perf_counter
    print(f"The program is finished in {round(end-start, 2)} seconds")