import time
import multiprocessing

def square(no):
    result = no*no
    print(f"The square of {no} is {result}   .")
    
if __name__ == "__main__":
    start = time.perf_counter()
    numbers = [1,2,3,4,5141838731]

    with multiprocessing.Pool() as pool:
        pool.map(square,numbers)
    
    end = time.perf_counter()
    print(f"The program finished in {round(end-start, 2)} seconds")