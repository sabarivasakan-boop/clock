import time
import threading
remote=True
remote_timer=True
def timer(hrs,mins,sec):
     format_time="{:02d} H:{:02d} M:{:02d} S".format(int(hrs),int(mins),int(sec))
     global remote_timer
     start=time.perf_counter()
     while remote_timer:
          end=time.perf_counter()-start
          mins,sec=divmod(end,60)
          hrs=mins/60
          format_time1="{:02d} H:{:02d} M:{:02d} S".format(int(mins/60),int(mins),int(sec))
          print(format_time1,end="\r")
          if str(format_time)==str(format_time1):
               remote_timer=False
          time.sleep(0.3)

     

def stop_watch():
     global remote
     start=time.perf_counter()
     while remote:
          end=time.perf_counter()-start
          mins,sec=divmod(end,60)
          format_time="{:02d}:{:02d}".format(int(mins),int(sec))
          print(format_time,end="\r")
          time.sleep(0.3)
def actual_timer():
     global remote
     print("Enter any key to stop the timer :")
     t=threading.Thread(target=stop_watch)
     t.start()
     input()
     remote=False
     t.join() 

if __name__=="__main__":
     user=""
     while user.lower()!="q":
          choice=input("\t\tDEVIL'S CLOCK \n1. Timer\n2. Stop Watch\n 3.Exit\n Enter the operation to perform : ")
          if choice=="1":
               actual_timer()
               print("\nCompleted\n")
          elif choice=="2":
               hrs,mins,sec=map(int,input("Enter the time %H:%M:%S").split(":"))
               timer(hrs,mins,sec)
               print("\n Timer Completed\n")
          elif choice == "3":
               user="q"
          else:
               continue