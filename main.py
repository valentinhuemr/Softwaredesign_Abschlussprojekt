import streamlit as st
import numpy as np
from mechanism import Mechanism
from simulation import MechanismSimulation

DEFAULT_FIXED_POINT=[0,0]
DEFAULT_RADIUS=15
DEFAULT_START_ANGLE=0
DEFAULT_SPEED=2
DEFAULT_JOINTS={1:np.array([0,0]),2:np.array([15,0]),3:np.array([10,10]),4:np.array([20,5])}
DEFAULT_FIXED_JOINTS={1}
DEFAULT_RODS=[(1,2),(2,3),(3,4),(4,1)]

mech=Mechanism(DEFAULT_FIXED_POINT,DEFAULT_RADIUS,DEFAULT_START_ANGLE,DEFAULT_SPEED,DEFAULT_JOINTS,DEFAULT_FIXED_JOINTS,DEFAULT_RODS)

st.title("Viergelenk-Mechanismus Simulation")
st.sidebar.header("Einstellungen")

radius=st.sidebar.number_input("Radius",value=DEFAULT_RADIUS,step=1)
start_angle=st.sidebar.slider("Startwinkel (°)",0,360,DEFAULT_START_ANGLE)
speed=st.sidebar.slider("Geschwindigkeit (°/Frame)",1,10,DEFAULT_SPEED)

mech.radius=radius
mech.theta=np.radians(start_angle)
mech.speed=np.radians(speed)

if st.sidebar.button("▶️ Simulation starten"):
 sim=MechanismSimulation(mech)
 sim.run_simulation()

st.sidebar.subheader("Aktuelle Mechanismus-Daten:")
st.sidebar.text(f"Fixpunkt: {DEFAULT_FIXED_POINT}")
st.sidebar.text(f"Gelenke: {list(DEFAULT_JOINTS.keys())}")
st.sidebar.text(f"Stäbe: {DEFAULT_RODS}")
