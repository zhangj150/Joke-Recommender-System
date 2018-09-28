#uses python2
#from flask import Flask
#from getJSONJokes import dfList
import pickle
import random

from semanticpy.vector_space import VectorSpace

######parse json jokes#########
#done in other file
#run getJSONJokes.py first
###############################

#randIX = random.randint(0, len(dfList)-1001)
#vector_space = VectorSpace(dfList[:100])

filehandler = open('vsm.obj', 'r')
vector_space = pickle.load(filehandler) #loads pretrained vector space model

reccQueue = [random.randint(0, 9000)] #queue of indices of jokes to recommend

currJokeIX = reccQueue.pop(0) #produce random first joke
print('first joke:')
print('-----------------')
print(vector_space.jokes[currJokeIX])
print('\n\n')

######run loop below each time user clicks like or dislike############
#Show score for relatedness against document 0


userlikesjoke = True
if userlikesjoke:
	toAdd = [i[2] for i in vector_space.related(currJokeIX)]
	toAdd.extend(reccQueue)
	reccQueue = toAdd

else: #user doesnt like joke
	if len(reccQueue) == 0:
		reccQueue = [random.randint(0, 999)]

currJokeIX = reccQueue.pop(0) #pop current joke off queue
print('2nd joke:')
print('-----------------')
print(vector_space.jokes[currJokeIX])#print to web screen

####end loop#########

# while len(reccQueue) > 0:
# 	print('----------------')
# 	print(vector_space.jokes[reccQueue.pop(0)])
