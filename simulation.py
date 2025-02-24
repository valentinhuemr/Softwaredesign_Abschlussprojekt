import matplotlib.pyplot as plt
import numpy as np
import time
import streamlit as st

class MechanismSimulation:
 def __init__(self,mechanism,scale=50,frames=100):
  self.mechanism=mechanism
  self.scale=scale
  self.frames=frames

 def run_simulation(self):
  placeholder=st.empty()
  fig,ax=plt.subplots()
  ax.set_xlim(-self.scale,self.scale)
  ax.set_ylim(-self.scale,self.scale)

  for _ in range(self.frames):
   self.mechanism.theta+=self.mechanism.speed
   self.mechanism.joints[2]=self.mechanism.compute_gelenk_2()
   optimized_joints=self.mechanism.optimize_joints()

   if optimized_joints:
    ax.clear()
    ax.set_xlim(-self.scale,self.scale)
    ax.set_ylim(-self.scale,self.scale)
    ax.set_title("Mechanismus-Simulation")

    for (j1,j2) in self.mechanism.rods:
     p1,p2=self.mechanism.joints[j1],self.mechanism.joints[j2]
     ax.plot([p1[0],p2[0]],[p1[1],p2[1]],'bo-',markersize=5,linewidth=2)

    for joint in self.mechanism.joints.values():
     ax.scatter(joint[0],joint[1],color='r',zorder=3,s=50)

    placeholder.pyplot(fig)
    time.sleep(0.05)
