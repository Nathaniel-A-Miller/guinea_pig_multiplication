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
            {char} was walking home from the bus stop one day when a guinea pig appeared
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
            surrounded by a thick cluster of pine trees.
            
            "Funny, {char} thought, "I've never noticed that building before."
            
            The guinea pig slipped through a crack in the door and disappeared.

            {char} went home and their dad made them do their homework.

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
            {char} kept walking on the sidewalk. The guinea pig scurried into a dark building
            surrounded by a thick cluster of pine trees.
            
            "Funny, {char} thought, "I've never noticed that building before."
            
            The guinea pig slipped through a crack in the door and disappeared.
            
            {char} approached the door. It was locked. On it was written:
            """)
    st.latex(r"12 \times 5 = ?")
    st.write("What's the answer")
    answer = st.number_input("Enter your answer", value=0, step=1, key="door")
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

            Inside {char} found the pink guinea pig with two other pigs, a brown and a black one.
            
            "What are you doing in here?" the pink pig asked. "How did you find us."

            {char} hesitated. "My name is {char}."

            "Maybe {char} can help us," the brown pig asked. "If they know math magic."

            "Let's test {char}", the black pig said.

            They all looked at {char} who shifted from side to side nervously.

            "Ok," the pink pig said. "What's the answer to"
            """)
    st.latex(r"12 \times 10 = ?")
    answer = st.number_input("Enter your answer", value=0, step=1, key="left door")
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
            "{char} understands math magic," the pink pig said. "My name is Thunderbolt. Welcome."

            "And I am Lady Nibbles," the brown pig said. "We are going to slay an evil warlock 
            who eats guinea pigs."
              
            "But first," said the black pig, whose name was Flash, "we must steal back the Sword
            of Destiny from one of our neighbors. Have you met Warrior Pig yet? He will use the Sword
             to defeat the warlock.
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

            "I am Warrior Pig," he said as he came to rest. "If you do not answer the following question
            I will use you for target practice."
            """)
    st.latex(r"12 \times 2 = ?")
    answer = st.number_input("Enter your answer", value=0, step=1, key="right door")
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
    char = st.session_state.character_name
    st.write(f"""
            {char}, Warrior Pig, Thunderbolt, Lady Nibbles, and Flash left the house and made their
            way down the street.

            "A local thug has stolen my Sword of Destiny and hid it in their basement," Warrior Pig said.

            "We're going to steal it back," Lady Nibbles said.

            They came to the house and snuck around the back. Thunderbolt stuck his long front teeth into
            a lock in the basement door and it popped open.

            Suddently a blond boy leapt out and said, "hey, stay out of my basement."

            "Quick!" Flash said, "I'll use a magic spell on him." {char} what's 
            """)
    st.latex(r"12 \times 3 = ?")
    answer = st.number_input("Enter your answer", value=0, step=1, key="neighbor")
    if st.button("Confirm answer"):
        if answer == 36:
            st.session_state.scene = "chest"
            st.rerun()
        else:
            st.session_state.scene = "loss_3"
            st.rerun()

def chest():
    char = st.session_state.character_name
    st.write(f"""
            Flash's magic worked and the big blond boy folded unconscious. 

            {char}, Warrior Pig, Thunderbolt, Lady Nibbles, and Flash made their way into the basement.

            There they found a large chest. 

            "This must be where he put the sword," Lady Nibbles said. She looked at the chest carefully.

            What's
            """)
    st.latex(r"12 \times 12 = ?")
    answer = st.number_input("Enter your answer", value=0, step=1, key="chest")
    if st.button("Confirm answer"):
        if answer == 144:
            st.session_state.scene = "hogback_1"
            st.rerun()
        else:
            st.error("The chest remains locked.")

def loss_3():
    st.write("""
            The spell failed and the big blond boy came storming through them, kicking
            guinea pigs left and right. 

            "We're done for!" Warrior Pig shouted. "Save yourselves!"
             
            THE END
            """)

def hogback_1():
    char = st.session_state.character_name
    st.write(f"""
            {char} and the pigs left the house with the sword and walked along until they came to a path.
            The path led down a slope, crossed a road, and then went up into some grasslands heading into
            the foothills. 

            They came to the foot of a particularly steep foothill.

            "This is where the warlock lives: up this slope, over the summit, in a cave on the other
            slope," Lady Nibbles said.

            Suddenly a fierce mountain goat leapt out in front of them.

            "Answer this to pass!" it bleated.
            """)
    st.latex(r"12 \times 4 = ?")
    answer = st.number_input("Enter your answer", value=0, step=1, key="goat")
    if st.button("Confirm answer"):
        if answer == 48:
            st.session_state.scene = "hogback_2"
            st.rerun()
        else:
            st.error("The goat head butts you.")

def hogback_2():
    char = st.session_state.character_name
    st.write(f"""
            As they appraoched the summit, they found a badly injured mountain biker collapsed
             in a heap beside his twisted bike.

            "I fell down the mountain," he said. "Help me call my wife. I can't unlock my phone.
             The password is"
            """)
    st.latex(r"12 \times 11 = ?")
    answer = st.number_input("Enter your answer", value=0, step=1, key="biker")
    if st.button("Confirm answer"):
        if answer == 132:
            st.session_state.scene = "cave_entrance"
            st.rerun()
        else:
            st.error("The phone doesn't unlock. Try again.")

def cave_entrance():
    char = st.session_state.character_name
    st.write(f"""
            They came to the summit where they had a magnificient view of everything around them.
             
            To the west, further mountains continued shrouded in mist as far as their eyes could see.
             To the east, there were vast plains and they could see {char}'s neighborhood.

            The continued down the other slope a short way and came to the warlock's cave.

            A forcefield blocked their way!

            Flash searched around, snuffling with his nose, and overturned a rock. Beneath it was 
            written 
            """)
    st.latex(r"12 \times 6 = ?")
    answer = st.number_input("Enter your answer", value=0, step=1, key="cave")
    if st.button("Confirm answer"):
        if answer == 72:
            st.session_state.scene = "warlock_1"
            st.rerun()
        else:
            st.error("The forcefield remains in place.")

def warlock_1():
    char = st.session_state.character_name
    st.write(f"""
            They wound their way deep into the cave, which was made of swirly brownish-gray gneiss. Water
             dripped from the roof of the cave.

            Suddenly they came into a larger cavern. There was the warlock, just about to eat another
             guinea pig! He was dressed in a purple robe and had white hair. When he saw them enter,
             he dropped the pig, which squealed and ran behind {char}.

            Warrior Pig stepped in front, wielding the Sword of Destiny.

            "We are the Pigs of Destiny, vile warlock! Your reign of terror is over!"

            The warlock cast a spell and a crack appeared in Warrior Pig's sword.

            "Quick," Thunderbolt said, "what's"
            """)
    st.latex(r"12 \times 9 = ?")
    answer = st.number_input("Enter your answer", value=0, step=1, key="broken sword")
    if st.button("Confirm answer"):
        if answer == 108:
            st.session_state.scene = "warlock_2"
            st.rerun()
        else:
            st.session_state.scene = "loss_4"

def loss_4():
    char = st.session_state.character_name
    st.write("""
            With Warrior Pig's sword broken, everyone fled. The warlock chased after them,
             hurling spells. Most of them made it, but {char} has a burn mark on their elbow 
             from a spell. It seemed that the warlokc's reign of terror would not end today.

             THE END
            """)
    
def warlock_2():
    char = st.session_state.character_name
    st.write(f"""
            The math magic sealed up the crack in the Sword of Destiny.
             
            Warrior Pig began bashing the warlock over the head with the Sword of Destiny but some 
             spell was protecting the warlock. Warrior Pig bashed and bashed until the warlock was
             on his knees.

            Suddenly the Sword of Destiny shattered into hundreds of pieces. No magic could restore it.
             
            The warlock stood, wobbly, to his feet.

            "Quick," Thunderbolt said, "we can cast a spell directly against him!"
            """)
    st.latex(r"12 \times 7 = ?")
    answer = st.number_input("Enter your answer", value=0, step=1, key="second spell")
    if st.button("Confirm answer"):
        if answer == 84:
            st.session_state.scene = "warlock_3"
            st.rerun()
        else:
            st.session_state.scene = "loss_4"

def warlock_3():
    char = st.session_state.character_name
    st.write(f"""
            "One more," Lady Nibbles yelled!"
            """)
    st.latex(r"12 \times 8 = ?")
    answer = st.number_input("Enter your answer", value=0, step=1, key="last spell")
    if st.button("Confirm answer"):
        if answer == 96:
            st.session_state.scene = "victory"
            st.rerun()
        else:
            st.session_state.scene = "loss_4"

def victory():
    char = st.session_state.character_name
    st.image("victory.png", use_container_width = True)
    st.write(f"""
            In a flash the warlock vanished!

            "We did it!" Lady Nibbles yelled. 
            
            {char} and all the guinea pigs hugged.
             
            The guinea pigs of world were safe once more.
             """)