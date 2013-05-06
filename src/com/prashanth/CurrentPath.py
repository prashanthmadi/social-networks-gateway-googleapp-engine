import os

def hubPathDir():
	path = os.path.split(__file__)[0]
	return path

def constantFilesPathDir():
	path = os.path.join(hubPathDir(), "constants")
	return path
