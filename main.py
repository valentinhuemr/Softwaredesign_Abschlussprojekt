import streamlit as st
import numpy as np
from mechanism import Mechanism
from simulation import MechanismSimulation

st.title("Viergelenk-Mechanismus Simulation")
st.sidebar.header("Mechanismus Konfiguration")

mid_x = st.sidebar.number_input("Mittelpunkt X", value=0.0, step=1.0)
mid_y = st.sidebar.number_input("Mittelpunkt Y", value=0.0, step=1.0)
radius = st.sidebar.number_input("Rotationsradius für Gelenk 2", value=15.0, min_value=1.0, max_value=100.0, step=0.5)
start_angle = st.sidebar.slider("Startwinkel von Gelenk 2 (Grad)", 0, 360, 0)
speed = st.sidebar.slider("Geschwindigkeit (°/Frame)", 1, 10, 2)

num_joints = st.sidebar.number_input("Anzahl der Gelenke", min_value=4, max_value=15, value=4, step=1)
num_rods = st.sidebar.number_input("Anzahl der Stäbe", min_value=3, max_value=num_joints*(num_joints-1)//2, value=4, step=1)

joints = {1: np.array([mid_x, mid_y])}
fixed_joints = {1}

st.sidebar.subheader("Gelenke Konfiguration")
for j in range(3, num_joints + 1):
    with st.sidebar.expander(f"Gelenk {j} bearbeiten"):
        x = st.number_input(f"Gelenk {j} - X", value=0.0, step=1.0, key=f"j_{j}_x")
        y = st.number_input(f"Gelenk {j} - Y", value=0.0, step=1.0, key=f"j_{j}_y")
        fixed = st.checkbox(f"Gelenk {j} fixiert?", value=False, key=f"j_{j}_fixed")
        joints[j] = np.array([x, y])
        if fixed:
            fixed_joints.add(j)

st.sidebar.subheader("Gelenk 2 (Berechnet)")
gelenk_2_x = mid_x + radius * np.cos(np.radians(start_angle))
gelenk_2_y = mid_y + radius * np.sin(np.radians(start_angle))
st.sidebar.text(f"X: {gelenk_2_x:.2f}, Y: {gelenk_2_y:.2f}")
joints[2] = np.array([gelenk_2_x, gelenk_2_y])

st.sidebar.subheader("Stäbe Konfiguration")
rods = []
all_joint_keys = list(joints.keys())

for i in range(1, num_rods + 1):
    joint1 = st.sidebar.selectbox(f"Stab {i} - Gelenk 1", all_joint_keys, key=f"rod_{i}_j1")
    joint2 = st.sidebar.selectbox(f"Stab {i} - Gelenk 2", all_joint_keys, key=f"rod_{i}_j2")
    rods.append((joint1, joint2))

mech = Mechanism([mid_x, mid_y], radius, start_angle, speed, joints, fixed_joints, rods)

if st.button("▶ Simulation starten"):
    sim = MechanismSimulation(mech)
    sim.run_simulation()