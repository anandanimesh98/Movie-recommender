import subprocess
import os 


def printToFile(Arr, n, m):
	mat = []
	for i in range(n+2):
		temp = []
		for j in range(m+2):
			temp.append(0)
		mat.append(temp)

	f=open("/home/animesh/WTA/movie_recommendation/recommender/trainer/input.txt","w")
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
	with open("/home/animesh/WTA/movie_recommendation/recommender/trainer/test_out.txt") as textFile:
		lines=[line.split() for line in textFile]
	
	return lines



def get_recommended_movies():
	subprocess.run(["bash", "/home/animesh/WTA/movie_recommendation/recommender/helper/run.sh" ])
	a=returnMatrix()
	return a
	



	

