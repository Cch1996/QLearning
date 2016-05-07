#!/usr/bin/python
#-*- coding: utf-8 -*-
#矩阵中对应格子的编号
#the index of each grid
# 0 3 6 9
# 1 4 7 10
# 2 5 8 11


#数组中的方向表示
#        3=north
#2=west              0=east
#        1=south
#


class juzhen:
    #'价值的矩阵'
    Direction=[0 for row in range(12)]
    B_content=[0 for row in range(12)]
    content=[0 for row in range(12)]
    matrix=[[0 for col in range(12)] for row in range(12)]
# win is the value of the 9th grid, los is the value of 10th grid, noise discount reward 
#win表示9号格子的值，los表示10号格子的值，noise表示到两边的概率，discount表示值的递减，reward表示生存奖励
    def __init__(self,win=1,los=-1,noise=0.2,discount=0.9,livingreward=0.0):
        self.noise=noise
        self.discount=discount
        self.livingreward=livingreward
        self.stepNo=0
        for k in range(12) :
            self.content[k]=0
            self.B_content[k]=0
            self.Direction[k]=3
            self.Direction[k] = -1
        self.content[9]=win
        self.content[10]=los

        for i in range(12) :
            for j in range(12) :
                self.matrix[i][j]=-1

        self.matrix[0][1]=0
        self.matrix[0][3]=0
        self.matrix[1][0]=0
        self.matrix[1][2]=0
        self.matrix[2][1]=0
        self.matrix[2][5]=0
        self.matrix[3][0]=0
        self.matrix[3][6]=0
        self.matrix[5][2]=0
        self.matrix[5][8]=0
        self.matrix[6][3]=0
        self.matrix[6][7]=0
        self.matrix[6][9]=0
        self.matrix[7][6]=0
        self.matrix[7][8]=0
        self.matrix[7][10]=0
        self.matrix[8][5]=0
        self.matrix[8][11]=0
        self.matrix[8][7]=0
        self.matrix[11][10]=0
        self.matrix[11][8]=0


    def show(self,rows=12,cols=12) :
       for i in range(rows):
          for j in range(cols):
              print (self.matrix[i][j])

    def showcontent(self,rows=12):
        for k in range(rows)  :
            print(self.content[k])


    def added_num(self,k,n):
        if (n<0) :
            return self.B_content[k]
        elif(n>11) :
            return  self.B_content[k]
        elif (self.matrix[k][n]==-1) :
#            print(self.matrix[k][n])
            return self.B_content[k]
        elif (self.matrix[k][n]!=-1):
 #           print(self.matrix[k][n])
            return self.B_content[n]
        else :
            print("error")


    def stepinto(self):
        self.stepNo+=1
        for k in range(12) :
            self.B_content[k]=self.content[k]
        for start in range(12) :
            for to in range(12) :
                if self.matrix[start][to]!=-1 :
                    temp=start-to

#                    print(temp)
                    tempmax=max(self.content[start],self.livingreward+self.discount*((1-self.noise)*self.B_content[to]+
                        0.5*self.noise*self.added_num(start, (start+4-temp))+0.5*self.noise*self.added_num(start,start-4+temp)))
                    if(self.content[start]<tempmax) :
                        if (temp==-3) :
                            self.Direction[start]=0
                        elif(temp==-1) :
                            self.Direction[start]=1
                        elif(temp==3) :
                            self.Direction[start]=2
                        elif(temp==1) :
                            self.Direction[start]=3
                        else:
                            print("error in direction !")
                    self.content[start]=tempmax
    def returnTheDirection(self):
        return self.Direction
    def returnTheQValue(self):
        return self.content
    
#juzhen1=juzhen()
#juzhen1.showcontent()
#for i in range(100) :
#juzhen1.stepinto()
#juzhen1.showcontent()