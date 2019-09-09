# -*- coding: utf-8 -*-
#
####################################################
#
# PRISM - Pipeline for animation and VFX projects
#
# www.prism-pipeline.com
#
# contact: contact@prism-pipeline.com
#
####################################################
#
#
# Copyright (C) 2016-2019 Richard Frangenberg
#
# Licensed under GNU GPL-3.0-or-later
#
# This file is part of Prism.
#
# Prism is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Prism is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Prism.  If not, see <https://www.gnu.org/licenses/>.

#igg mod:Bryan


try:
	from PySide2.QtCore import *
	from PySide2.QtGui import *
	from PySide2.QtWidgets import *
	psVersion = 2
except:
	from PySide.QtCore import *
	from PySide.QtGui import *
	psVersion = 1

if psVersion == 1:
	from UserInterfaces import UnrealVersionLoad_ui
else:
	from UserInterfaces import UnrealVersionLoad_ui_ps2 as UnrealVersionLoad_ui


from collections import defaultdict
from shutil import copyfile
import sys, os, time,logging,traceback,re,threading
from functools import wraps
from Common import isShotDirEqual,getNameStrs







#logging.basicConfig(filename='D:/BT_bryanTest/03_Workflow/Shots/s-010/unreal_load.log', filemode='w',level=logging.DEBUG)
if sys.version[0] == "3":
	pVersion = 3
else:
	pVersion = 2
global dicDefault
dicDefault = ["scene","BaseColor","CustomDepth","CustomStencil","CustomTags","FinalImage","LightingModel","MaterialAO","Metallic","Opacity","Roughness","SceneColor","SceneDepth","SeparateTranslucencyRGB","SeparateTranslucencyA","Specular","SubsurfaceColor","WorldNormal","WorldPosition","AmbientOcclusion","CustomDepthWorldUnits","SceneDepthWorldUnits","PreTonemapHDRColor","PostTonemapHDRColor","MotionVector"]
global dic
dic = defaultdict(list)
global loadedFileNum
loadedFileNum = 0

class myThread (threading.Thread):
	def __init__(self, threadID, name, tPath, full_ver_dir):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.tPath = tPath
		self.full_ver_dir= full_ver_dir
		#self.showtext("start thread")

	def run(self):
		if not os.path.exists(tPath):
			os.makedirs(tPath)
		#self.showtext("start thread")

	
		for x in dic.keys():	
			passPath=os.path.join(tPath, x)

			if not os.path.exists(passPath):
				os.makedirs(passPath)
			#self.showtext(passPath)					
			for y in dic[x]:
				filePath = os.path.join(passPath, y)
				soureFilePath = os.path.join(self.full_ver_dir, y)			
				if os.path.exists(soureFilePath):
					loadedFileNum += 1
					copyfile(soureFilePath, filePath)


