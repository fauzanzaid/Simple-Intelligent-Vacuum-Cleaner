class Config(object):
	
	# Env sizes and dirst % can be set here

	envSizeT1 = [4,4]
	envDirtT1 = 0.3
	homesT1 = [
		[0,0],
		[0,envSizeT1[1]-1],
		[envSizeT1[0]-1,0],
		[envSizeT1[0]-1,envSizeT1[1]-1]
	]
	
	envSizeT2 = [10,10]
	envDirtT2 = 0.3
	homesT2 = [
		[0,0],
		[0,envSizeT2[1]-1],
		[envSizeT2[0]-1,0],
		[envSizeT2[0]-1,envSizeT2[1]-1]
	]

	pathColorG1 = (1,0,0)
	pathColorG2a = (0,0,1)
	pathColorG2b = (0,0.7,0)