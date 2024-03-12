import sys
import os
from threading import Thread

ppath = sys.executable
print(f"path to python executable: {ppath}")

print("installing requirements...")
os.system(f"{ppath} -m pip install -r requirements.txt")
print("requirements installed!")

print("opening notebook")
Thread(target=os.system, args=[f"{ppath} -m jupyter notebook model/notebook.ipynb"]).start()
print("notebook running!")