import numpy as np
import scipy.signal as sig
a=(9,8)
#print a[0]
size=(2,10,1)
size2=(4,3)
zx=np.random.uniform(-0.1,0.1,size=size)
zy=np.random.uniform(-0.1,0.1,size=size2)
ad=np.array([16,2,3,13,5,11,10,8])
ad2=np.array([[0.8,0.1,-0.6],[0.3,0.5,0.7],[-0.4,0,-0.2]])
as11=np.rot90(ad2)
as22=np.rot90(as11)
a2=np.where(ad2<0,0.01,1)
maps = np.zeros((1,2))
zxx=[[-5,1,21],[1,2,0]]
print np.all(zxx)
#sig.convolve2d(ad,as22,mode="valid")
#sum=sum+zx[0,:,:]+zx[1,:,:]
adss=np.unravel_index(np.argmax(ad),(2,4))
#print ad
as1=np.rot90(ad)
#print np.rot90(as1)
zz=sig.convolve2d(zx[0,:,:], [[0,1],[1,0]], mode='valid')
#print zz