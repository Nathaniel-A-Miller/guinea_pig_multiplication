import streamlit as st
import scenes

st.title("The Pigs of Destiny")

# Initialize state
if "scene" not in st.session_state:
    st.session_state.scene = "intro"
if "character_name" not in st.session_state:
    st.session_state.character_name = ""

# Map scene names to functions
SCENES = {
    "intro": scenes.intro,
    "encounter": scenes.encounter,
    "door_puzzle": scenes.door_puzzle,
    "home": scenes.home,
    "bedtime": scenes.bedtime,
    "door_puzzle": scenes.door_puzzle,
    "two_rooms": scenes.two_rooms,
    "left_door": scenes.left_door,
    "right_door": scenes.right_door,
    "left_door_2": scenes.left_door_2,
    "loss_1": scenes.loss_1,
    "neighbor": scenes.neighbor,
    "loss_2": scenes.loss_2,
    "right_door_2": scenes.right_door_2,
    "chest": scenes.chest,
    "loss_3": scenes.loss_3,
    "hogback_1": scenes.hogback_1,
    "hogback_2": scenes.hogback_2,
    "cave_entrance": scenes.cave_entrance,
    "warlock_1": scenes.warlock_1,
    "warlock_2": scenes.warlock_2,
    "warlock_3": scenes.warlock_3,
    "loss_4": scenes.loss_4,
    "victory": scenes.victory
}

# Run the current scene
current_scene_name = st.session_state.scene
SCENES[current_scene_name]()

