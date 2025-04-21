#MapPlot.py
#Name:
#Date:
#Assignment:

# MapPlot.py
# Name: [Your Name]
# Date: [Today's Date]
# Assignment: Lab 10 - Visualizations with Matplotlib

import coffee  # type: ignore
import pandas as pd
import matplotlib.pyplot as plt

# Get the coffee data from the CORGIS dataset
coffee = coffee.get_coffee()

# Create empty lists to store years and scores
years = []
scores = []

# Loop through the coffee data
for bean in coffee:
    year = bean["Year"]
    score = bean["Data"]["Scores"]["Total"]
    
    # Clean the data: only include scores that are not zero
    if score != 0:
        years.append(year)
        scores.append(score)  # <-- this was the main fix!

# Create a DataFrame from the lists
df = pd.DataFrame({
    "Year": years,
    "Score": scores
})

# Print the DataFrame to check the data
print(df)

# Create a basic line plot using Matplotlib
plt.plot(years, scores, marker='o')  # <-- changed marker from '0' to 'o' (zero vs letter O)
plt.xlabel("Year")  # <-- fixed from clabel to xlabel
plt.ylabel("Score")
plt.title("Coffee Bean Scores Over the Years")

# Save the plot to a file
plt.savefig("output.png")  # <-- fixed spelling "output" to "output.png"

# Show the plot
plt.show()
