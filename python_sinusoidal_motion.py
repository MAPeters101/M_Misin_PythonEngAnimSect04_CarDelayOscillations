import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Time array
t0=0
t_end=16
dt=0.02
t=np.arange(t0,t_end+dt,dt)

# Create arrays for motion

# Blue train:
f1=0.125 # [hz]
A1=7 # [m]
train_blue=A1*np.sin(2*np.pi*f1*t)

# Blue train:
f2=0.125 # [hz]
A2=-7 # [m]
train_red=A2*np.cos(2*np.pi*f2*t)

# Cars:
y_i=13
car_green=y_i-2*(t-2)**2
car_purple=y_i-2*(t-6)

############################## ANIMATION ##############################
frame_amount=len(t)

def update_plot(num):

    return

# Set up your figure properties
fig=plt.figure(figsize=(16,9),dpi=80,facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(2,2)

# Subplot 0
ax0=fig.add_subplot(gs[0,0],facecolor=(0.9,0.9,0.9))
X_blue,=ax0.plot([],[],'-b',linewidth=3,label='X_blue = '+str(A1)+'*sin(2pi*'+str(f1)+'*t)')
X_red,=ax0.plot([],[],'-r',linewidth=3,label='X_red = '+str(A2)+'*cos(2pi*'+str(f2)+'*t)')
plt.xlim(t0,t_end)
plt.ylim(-8,8)
plt.grid(True)
plt.xlabel('time [s]')
plt.ylabel('X [m]')
ax0.spines['bottom'].set_position('center')
ax0.xaxis.set_label_coords(0.5,0)
plt.legend(bbox_to_anchor=(1,1.2),fontsize='medium')

# Subplot 1
ax1=fig.add_subplot(gs[1,0],facecolor=(0.9,0.9,0.9))
Y_green,=ax1.plot([],[],'g',linewidth=3)
Y_green2,=ax1.plot([],[],'g',linewidth=3,alpha=0.3)
Y_purple,=ax1.plot([],[],'m',linewidth=3)
Y_purple2,=ax1.plot([],[],'m',linewidth=3,alpha=0.3)
plt.xlim(t0,t_end)
plt.ylim(-2,y_i+1)
plt.grid(True)
plt.xlabel('time [s]')
plt.ylabel('Y [m]')
ax1.spines['bottom'].set_position(('data',0))
ax1.xaxis.set_label_coords(0.5,0)

# Subplot 2
ax2=fig.add_subplot(gs[:,1],facecolor=(0.9,0.9,0.9))
block_blue,=ax2.plot([],[],'-b',linewidth=28)
block_red,=ax2.plot([],[],'-b',linewidth=28)
block_green,=ax2.plot([],[],'-b',linewidth=24)
block_purple,=ax2.plot([],[],'-b',linewidth=24)

# Create danger zone 1
danger_zone1_1,=ax2.plot([3,4],[1,1],'-k',linewidth=3)
danger_zone1_2,=ax2.plot([3,4],[2,2],'-k',linewidth=3)
danger_zone1_3,=ax2.plot([3,3],[1,2],'-k',linewidth=3)
danger_zone1_4,=ax2.plot([4,4],[1,2],'-k',linewidth=3)

# Create danger zone 2
danger_zone2_1,=ax2.plot([3,4],[3,3],'-k',linewidth=3)
danger_zone2_2,=ax2.plot([3,4],[4,4],'-k',linewidth=3)
danger_zone2_3,=ax2.plot([3,3],[3,4],'-k',linewidth=3)
danger_zone2_4,=ax2.plot([4,4],[3,4],'-k',linewidth=3)

# Create danger zone 3
danger_zone3_1,=ax2.plot([-3,-4],[1,1],'-k',linewidth=3)
danger_zone3_2,=ax2.plot([-3,-4],[2,2],'-k',linewidth=3)
danger_zone3_3,=ax2.plot([-3,-3],[1,2],'-k',linewidth=3)
danger_zone3_4,=ax2.plot([-4,-4],[1,2],'-k',linewidth=3)

# Create danger zone 4
danger_zone4_1,=ax2.plot([-3,-4],[3,3],'-k',linewidth=3)
danger_zone4_2,=ax2.plot([-3,-4],[4,4],'-k',linewidth=3)
danger_zone4_3,=ax2.plot([-3,-3],[3,4],'-k',linewidth=3)
danger_zone4_4,=ax2.plot([-4,-4],[3,4],'-k',linewidth=3)

bbox_green=dict(boxstyle='square',fc=(0.9,0.9,0.9),ec='g',lw=1.0)
bbox_purple=dict(boxstyle='square',fc=(0.9,0.9,0.9),ec='purple',lw=1.0)
ax2.text(0.3,y_i+1.5,'car_green='+str(int(y_i))+'-2(t-2)^2',size=10,color='g',bbox=bbox_green)
ax2.text(-7.8,y_i+1.5,'car_purple='+str(int(y_i))+'-2(t-6)',size=10,color='purple',bbox=bbox_purple)



plt.xlim(-max(A1,A2)-1,max(A1,A2)+1)
plt.ylim(-2,y_i+1)
plt.grid(True)
ax2.spines['left'].set_position('center')
ax2.spines['bottom'].set_position(('data',0))




plt.show()



