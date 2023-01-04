import pandas as pd

# Data Visualization
# EDA: exploratory data analysis 
# getting ready to your data
# exploring data, visualizing data, mining data (looking for patterns, groups, outliers, associations, etc.)

# Goal of data visualization
# 1. CLearly and accurately represent data
# 2. be creative with the goal of increasing understanding
# 3. label units and points of interests

# Some jargon
# chart: a 2D visualization
# plot: a chart of 2D visualization of data points (e.g. scatter plot)
# graph: a chart of a math function (e.g. sine)

# We are going to use matplotlib library, which is already included in anaconda
# 3 way to use matplotlib
# 1. using the pyplot submodule
import matplotlib.pyplot as plt
# note: there is always a "current figure"
# 2. using the OOP (object-oriented programming) interface
# 3. a mix of both

# Lots of ways to customize. Read the documentations!

# Let's start with a simple line chart
def line_chart_ex (x, y, y2, filename):
    # x and y are "sequences"
    # lists, series, numpy array, etc.
    # they are parralel
    plt.plot(x, y, label="PTS", color="purple")
    plt.plot(x, y2, label="MIN")

    # TODO: fix bad x tick label
    # Let's beautify the plot
    plt.xticks(rotation=45, ha="right") # ha is horizontal alignment
    plt.xlabel("Player")
    plt.ylabel("Season Point Total")
    plt.title("Gonzaga Men Bulldog Stat 2021 - 2022")
    plt.grid()
    plt.legend() # to show the legend in the graph

    plt.tight_layout() # if called before plt.show() or plt.savefig(), it will fix the wrapping issue
    
    # 3 ways to "show" the chart
    # 1. plt.show()
    # plt.show() # show as an interactive window
    # 2. plt.savefig()
    plt.savefig(filename)
    # 3. inline inside of a jupyter notebook. More on this later

def scatter_chart_example(x, y, filename):
    plt.figure() # create a new *current figure*
    plt.scatter(x, y)
    plt.savefig(filename)

def bar_chart_example(x, y, filename):
    plt.figure() # create a new *current figure*
    plt.bar(x, y)
    plt.savefig(filename)

def pie_chart_example(labels, values, filename):
    plt.figure() # create a new *current figure*
    plt.pie(values, labels=labels, autopct="%1.1f%%") # rounding
    plt.savefig(filename)

def histogram_chart_example(values, filename):
    # default number of bin is 10
    # uniform distribution: when the counts (y-axis) is identical
    plt.figure() # create a new *current figure*
    plt.hist(values, bins=5, edgecolor="black")
    plt.savefig(filename)

def main():
    data = pd.read_csv("bball.csv", index_col="NAME")

    new_row_df = pd.DataFrame([["G",12,20,1]], columns=data.columns, index=["Joe Few"])
    new_row_df.index.name = data.index.name
    df = pd.concat([data, new_row_df])
    print(data)

    data["CLASS"] = ["Sr", "Jr", "Fr", "Fr", "Jr", "Fr", "So", "Fr", "Jr", "Sr", "Fr", "Sr", "Sr", "Fr"]
    print(data)

    class_count_series = data["CLASS"].value_counts()
    print(class_count_series)

    grouped_by_class = data.groupby("CLASS")
    mean_pts_series = grouped_by_class["PTS"].mean()

    ppg_series = data["PTS"] / data["GP"]
    print(ppg_series[ppg_series == ppg_series.max()]) # a boolean series

    # OR
    max_position = ppg_series.argmax()
    print(ppg_series.index[max_position])

    # task: add another line in the chart for minutes played
    line_chart_ex(data.index, data["PTS"], data["MIN"], "line_example.png")
    scatter_chart_example(data.index, data["PTS"], "scatter_example.png")
    # bar_chart_example(data.index, data["PTS"], "bar_example.png")
    bar_chart_example(class_count_series.index, class_count_series, "bar_example.png")
    # pie chart: great for showing parts of a whole
    pie_chart_example(class_count_series.index, class_count_series, "pie_example.png")
    histogram_chart_example(data["PTS"], "histogram_example.png")

main()