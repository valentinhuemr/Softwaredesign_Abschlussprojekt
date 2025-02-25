import streamlit as st
import numpy as np
from mechanism import Mechanism
from storage import save_mechanism, load_mechanism, get_all_mechanism_names
from simulation import simulate_mechanism

st.title("Simulation eines Viergelenk-Mechanismus")
st.sidebar.header("Mechanismus Konfiguration")

saved_mechanisms = get_all_mechanism_names()
selected_mechanism = st.sidebar.selectbox("Gespeicherte Mechanismen", ["-"] + saved_mechanisms)

if "loaded_data" not in st.session_state:
    st.session_state.loaded_data = None

if st.sidebar.button("Laden"):
    if selected_mechanism != "-":
        loaded_mech = load_mechanism(selected_mechanism)
        if loaded_mech:
            st.session_state.loaded_data = {
                "mid_x": loaded_mech.fixed_point[0],
                "mid_y": loaded_mech.fixed_point[1],
                "radius": loaded_mech.radius,
                "start_angle": np.degrees(loaded_mech.theta),
                "speed": np.degrees(loaded_mech.speed),
                "num_joints": len(loaded_mech.joints),
                "num_rods": len(loaded_mech.rods),
                "joints": loaded_mech.joints,
                "fixed_joints": loaded_mech.fixed_joints,
                "rods": loaded_mech.rods
            }

mid_x = st.sidebar.number_input("Mittelpunkt X", value=st.session_state.loaded_data["mid_x"] if st.session_state.loaded_data else 0.0, step=1.0)
mid_y = st.sidebar.number_input("Mittelpunkt Y", value=st.session_state.loaded_data["mid_y"] if st.session_state.loaded_data else 0.0, step=1.0)
radius = st.sidebar.number_input("Rotationsradius für Gelenk 2", value=st.session_state.loaded_data["radius"] if st.session_state.loaded_data else 15.0, min_value=1.0, max_value=100.0, step=0.5)
start_angle = st.sidebar.slider("Startwinkel von Gelenk 2 (Grad)", 0, 360, int(st.session_state.loaded_data["start_angle"]) if st.session_state.loaded_data else 0)
speed = st.sidebar.slider("Geschwindigkeit (°/Frame)", 1, 10, int(st.session_state.loaded_data["speed"]) if st.session_state.loaded_data else 2)

num_joints = st.sidebar.number_input("Anzahl der Gelenke", min_value=4, max_value=15, value=st.session_state.loaded_data["num_joints"] if st.session_state.loaded_data else 4, step=1)
num_rods = st.sidebar.number_input("Anzahl der Stäbe", min_value=3, max_value=num_joints*(num_joints-1)//2, value=st.session_state.loaded_data["num_rods"] if st.session_state.loaded_data else 4, step=1)

joints = {1: np.array([mid_x, mid_y])}
fixed_joints = {1}
show_trajectory = {}

st.sidebar.subheader("Gelenke Konfiguration")
for j in range(2, num_joints + 1):
    with st.sidebar.expander(f"Gelenk {j} bearbeiten"):
        x = st.number_input(f"Gelenk {j} - X", value=st.session_state.loaded_data["joints"].get(j, [0.0, 0.0])[0], step=1.0, key=f"j_{j}_x")
        y = st.number_input(f"Gelenk {j} - Y", value=st.session_state.loaded_data["joints"].get(j, [0.0, 0.0])[1], step=1.0, key=f"j_{j}_y")
        fixed = st.checkbox(f"Gelenk {j} fixiert?", value=j in st.session_state.loaded_data["fixed_joints"] if st.session_state.loaded_data else False, key=f"j_{j}_fixed")
        show_trajectory[j] = st.checkbox(f"Bahnkurve anzeigen?", key=f"show_traj_{j}")
        joints[j] = np.array([x, y])
        if fixed:
            fixed_joints.add(j)

mech = Mechanism([mid_x, mid_y], radius, start_angle, speed, joints, fixed_joints, rods=[])

name = st.sidebar.text_input("Mechanismus Name")
if st.sidebar.button("Speichern"):
    save_mechanism(mech, name)

if st.button("Simulation starten"):
    simulate_mechanism(mech, 100)

