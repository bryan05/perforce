#>>>PrismStart
from maya import OpenMaya as omya


def savecallbackPrism():
	print "apply prism save to all maya saves1"
	saveCallback = omya.MSceneMessage.addCallback(
       omya.MSceneMessage.kBeforeSave,
       aboutToSaveFunction)


def aboutToSaveFunction():
   print 'About to save!'
   
if omya.MGlobal.mayaState() != omya.MGlobal.kBatch:
	try:
		import PrismInit
		pcore = PrismInit.prismInit()
	except:
		print "Error occured while loading pcore"
#<<<PrismEnd




