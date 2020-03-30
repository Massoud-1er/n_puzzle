    
import sys
from itertools import combinations
import subprocess

def tester():

    print("testing 50 map of size 3 :")
    for _ in range(50):
        subprocess.run("/usr/bin/python2.7 generator.py 3 > map_3.txt", shell=True)
        subprocess.run("cat map_3.txt | python3 main.py > output.log", shell=True)
        subprocess.run("cat output.log", shell=True)

    print("testing 50 map of size 4 :")
    for _ in range(50):
        subprocess.run("python2 generator.py 4 > map_4.txt", shell=True)
        subprocess.run("cat map_4.txt | python3 main.py > output.log", shell=True)
        subprocess.run("cat output.log", shell=True)

tester()