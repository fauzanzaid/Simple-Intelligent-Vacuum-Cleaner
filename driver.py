#! /usr/bin/python2

from env import Env
from ivc import	IVC, IVCVisibility
from gui import GUI

from iddfsctrlr import IDDFSController
from h1ctrlr import H1Controller
from h2ctrlr import H2Controller
from bestpathctrlr import BestPathController

from config import Config



def printHelp():
	print ""
	print "Enter number corresponding to each option"
	print "[1] Display the environment"
	print "[2] Find path using T1"
	print "[3] Find path using T2"
	print "[4] Show analysis and graphs"
	print "Press enter to exit"



analysis = {i:"Not computed" for i in xrange(1,12)}


room1 = Env(Config.envSizeT1, Config.envDirtT1)
room2a = Env(Config.envSizeT2, Config.envDirtT2)
room2b = Env(Config.envSizeT2, Config.envDirtT2)
room2b.grid = [r[:] for r in room2a.grid]	# Make environment same

cont1 = IDDFSController(room1.dim, Config.homesT1)
cont2a = H1Controller(room2a.dim, Config.homesT2)
cont2b = H2Controller(room2b.dim, Config.homesT2)

vac1 = IVC("Roomba1", room1, [0,0], cont1, IVCVisibility.ALL)
vac2a = IVC("Roomba2a", room2a, [0,0], cont2a, IVCVisibility.ONE)
vac2b = IVC("Roomba2b", room2b, [0,0], cont2b, IVCVisibility.ONE)




mygui = GUI()

mygui.setG1env(room1)
mygui.setG1ivc(vac1)
mygui.setG2env(room2a)
mygui.setG2ivc(vac2a)




while True:
	printHelp()
	opt = raw_input()



	if opt == "1":
		mygui.drawG1()
		mygui.drawG2()



	elif opt == "2":
		vac1.run()
		analysis[1] = cont1.stats["nodesGen"]
		analysis[3] = cont1.stats["maxStackDepth"]
		analysis[4] = vac1.stats["cost"]
		analysis[5] = str(vac1.stats["time"])+"s"
		# mygui.updateG1()
		mygui.updatePathG1(vac1.start, vac1.actionsHistory, Config.pathColorG1, 0)



	elif opt == "3":
		vac2a.run()
		vac2b.run()
		analysis[6] = "H1:"+str(cont2a.stats["nodesGen"])+", H2:"+str(cont2b.stats["nodesGen"])
		analysis[8] = "H1:"+str(vac2a.stats["cost"])+", H2:"+str(vac2b.stats["cost"])
		analysis[9] = "H1:"+str(vac2a.stats["time"])+"s, H2:"+str(vac2b.stats["time"])+"s"
		# mygui.updateG2()
		mygui.updatePathG2(vac2a.start, vac2a.actionsHistory, Config.pathColorG2a, -1)
		mygui.updatePathG2(vac2b.start, vac2b.actionsHistory, Config.pathColorG2b, 1)



	elif opt == "4":
		timeVsRoomSizeH1 = []
		for i in xrange(3,21):
			room = Env([i,i], Config.envDirtT2)
			cont = H1Controller(room.dim, [[0,0],[0,i-1],[i-1,0],[i-1,i-1]])
			vac = IVC("Roomba", room, [0,0], cont, IVCVisibility.ONE)
			vac.run()
			timeVsRoomSizeH1.append(vac.stats["time"])
		mygui.drawG3(timeVsRoomSizeH1, Config.pathColorG2a)

		timeVsRoomSizeH2 = []
		for i in xrange(3,21):
			room = Env([i,i], Config.envDirtT2)
			cont = H2Controller(room.dim, [[0,0],[0,i-1],[i-1,0],[i-1,i-1]])
			vac = IVC("Roomba", room, [0,0], cont, IVCVisibility.ONE)
			vac.run()
			timeVsRoomSizeH2.append(vac.stats["time"])
		mygui.drawG3(timeVsRoomSizeH2, Config.pathColorG2b)

		timeVsDirtSizeH1 = []
		for i in xrange(5,105, 5):
			room = Env([10,10], i/100.0)
			cont = H1Controller(room.dim, [[0,0],[0,9],[9,0],[9,9]])
			vac = IVC("Roomba", room, [0,0], cont, IVCVisibility.ONE)
			vac.run()
			timeVsDirtSizeH1.append(vac.stats["time"])
		mygui.drawG4(timeVsDirtSizeH1, Config.pathColorG2a)

		# timeVsDirtSizeH2 = []
		# for i in xrange(5,105, 5):
		# 	room = Env([10,10], i/100.0)
		# 	cont = H2Controller(room.dim, [[0,0],[0,9],[9,0],[9,9]])
		# 	vac = IVC("Roomba", room, [0,0], cont, IVCVisibility.ONE)
		# 	vac.run()
		# 	timeVsDirtSizeH2.append(vac.stats["time"])
		# mygui.drawG4(timeVsDirtSizeH2, Config.pathColorG2b)

		costAvT1 = 0
		for i in xrange(10):
			room = Env(Config.envSizeT1, Config.envDirtT1)
			cont = IDDFSController(room.dim, Config.homesT1)
			vac = IVC("Roomba", room, [0,0], cont, IVCVisibility.ALL)
			vac.run()
			costAvT1 += vac.stats["cost"]
		costAvT1 /= 10.0

		costAvH1 = 0
		for i in xrange(10):
			room = Env(Config.envSizeT2, Config.envDirtT2)
			cont = H1Controller(room.dim, Config.homesT2)
			vac = IVC("Roomba", room, [0,0], cont, IVCVisibility.ONE)
			vac.run()
			costAvH1 += vac.stats["cost"]
		costAvH1 /= 10.0

		costAvH2 = 0
		for i in xrange(10):
			room = Env(Config.envSizeT2, Config.envDirtT2)
			cont = H2Controller(room.dim, Config.homesT2)
			vac = IVC("Roomba", room, [0,0], cont, IVCVisibility.ONE)
			vac.run()
			costAvH2 += vac.stats["cost"]
		costAvH2 /= 10.0

		analysis[11] = "T1:"+str(costAvT1)+", H1:"+str(costAvH1)+", H2:"+str(costAvH2)

		for k in analysis:
			mygui.drawPartition1Text(k,analysis[k])


	else:
		break
