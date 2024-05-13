import requests
from bs4 import BeautifulSoup
import re
import random
from tkinter import *
#import customtkinter
def scraper():
    text_list = []
    # URL of the Wikipedia article
    url = "https://en.wikipedia.org/wiki/List_of_generic_forms_in_place_names_in_the_British_Isles"

    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table with the class "wikitable" on the page
    table = soup.find("table", class_="wikitable")

    # Extract the text from the first column (index 0) of each row in the table
    rows = table.find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        if len(cells) > 0:
            first_column_text = cells[0].get_text(strip=True)
            
            # Remove numbers from the extracted text using regular expressions
            text_without_numbers = re.sub(r'\d+', '', first_column_text)
            text_without_brackets = re.sub(r'\[.?\]', '', text_without_numbers)
            
            # Split the text on commas and add individual elements to the list
            text_list.extend(text_without_brackets.split(','))
    
    return text_list
text_list = scraper()

def combiner(text_list):
   #prompt = int(input("select the number of names you want to generate: "))
    num = 0
    townName = ''
    while num < 2:
        seedValue = random.randint(0, 248)
        x = text_list[seedValue]
        townName += x
        num += 1
    print(townName)
    return townName

def add_value():
    townName = combiner(text_list)
    interface_list.delete(0, END)
    interface_list.insert(END, townName)


app = Tk()
interface_button = Button(app, text='Generate name', width=12, command=add_value)
#interface_button.grid(row=2, column=3, pady=20)
interface_button.pack()

app.title("EnglishTownNameGenerator")
app.geometry('250x250')

interface_list = Listbox(app, height=4, width=20)
#interface_list.grid(row=3, column=2, columnspan=2, rowspan=3, pady=80, padx=20)
interface_list.pack()


    


app.mainloop()






