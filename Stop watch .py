#stop watch in python
#$import time
import time
#define watch
def stopwatch():
    input("Press Enter to start the stopwatch.")
    start_time = time.time()

    try:
      #using while loop
        while True:
            elapsed_time = time.time() - start_time
            minutes, seconds = divmod(int(elapsed_time), 60)
            hours, minutes = divmod(minutes, 60)
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
#print statement
            print("\r" + time_str, end="")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopwatch stopped.")
        return

if __name__ == "__main__":
    stopwatch()
