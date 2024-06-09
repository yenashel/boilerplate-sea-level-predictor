import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
   

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x1 = range(df["Year"].min(),2051,1) #create x values from the start of actual data to the point I want to predict. It needs to be 2051 to deal with the correct number of values in the test file
    y1 = x1 * slope + intercept

    plt.plot(x1, y1, 'r', label='first line')

    # Create second line of best fit
    df2=df[df["Year"]>=2000]

    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df2["Year"], df2["CSIRO Adjusted Sea Level"])

    x2 = range(2000,2051,1) #create x values from the start of actual data to the point I want to predict
    y2 = x2 * slope2 + intercept2

    plt.plot(x2, y2, "y", label="second line")


    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()