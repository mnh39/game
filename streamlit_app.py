import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Bookr: The Daily Book Guessing Game',
    page_icon=':books:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
#Book of the day info
title_real = "Project Hail Mary"
title = "project hail mary"
genre = "science fiction"
year = "2022"
language = "English"
author = "Andy Weir"

#Score
score = 1

#Welcome
print(f"Welcome to Bookr! The daily game that tests your book knowledge. \nWe'll give you a hint to help you guess, but if you don't get it right on the first try don't worry! You'll have four chances to guess the book of the day!\n\nHappy Guessing!")

#Game
#Hint 1: Genre
print(f"\nThis book is classified as", genre)
answer=input(f"\nGuess: ")
answer=answer.lower()

if answer == title:
   print(f"Congratulations! You guessed it in {score}!")
#Hint 2: Year
else:
    print (f"\nSorry, that's incorrect.")
    score = score +1
    print (f"This book was published in {year}")
    answer = input(f"\nGuess: ")
    answer = answer.lower()
    if answer == title:
        print(f"Congratulations! You guessed it in {score}")
    else:
#Hint 3 Language
        score = score +1
        print (f"\nSorry, that's incorrect.")
        print (f"This book was published in {language}")
        answer = input(f"\nGuess: ")
        answer = answer.lower()
        if answer == title:
             print(f"Congratulations! You guessed it in {score}")
        else:
#Hint 4 Author
            score = score + 1
            print (f"\nSorry, that's incorrect.")
            print (f"This book was written by {author}")
            answer = input(f"\nGuess: ")
            answer = answer.lower()
            if answer == title:
                print(f"Congratulations! You guessed it in {score}")
            else:
                print(f"Better luck next time! The answer was {title_real}")