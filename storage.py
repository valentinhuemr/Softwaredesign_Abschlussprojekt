from tinydb import TinyDB, Query
import numpy as np
from mechanism import Mechanism
import streamlit as st

db = TinyDB("mechanism_configurations.json")

def save_mechanism(mechanism, name):
    if name:
        db.upsert({
            "name": name,
            "fixed_point": mechanism.fixed_point.tolist(),
            "radius": mechanism.radius,
            "theta": np.degrees(mechanism.theta),
            "speed": np.degrees(mechanism.speed),
            "joints": {str(k): v.tolist() for k, v in mechanism.joints.items()},
            "fixed_joints": list(mechanism.fixed_joints),
            "rods": [tuple(pair) for pair in mechanism.rods]
        }, Query().name == name)
        st.sidebar.success(f"Mechanismus '{name}' gespeichert!")
    else:
        st.sidebar.error("Bitte einen gültigen Namen eingeben.")

def load_mechanism(name):
    config = Query()
    result = db.get(config.name == name)
    
    if result:
        try:
            return Mechanism(
                fixed_point=np.array(result["fixed_point"]),
                radius=result["radius"],
                start_angle=result["theta"],
                speed=result["speed"],
                joints={int(k): np.array(v) for k, v in result["joints"].items()},
                fixed_joints=set(result.get("fixed_joints", [])),
                rods=[tuple(pair) for pair in result["rods"]]
            )
        except Exception as e:
            st.sidebar.error(f"Fehler beim Laden des Mechanismus: {e}")
            return None
    else:
        st.sidebar.error("Mechanismus nicht gefunden.")
        return None

def get_all_mechanism_names():
    return [entry["name"] for entry in db.all()]
