# -*- coding: utf-8 -*-
"""
       (`-()_.-=-.
       /66  ,  ,  \
     =(o_/=//_(   /======`
         ~"` ~"~~`        C.E.
         
Created on Wed Aug 12 14:20:56 2020
@author: Chris
Contact :
    Christopher.eaby@gmail.com
"""
import pymongo #mongodb module
import tkinter as tk #gui
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
import folium
import webbrowser

'''
#creates mongodatabase and the collections
myclient = pymongo.MongoClient("mongodb+srv://Chris:pass1234@cluster0.whwc8.mongodb.net/test")
mydb = myclient["CovidCases"]
act = mydb["Cases"]
df = pd.DataFrame(list(act.find()))
'''

data = pd.read_csv("Data_ WHO Coronavirus Covid-19 Cases and Deaths - WHO-COVID-19-global-data.csv")
datafr = pd.DataFrame(data = data)

def makeitdostuff(vari):
    data = pd.read_csv("Data_ WHO Coronavirus Covid-19 Cases and Deaths - WHO-COVID-19-global-data.csv")
    datafr = pd.DataFrame(data = data)
    df_new = datafr[datafr['COUNTRY_NAME'] == vari]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,10))
    fig.suptitle(vari)
    ax1.plot(df_new['Date_epicrv'].str[5:10],df_new['TotalCase'], 'tab:green')
    ax1.set_title('Confirmed Cases')
    ax2.plot(df_new['Date_epicrv'].str[5:10],df_new['TotalDeath'], 'tab:red')
    ax2.set_title('Confirmed Deaths')

    n1 = 2
    for n, label in enumerate(ax1.yaxis.get_ticklabels()):
        if n % n1 != 0:
            label.set_visible(False)       
    for n, label in enumerate(ax2.yaxis.get_ticklabels()):
        if n % n1 != 0:
            label.set_visible(False)
    n1 = 10
    for n, label in enumerate(ax1.xaxis.get_ticklabels()):
        if n % n1 != 0:
            label.set_visible(False)
    for n, label in enumerate(ax2.xaxis.get_ticklabels()):
        if n % n1 != 0:
            label.set_visible(False)

gui = tk.Tk()
# sets the title 
gui.title("Covid-19 graphing")
# sets the size
gui.geometry("220x120")

# creates text field for data input
txt = tk.Text(gui, fg = "white", bg = "purple", height = 1, width = 15)
# griding for the text field
txt.grid(row = 1, column = 0)
lbl2 = tk.Label(gui, text = "Search", justify = tk.CENTER, padx = 30, pady = 10)
# creates a label to show what the text field is for
lbl2.grid(row = 0, column = 1)
b2 = tk.Button(gui, text = "Search", height = 2, width = 9, command = lambda: makeitdostuff(str(txt.get("1.0","end")[:-1])))
b2.grid(row = 1, column = 1) 

gui.mainloop()
country_geo = 'world-countries.json'

map = folium.Map(location = [0, 0], zoom_start = 1)

map.choropleth(geo_data = country_geo, 
               data = datafr,
               columns= ['ISO_CODE', 'TotalCase'],
               key_on='feature.id',
               fill_color='YlGnBu', fill_opacity=0.7,
               line_opacity=0.2)

map.save('plot_data.html')
new = 2
webbrowser.open('plot_data.html', new = new)