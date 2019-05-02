# -*- coding: utf-8 -*-
"""

@author: Anıl
"""

from scipy import interpolate
import numpy as np

import matplotlib.pyplot as plt
import glob



xut = glob.glob("*.txt")
mnmn=int(len(xut)-1)

       
       #                    PART A
       
       
       
for i in range(mnmn):
       adddd=xut[i+1]
       a=np.loadtxt(adddd) ###normalization
       xcoor=a[0:,0]
       ll=int(len(xcoor))
       ff=xcoor.max()
       cc=xcoor.min()
       gg=[]
       for i in range(ll):
          x2=(xcoor[i]-(cc))/(ff-cc)
          gg.append(x2)
######################################### go 1 to 1  
       xcoor=a[0:,0]
       ycor=a[0:,1]
       c=int(len(xcoor)/2)
       g=a[0:c,0:]
       h=g[::-1]
       a[0:c,0:]=h
       camber_list_length = int(len(xcoor) / 2)
       
       #                     PART B
       
       
################################# airfoil drowing
       t=a[0:,0]
       p=a[0:,1]
       plt.plot(t,p)
       plt.ylim(-0.3,0.3)
############################  camberline
       ss=[]
       for n in range(c):
           bb=(ycor[(ll-1)-n]+ycor[n])/2
           ss.append(bb)
       hh=a[:c,0]
       plt.plot(hh,ss)
       plt.ylim(-0.3,0.3)
       plt.title(adddd[:-4])
##################For camber
       y=np.linspace(0,0,c)
       x=np.linspace(0,1,c)
       plt.plot(x,y)
####################### thickness
       q=a[0:,0]
       j=[]
       for v in range(c):
          uu=(ycor[v]-ycor[(ll-1)-v])
          j.append(uu)
          
       
       k=max(j)
       
       xx=j.index(k)
       vv=q[xx]*100
       plt.text(0.0, -0.38,'Maximum Thickness Location Percentage =' + str(vv) +'c' )
       ı=np.linspace(q[xx],q[xx],2)
       r=[ycor[xx],ycor[(ll-1)-xx]] 
       
       T = np.abs(ycor[xx]-ycor[(ll-1)-xx])  #Max Thickness calculation
       plt.text(0.6, 0.25, 'Max Thickness ='+ str(T) )
       plt.plot(ı,r)
       plt.ylim(-0.3,0.3)
       
##########################################
       
       
       #                    PART C



       gg=int(len(a))
       xu=a[0:c,0]
       yu=a[0:c,1]
       xl=a[c:,0]
       yl=a[c:,1]
       mb=int(len(xu)/2)
   ##Panels
       f1=interpolate.interp1d(xu,yu,kind='cubic')
       f2=interpolate.interp1d(xl,yl,kind='cubic')
    
       xnew1=np.linspace(0,1,21)
       xnew2=xnew1[::-1]
       yunew=f1(xnew1)
       ylnew=f2(xnew2)
       z=int(len(xnew1)-1)
       plt.plot(xnew1,yunew,'.',xnew2,ylnew,'.')
       plt.ylim(-0.3,0.3)

       v=[]
       kk=[]
       for n in range(z):    #######    normal  x upper
            pp=(xnew1[n]+xnew1[n+1])/2
            v.append(pp)

       for i in range(z):
            kj=(yunew[i]+yunew[i+1])/2 ####### normal  upper y
            kk.append(kj)

       uy=[]
       yu=[]


       for n in range(z):    #######    normal  x lover
           kl=(xnew2[n]+xnew2[n+1])/2
           uy.append(kl)


       for i in range(z):
           kz=(ylnew[i]+ylnew[i+1])/2 ####### normal  lover y
           yu.append(kz)


######################### for upper surface
       saa=[]
       dgg=[]
       for i in range(z):
          nm=np.arctan((yunew[i]-yunew[i+1])/(xnew1[i]-xnew1[i+1]))
          dgg.append(nm)
          jh=np.sqrt((xnew1[i]-xnew1[i+1])**2+(yunew[i]-yunew[i+1])**2)
          saa.append(jh)
    

       rsin=[]
       rcos=[]
       for i in range(z):
          xxx=np.cos(dgg[i])*1
          rcos.append(xxx)
          yyy=np.sin(dgg[i])*1
          rsin.append(-yyy)
    
       plt.quiver(v,kk,rsin,rcos)
       plt.ylim(-0.3,0.3)


################## for lower surface

       sa=[]
       dg=[]
       for i in range(z):
          nm=np.arctan((ylnew[i]-ylnew[i+1])/(xnew2[i]-xnew2[i+1]))
          dg.append(nm)
          jh=np.sqrt((xnew2[i]-xnew2[i+1])**2+(ylnew[i]-ylnew[i+1])**2)
          sa.append(jh)
    

       rsin=[]
       rcos=[]
       for i in range(z):
          xxx=np.cos(dg[i])*1#sa[i] if ı put the this data my arrow distance is not equal
          rcos.append(-xxx)
          yyy=np.sin(dg[i])*1#sa[i]
          rsin.append(yyy)
  
       plt.quiver(uy,yu,rsin,rcos)
       plt.ylim(-0.3,0.3)
######################################################### kutta  

       f=a[0:,0]
       g=a[0:,1]
       z=1           ######### upper surface
       k=0
       d=int(len(f)-1)
       c=int(len(f)-2)######### lower surface
       x1=f[c]
       y1=g[c]
       x22=f[k]
       y22=g[k]
       x2=f[d]
       y2=g[d]
       x3=f[z]
       y3=g[z]

       if y22!=0 and y2!=0:
            y22=0
            y2=0
       else:
            y22=0

            
    
       xval=[]
       yval=[]
       xval.append(x1)
       xval.append(x2)
       xval.append(x22)
       xval.append(x3)

       yval.append(y1)
       yval.append(y2)
       yval.append(y22)
       yval.append(y3)
       xv=int(len(xval))
       cvc=np.linspace(0,0,xv)
       vcv=np.linspace(0.95,1,xv)


       def fx(x22,y22,x3,y3):
    
             return np.abs((y3-y22)/(x3-x22))    #######upper
       def fxx(x1,y1,x2,y2):
    
             return np.abs((y1-y2)/(x1-x2))  #####lower



       for i in range(camber_list_length,int(len(xcoor))):
             if ycor[c] > 0:
                 plt.text(0.10, 0.25,'The airfoil is cusped' )
                 break
             else:
                 plt.text(0.10, 0.25,'The airfoil is pointed' )
            
       plt.savefig('' + adddd[:-4] +'.jpg', dpi=240)
       plt.show()
       
     