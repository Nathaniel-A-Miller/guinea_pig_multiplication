import streamlit as st

def intro():

    st.image("intro_image.png", use_container_width=True)

    st.write("Hi there. I have a story to tell you and you're part of the story!")
    name = st.text_input("What's your name?")
    if st.button("That's my name, don't wear it out"):
        if name:
            st.session_state.character_name = name
            st.session_state.scene = "encounter"
            st.rerun()
        else:
            st.warning("Please enter a name first!")

def encounter():
    char = st.session_state.character_name
    st.write (f"""
            {char} was walking home from the bus stop one day when he saw a guinea pig 
            on the sidewalk. That was strange enough, but the guinea pig was also entirely,
            completely pink!

            As {char} approached, the guinea pig started to run away.

            Do you follow it?
            """)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes, follow it!"):
            st.session_state.scene = "door_puzzle"
            st.rerun()

    with col2:
        if st.button("No, let's go home"):
            st.session_state.scene = "home"
            st.rerun()

def home():
    char = st.session_state.character_name
    st.write (f"""
            {char} kept walking on the sidewalk. The guinea pig scurried into a dark building
            surrounded by a thick cluster of pine trees {char} had never noticed before between
            two houses. It slipped through a crack in the door and disappeared.

            {char} went home and his dad made him do his homework.

            Do you want to tell your dad what happened and go back to the mysterious building?
            Or play games until dinner and then go to bed?
            """)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Tell dad about the pig!"):
            st.session_state.scene = "door_puzzle"
            st.rerun()

    with col2:
        if st.button("Play games until bed"):
            st.session_state.scene = "bedtime"
            st.rerun()

def bedtime():
    st.write("""
            You play games until dinner and then get ready for bed.
            
            THE END
            """)            

def door_puzzle():
    char = st.session_state.character_name
    st.write(f"""
            {char} had seen the guinea pig scurry into a dark building
            surrounded by a thick cluster of pine trees {char} had never noticed
            before between two houses. It had slipped through a crack in the door
            and disappeared.
            
            {char} approached the door. It was locked. On it was written:
            """)
    st.latex(r"12 \times 5 = ?")
    st.write("What's the answer")
    answer = st.number_input("Enter your answer", value=0, step=1)
    if st.button("Confirm answer"):
        if answer == 60:
            st.session_state.scene = "two_rooms"
            st.rerun()
        else:
            st.error("The door remains locked.")

def two_rooms():
    char = st.session_state.character_name
    st.write (f"""
            The door creaked open and {char} walked in slowly. 

            {char} was in an empty room with two doors. Which one do you take?
            """)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Left door"):
            st.session_state.scene = "left_door"
            st.rerun()

    with col2:
        if st.button("Right door"):
            st.session_state.scene = "right_door"
            st.rerun()

def left_door():
    char = st.session_state.character_name
    st.write(f"""
            {char} entered the left door.

            Inside he found the pink guinea pig with two other pigs, a brown and a black one.
            
            "What are you doing in here?" the pink pig asked. "How did you find us."

            {char} hesitated.

            "Maybe he can help us," the brown pig asked. "If he knows math magic."

            "Let's test him", the black pig said.

            They all looked at {char} who shifted from side to side nervously.

            "Ok," the pink pig said. "What's the answer to"
            """)
    st.latex(r"12 \times 10 = ?")
    answer = st.number_input("Enter your answer", value=0, step=1)
    if st.button("Confirm answer"):
        if answer == 120:
            st.session_state.scene = "left_door_2"
            st.rerun()
        else:
            st.session_state.scene = "loss_1"
            st.rerun()

def left_door_2():
    char = st.session_state.character_name
    st.write(f"""
            "He understands math magic," the pink pig said. "My name is Thunderbolt. Welcome."

            "And I am Lady Nibbles," the brown pig said. "We are going to slay an evil warlock 
            who eats guinea pigs."
              
            "But first," said the black pig, whose name was Flash, "we must steal back the Sword
            of Destiny from one of our neighbors. Have you met Warrior Pig yet? He 
            """)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes I've met him already"):
            st.session_state.scene = "neighbor"
            st.rerun()

    with col2:
        if st.button("No not yet"):
            st.session_state.scene = "right_door"
            st.rerun()

def loss_1():
    st.write("""
            The guinea pigs jump onto your face scratching at you until you
            until you escape the building and run home.
             
            The next day you look for their building among the pine trees but 
            you can't find it anywhere.
             
            THE END
            """)

def right_door():
    char = st.session_state.character_name
    st.write(f"""
            {char} entered the right door and was almost hit in the head by a very furry guinea pig
            performing karate kicks and punches.

            "I am warrior pig," he said as he came to rest. "If you do not answer the following question
            I will use you for target practice."
            """)
    st.latex(r"12 \times 2 = ?")
    answer = st.number_input("Enter your answer", value=0, step=1)
    if st.button("Confirm answer"):
        if answer == 24:
            st.session_state.scene = "right_door_2"
            st.rerun()
        else:
            st.session_state.scene = "loss_2"
            st.rerun()

def loss_2():
    st.write("""
            Warrior Pig performs a flurry of kicks and punches so fast you are unconscious before you
            realize it.
             
            THE END
            """)

def right_door_2():
    char = st.session_state.character_name
    st.write(f"""
            "Well done. You are worthy of respect!" Warrior Pig said.
             
            "Have you met Thunderbolt, Lady Nibbles, and Flash yet?"
            """)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes I've met them already"):
            st.session_state.scene = "neighbor"
            st.rerun()

    with col2:
        if st.button("No not yet"):
            st.session_state.scene = "left_door"
            st.rerun()

def neighbor():
    st.write("under construction")