class LoadUnrealVersion(QDialog, UnrealVersionLoad_ui.Ui_UnrealVersionLoad):
	def err_decorator(func):
		@wraps(func)
		def func_wrapper(*args, **kwargs):
			try:
				return func(*args, **kwargs)
			except Exception as e:
				exc_type, exc_obj, exc_tb = sys.exc_info()
				erStr = ("%s ERROR - PrismSettings %s:\n%s\n\n%s" % (time.strftime("%d/%m/%y %X"), args[0].core.version, ''.join(traceback.format_stack()), traceback.format_exc()))
				args[0].core.writeErrorLog(erStr)

		return func_wrapper
		
	@err_decorator
	def __init__(self, core, startText = "", renderPath = ""):
		QDialog.__init__(self)
		self.setupUi(self)
		self.core = core
		self.core.parentWindow(self)
		self.init_combo(startText)
		#this combo box lists all the sequences in the unreal folder
		self.comboBox.currentIndexChanged.connect(self.selectionchange_seq)
		#this combo box lists all the versions for a given shot
		self.comboBox_2.currentIndexChanged.connect(self.selectionchange_ver)
		self.pushButton.clicked.connect(self.loadClicked)
	
		self.renderPath = renderPath
		fPath = os.path.join(renderPath, "unreal_load.log")

	
	def showtext(self, ptext):
		msg = QDialog()
		msg.setWindowTitle("Load Info")
		l_info = QLabel(ptext)
		bLayout = QVBoxLayout()
		bLayout.addWidget(l_info)
		bLayout.addStretch()
		msg.setLayout(bLayout)
		msg.setParent(self.core.messageParent, Qt.Window)
		msg.setFocus()
		action = msg.exec_()	
	
	def selectionchange_ver(self):
		if self.comboBox_2.count() > 0 :
			dic.clear()
			self.file_num_ver = 0
			self.ver_dir=self.comboBox_2.currentText()
			self.full_ver_dir=self.full_seq_dir+"/"+self.ver_dir
			cachepass = ""
			i=0.01
			for dirpath, dirnames, filenames in os.walk(self.full_ver_dir):			
				for filename in filenames:
					if len(cachepass)!=0 and cachepass in filename:
							dic[cachepass].append(filename)
					else:		
						for passname in dicDefault:
							if passname in filename:
								dic[passname].append(filename)
								cachepass = passname
								break
					i+=0.01;
					#self.showtext(filename)
					self.progressBar.setValue(100*(i))		
			self.progressBar.setValue(50)			

	@err_decorator
	def loadClicked(self):
		self.pushButton.setEnabled(False)
		
		self.selectionchange_ver()
		nameList=[]
		getNameStrs(self.seq_dir,nameList)	
		folderStr=""
		if len(nameList)==2:
			if len(folderStr)==0:
				folderStr+="lgt"
			else:
				folderStr+=nameList[1]
			
		nameList=[]	
		getNameStrs(self.ver_dir,nameList,1)				
		if len(nameList)==2:
			if len(folderStr) >0:
				folderStr+="_"
				folderStr+=nameList[1]
		else :
			self.showtext("version folder name is wrong, please change it!")
			return
		folderStr+="_UE"	
		tPath = os.path.join(self.renderPath, "Rendering", "3dRender", folderStr, nameList[0])
		totalFileNum = 0		
		for x in dic.keys():
			for y in dic[x]:
				totalFileNum+=1
		thread = myThread(1, "test", tPath ,self.full_ver_dir)
		thread.start()
		while 1:
			if totalFileNum!= loadedFileNum:
				#self.showtext(str(loadedFileNum) +" files have been loaded!")
				self.progressBar.setValue(100*(0.5 * loadedFileNum/totalFileNum + 0.5))
			else:
				break
		self.showtext(str(loadedFileNum) +" files have been loaded!")
		thread.join()
		self.pushButton.setEnabled(True)


	#
	def selectionchange_seq(self,i):
		self.seq_dir=""
		if self.comboBox.count() > 0 :
			self.comboBox_2.clear()
			self.seq_dir = self.comboBox.currentText()
			self.full_seq_dir=""
			if self.unreal_dir[-1]=='\\' or self.unreal_dir[-1]=='/' :
				self.full_seq_dir = self.unreal_dir + self.seq_dir
			else:
				self.full_seq_dir = self.unreal_dir + "/" + self.seq_dir
			for dirpath, dirnames, filenames in os.walk(self.full_seq_dir):
				for dir in dirnames:
						self.comboBox_2.addItem(dir)


		

	@err_decorator
	def init_combo(self, startText = "" ):
		pcData = {}
		pcData["unDir"] = ["globals", "unreal_dir"] #igg mod:Bryan
		pcData = self.core.getConfig(data=pcData, configPath=self.core.prismIni)
		if pcData["unDir"] is None:
			return 
		self.unreal_dir = pcData["unDir"]
		#self.showtext(startText)
		#seq_dir = startText.split("-")[1]		
		for dirpath, dirnames, filenames in os.walk(self.unreal_dir):
			for dir in dirnames:
				#self.showtext(startText+"|||"+dir)
				if isShotDirEqual(startText,dir):
					self.comboBox.addItem(dir)
		if self.comboBox.count() > 0 :
			self.selectionchange_seq(0) #init the combo box for shot


		