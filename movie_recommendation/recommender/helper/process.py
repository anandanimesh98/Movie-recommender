import subprocess
import os 
import shutil
import sys


HELPER_DIR = os.path.dirname(os.path.abspath(__file__))
TRAINER_DIR = os.path.join(os.path.dirname(HELPER_DIR), 'trainer')
INPUT_FILE = os.path.join(TRAINER_DIR, 'input.txt')
OUTPUT_FILE = os.path.join(TRAINER_DIR, 'test_out.txt')
PREDICTION_FILE = os.path.join(TRAINER_DIR, 'test_file.txt')
TRAIN_SCRIPT = os.path.join(TRAINER_DIR, 'test.py')
RANKER_SOURCE = os.path.join(TRAINER_DIR, 'process.cpp')
RANKER_BINARY = os.path.join(TRAINER_DIR, 'process.exe' if os.name == 'nt' else 'process')
CXX_CANDIDATES = ('c++', 'g++', 'clang++')


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



def runTrainer():
	# common.py imports matplotlib.pyplot, so force a headless backend rather
	# than letting it try to open a window from inside the request handler
	env = dict(os.environ, MPLBACKEND='Agg')
	subprocess.run([sys.executable, TRAIN_SCRIPT], check=True, env=env)


def buildRanker():
	"""Compile the C++ ranker, returning None when no compiler is installed."""
	if os.path.exists(RANKER_BINARY) and os.path.getmtime(RANKER_BINARY) >= os.path.getmtime(RANKER_SOURCE):
		return RANKER_BINARY

	compiler = next((c for c in CXX_CANDIDATES if shutil.which(c)), None)
	if compiler is None:
		return None

	subprocess.run([compiler, '-std=c++17', '-O2', '-o', RANKER_BINARY, RANKER_SOURCE], check=True)
	return RANKER_BINARY


def rankInPython():
	"""Pure Python equivalent of process.cpp, used when there is no compiler."""
	with open(PREDICTION_FILE) as f:
		n, m = (int(x) for x in f.readline().split())
		predicted = [[float(x) for x in f.readline().split()] for _ in range(n)]

	with open(INPUT_FILE) as f:
		actual = [[float(x) for x in f.readline().split()] for _ in range(n)]

	with open(OUTPUT_FILE, 'w') as out:
		for i in range(n):
			# highest predicted rating first, ties broken by the larger column
			order = sorted(range(m), key=lambda j: (predicted[i][j], j), reverse=True)
			for j in order:
				if actual[i][j] == 0:
					out.write(str(j+1))
					out.write(' ')
			out.write('\n')


def get_recommended_movies():
	runTrainer()
	ranker = buildRanker()
	if ranker is None:
		rankInPython()
	else:
		subprocess.run([ranker, TRAINER_DIR], check=True)
	a=returnMatrix()
	return a

