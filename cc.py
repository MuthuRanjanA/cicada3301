import streamlit as s
from PIL import Image
s.set_page_config(page_title="CICADA_3301")
s.header("")
s.write("""# Greetings

We are looking for highly intelligent individuals.To find them, we have devised a test.

There is a message hidden within this webpage.You will not find it by merely reading the text.Look closer, think deeper, and question everything.The path to enlightenment is not straight and obvious.Instead, it is a labyrinth that requires a sharp mind to navigate.

Should you succeed in uncovering the truth hidden in plain sight, you will have taken the first step towards a larger world, where the pursuit of knowledge reigns supreme.

We look forward to meeting the few who will make it all the way through.

Good luck.

3301""")
s.write("___")
s.write("""_IF YOU WANT THE ANSWER FOR THE EVENT , ANSWER THE QUESTION_""")
c1,c2=s.columns(2)
with c1:
    a1=s.number_input("what is the value of pi with 2 floating point?")
with c2:
    a2=s.number_input("what is the value of phi with 2 floating point?")
if (a1==3.14) and (a2==1.62):
    s.write("congratulations;")
    #code for image
    col1,col2,col3=s.columns(3)
    with col1:
        s.write("")
    with col2:
        img = Image.open("cc.jpg")
        s.image(img,caption="Find me")
    with col3:
        s.write("")

else:
    s.write("Answer is wrong , please refresh the page and continue")
