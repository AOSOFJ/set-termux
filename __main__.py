import os

def worker(work):
  os.system(work)

worker("setup-storage")
worker("apt-get update")
worker("apt install git")
worker("apt install python")
