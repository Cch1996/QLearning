#!/usr/bin/python
#-*- coding: utf-8 -*-
from Tkinter import *
import tkFont
from juzhen import juzhen
#global gridworld
#gridworld = juzhen()
class Graphics:
	QValues = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	Arrows = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	iteration = 0
	IterateCount = 0
	QV = 0
	noise = 0
	livingreword = 0
	discount = 0
	gridworld = 0
	def __init__(self,root):
		self.root = root
		Graphics.gridworld = juzhen()
	def drawGraphics(self):
		cv = Canvas(root,bg='black',height=400,width=520)
		Graphics.noise =StringVar()
		Graphics.discount=StringVar()
		Graphics.livingreword =StringVar()
		Graphics.QV = cv
		
		cv.create_rectangle(50,50,130,130,fill='green',outline='white')
		cv.create_rectangle(130,50,210,130,fill='green',outline='white')
		cv.create_rectangle(210,50,290,130,fill='green',outline='white')
		cv.create_rectangle(290,50,370,130,fill='green',outline='white')
		cv.create_rectangle(300,60,360,120,fill='green',outline='white')
		cv.create_rectangle(50,130,130,210,fill='green',outline='white')
		cv.create_rectangle(130,130,210,210,fill='gray',outline='white')
		cv.create_rectangle(210,130,290,210,fill='green',outline='white')
		cv.create_rectangle(290,130,370,210,fill='red',outline='white')
		cv.create_rectangle(300,140,360,200,fill='red',outline='white')
		cv.create_rectangle(50,210,130,290,fill='green',outline='white')
		cv.create_rectangle(130,210,210,290,fill='green',outline='white')
		cv.create_rectangle(210,210,290,290,fill='green',outline='white')
		cv.create_rectangle(290,210,370,290,fill='green',outline='white')
		#Graphics.QValues[0][3] = cv.create_text(330,90,text='1.00',fill='white')
		#Graphics.QValues[1][3] = cv.create_text(330,170,text='-1.00',fill='white')
		afont = tkFont.Font(size=19)
		Graphics.IterateCount = cv.create_text(170,330,font = afont,text="VALUES AFTER " + str(Graphics.iteration) + " ITERATION",fill='white')
		cv.pack()
		Button(root,text="cotinue",command = deletee).pack(side='left')
		Label(root,width=5,text='noise:').pack(side='left')
		Entry(root,width=5,textvariable=Graphics.noise).pack(side='left')
		Graphics.noise.set('0.2')
		Label(root,width=8,text='discount:').pack(side='left')
		Entry(root,width=5,textvariable=Graphics.discount).pack(side='left')
		Graphics.discount.set('0.9')
		Label(root,width=10,text='livingreward:').pack(side='left')
		Entry(root,width=5,textvariable=Graphics.livingreword).pack(side='left')
		Graphics.livingreword.set('0.0')
		Button(root,text="reset",command = resets).pack(side='left')
		root.geometry('520x450')
		root.title('Q learning')
		#frame = Frame(root,height=400,width=500,bg='black').pack(expand=YES,fill=BOTH)
		root.mainloop()
		

def deletee():
		for i in range(3):
			for j in range(4):
				if Graphics.QValues[i][j] != 0:
					Graphics.QV.delete(Graphics.QValues[i][j])
				if Graphics.Arrows[i][j] != 0:
					Graphics.QV.delete(Graphics.Arrows[i][j])
		Graphics.QV.delete(Graphics.IterateCount)
		Graphics.iteration = Graphics.iteration + 1
		afont = tkFont.Font(size=19)
		Graphics.IterateCount = Graphics.QV.create_text(170,330,font=afont,text="VALUES AFTER " + str(Graphics.iteration)+ " ITERATION",fill='white')
		Graphics.gridworld.stepinto()
		content = Graphics.gridworld.returnTheQValue()
		direction = Graphics.gridworld.returnTheDirection()
		i=0
		j=0
		for value in content:
			value = round(value,2)
			if value != 0.0:
				Graphics.QValues[i][j] = Graphics.QV.create_text(90+80 * j,90 + 80 * i,text=str(value),fill='white')
			i = i + 1
			if i == 3:
				i = 0
				j = j + 1
		i=0
		j=0
		for direct in direction:
			drawArrow(i,j,direct)
			i = i + 1
			if i == 3:
				i = 0
				j = j + 1
def drawArrow(i,j,direct):
	if i==0 and j == 3:
		return
	elif i == 1 and j==1:
		return
	elif i == 1 and j == 3:
		return
	if direct == 3: #north
		Graphics.Arrows[i][j] = Graphics.QV.create_polygon( (90+ 80*j ,50 + 80*i ,90+80*j-5,50+80*i+5,90+80*j+5,50+80*i+5),fill='white')
	elif direct == 2: # west
		Graphics.Arrows[i][j] = Graphics.QV.create_polygon((50+80*j+5,90+80*i-5,50+80*j,90+80*i,50+80*j+5,90+80*i+5),fill='white')
	elif direct == 1: # south
	    Graphics.Arrows[i][j] = Graphics.QV.create_polygon((90+80*j,130+80*i,90+80*j-5,130+80*i-5,90+80*j+5,130+80*i-5),fill='white')
	elif direct == 0: # east
		Graphics.Arrows[i][j] = Graphics.QV.create_polygon((130+80*j,90+80*i,130+80*j-5,90+80*i-5,130+80*j-5,90+80*i+5),fill='white') 

def resets():
	for i in range(3):
		for j in range(4):
			if Graphics.QValues[i][j] != 0:
				Graphics.QV.delete(Graphics.QValues[i][j])
			if Graphics.Arrows[i][j] != 0:
				Graphics.QV.delete(Graphics.Arrows[i][j])
	newNoise = Graphics.noise.get()
	newDiscount = Graphics.discount.get()
	newLivingReward = Graphics.livingreword.get()
	Graphics.iteration = 0
	Graphics.QV.delete(Graphics.IterateCount)
	if newNoise == '':
		newNoise = 0.2
	if newDiscount == '':
		newDiscount = 0.9
	if newLivingReward == '':
		newLivingReward = 0.0
	Graphics.gridworld = juzhen(noise=float(newNoise),discount=float(newDiscount),livingreward=float(newLivingReward))
	#a.stepinto()
	#print a.returnTheQValue()



if __name__ == '__main__':
	root = Tk()
	g = Graphics(root)

	g.drawGraphics()
	
	#gridworld = juzhen()
