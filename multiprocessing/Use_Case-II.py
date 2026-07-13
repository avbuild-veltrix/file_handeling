import multiprocessing

def enroll_student(student_queue):
    for student in ["Rahul","Kartik","Avinash","Indar"]:
        student_queue.put(f"Enroll request for {student}")


def register_student(student_queue):
    while True:
        enrollment_request = student_queue.get()
        if enrollment_request is None:
            break
        else:
            print(f"Register the enrollment request: {enrollment_request}")

if __name__ == "__main__":        
    if True:
        student_queue = multiprocessing.Queue()
        enrollment_process = multiprocessing.Process(target= enroll_student, args = (student_queue, ))
        registration_process = multiprocessing.Process(target=register_student, args= (student_queue,))
    
    enrollment_process.start()
    registration_process.start()

    enrollment_process.join()
    registration_process.join()