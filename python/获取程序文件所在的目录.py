import os

def chwd():
    os.chdir(os.path.split(os.path.realpath(__file__))[0])

print(os.path.split(os.path.realpath(__file__))[0])