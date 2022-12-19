import streamlit as st
import pandas as pd
import plotly.express as px

################ Model ################
class Model:
    '''
    Class representing the data
    '''
    
    header = 'Global Statistics from Gapminder'
    description ='''
        See how life expectancy changes over time and in relation to GDP.
        Move the slider to change the year to display.
    '''
    sliderCaption="Select the year for the chart"
    x = 0
    
    def __init__(self):
        
        # for the dashboard
        self.df = pd.DataFrame(px.data.gapminder())
        self.clist = self.df['country'].unique() 
        self.ylist = [int(i) for i in self.df['year'].unique()] # convert to int
        self.yearStart = self.ylist[0]
        self.yearEnd = self.ylist[-1]
        self.yearStep = self.ylist[1]-self.ylist[0]
        
        # for the page 2
        self.var_x = -11
        
        
    def chart(self,year):
        return px.scatter(
            self.df[self.df['year'] == year], 
            x = 'lifeExp', y = 'gdpPercap', title = f'Year: {year}',
            color='continent',size='pop')
        
    