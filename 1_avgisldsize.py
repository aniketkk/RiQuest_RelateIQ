#!/usr/bin/python
import sys

size = int(raw_input())
archipelago = [[0 for x in range(0,size)] for x in range(0, size)]
visited = [[False for x in range(0,size)] for x in range(0, size)]

i,j,sum,count,temp =  0,0,0,0,['0' for x in range(0, size+1)]
for i in range(0,size):
	temp[i] = sys.stdin.readline()  
#********************create the archipelago**************************************************	
for i in range(0, size):
	for j in range(0, size):
		if temp[i][j] == '\n':
			j = 0
			i += 1
		elif temp[i][j] == '1':
			archipelago[i][j]=int(temp[i][j])
			sum += 1 #check the total land area i.e 1's in the archipelago
		else: archipelago[i][j]=int(temp[i][j])
#********************************************************************************************
#**********check if there are only zeroes or only ones***************************************

if sum == 0:
        print 0
	sys.exit()

if sum%(size*size) == 0:
        print sum
	sys.exit()



#********************depth first search to demarcate islands from oceans*********************

def dfs(i, j, archipelago, visited):
        if i < 0 or i>len(archipelago)-1 or j<0 or j>len(archipelago)-1: # beyond the 7 seas......i.e boundary condition check
                return 0
	if archipelago[i][j] == 0:
		return 0
	elif archipelago[i][j] == 1 and visited[i][j] == True: #if an part of an island has been visited then it is counted as 0
		return 0
        elif archipelago[i][j] == 1 and visited[i][j] == False: #if not visited then explore it for hidden treasures!
		visited[i][j] = True	
                if dfs(i+1, j, archipelago, visited)+ \
               	dfs(i, j-1, archipelago, visited)+ \
                dfs(i, j+1, archipelago, visited)+ \
                dfs(i-1, j, archipelago, visited) == 0:
			return 0
		
	return 1
#********************************************************************************************

for i in range(0, size):
	for j in range(0, size):
		if archipelago[i][j] == 1 and visited[i][j] == False:
			if dfs(i,j,archipelago, visited) == 0: # this condition check if the entire island is visited since all of it neighbors are either visited or 0's
				count+=1
#*******************************write output to stdout***************************************
sys.stdout.write(str(int(sum//count))+'\n')
