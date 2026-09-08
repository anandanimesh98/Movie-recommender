import subprocess
import os 
import sys


HELPER_DIR = os.path.dirname(os.path.abspath(__file__))
TRAINER_DIR = os.path.join(os.path.dirname(HELPER_DIR), 'trainer')
RUN_SCRIPT = os.path.join(HELPER_DIR, 'run.sh')
INPUT_FILE = os.path.join(TRAINER_DIR, 'input.txt')
OUTPUT_FILE = os.path.join(TRAINER_DIR, 'test_out.txt')


def printToFile(Arr, n, m):
	mat = []
	for i in range(n+2):
		temp = []
		for j in range(m+2):
			temp.append(0)
		mat.append(temp)

	f=open(INPUT_FILE,"w")
	for tup in Arr:
		print(tup)
		mat[tup[0]][tup[1]] = tup[2]
	
	for i in range(1, n+1):
		for j in range(1, m+1):
			f.write(str(mat[i][j]))
			f.write(' ')
		f.write('\n')
	f.close()


def generate_data_to_process(Arr, n, m):
	print(Arr)
	printToFile(Arr, n, m)


def returnMatrix():
	with open(OUTPUT_FILE) as textFile:
		lines=[line.split() for line in textFile]
	
	return lines



def get_recommended_movies():
	subprocess.run(["bash", RUN_SCRIPT, TRAINER_DIR, sys.executable], check=True)
	a=returnMatrix()
	return a
	



	

