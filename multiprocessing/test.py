{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8bfc618a-dd86-43e3-988a-e3b7c5eb5376",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The program finished in 0.17 seconds\n"
     ]
    }
   ],
   "source": [
    "import multiprocessing\n",
    "import time\n",
    "\n",
    "def test_fun():\n",
    "    print(\"Do something\")\n",
    "    print(\"Sleep for 1 second\")\n",
    "    time.sleep(1)\n",
    "    print(\"Done sleeping\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    start = time.perf_counter()\n",
    "\n",
    "    processes = []\n",
    "\n",
    "    for _ in range(4):\n",
    "        p = multiprocessing.Process(target=test_fun)\n",
    "        processes.append(p)\n",
    "        p.start()\n",
    "\n",
    "    for process in processes:\n",
    "        process.join()\n",
    "\n",
    "    end = time.perf_counter()\n",
    "\n",
    "    print(f\"The program finished in {round(end-start, 2)} seconds\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c3b5020b-a95c-48e2-afe1-f317f43cb1e6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
