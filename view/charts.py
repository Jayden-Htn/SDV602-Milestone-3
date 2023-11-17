"""
Chart Examples in matplotlib
This set of examples comes from https://www.python-course.eu/matplotlib_overview.php
"""


# Imports
import sys
sys.dont_write_bytecode = True
import matplotlib.pyplot as plt
import numpy as np


# Procedures
def line_plot(**kwargs):
    """
    Automagically takes a list of Y values (data) and figures out the X axis.
    As a continuous graph.

    Args 
          **kwargs lets you pass arguments into this function 
    """
    x_label = 'Day'
    y_label = 'Temperature in Celsius'
    title_label = 'Temperature Graph'
    x_values = range(1, 9)
    y_values = [25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]
    zoom = 0
    pan = 1

    if 'x_label' in kwargs :
        x_label = kwargs['x_label']
    if 'y_label' in kwargs :
        y_label = kwargs['y_label']
    if 'title_label' in kwargs :
        title_label = kwargs['title_label']
    if 'x_values' in kwargs :
        x_values = kwargs['x_values']
    if 'y_values_1' in kwargs :
        y_values = kwargs['y_values_1']
    if 'zoom' in kwargs :
        zoom = kwargs['zoom']
    if 'pan' in kwargs :
        pan = kwargs['pan']

    # Create separate smaller tick list to avoid overlapping labels
    x_ticks = x_values
    y_ticks = y_values
    if len(x_values) > 10:
        num = round(len(x_values)/6)
        x_ticks = x_values[::num]
    if len(y_values) > 10:
        num = round(len(y_values)/10)
        y_ticks = y_values[::num]

    # Create chart
    ax = plt.plot(x_values, y_values)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title_label)
    plt.xticks(x_ticks)
    plt.yticks(y_ticks)
    plt.margins(zoom)

    return plt.gcf()


def discrete_plot(**kwargs):
    """
    Plot format, sets marker in place of a continuous line. 

    Args 
          **kwargs lets you pass arguments into this function
    """
    x_label = 'Day'
    y_label = 'Temperature in Celsius'
    title_label = 'Temperature Graph'
    x_values = range(1, 9)
    y_values = [25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]

    if 'x_label' in kwargs :
        x_label = kwargs['x_label']
    if 'y_label' in kwargs :
        y_label = kwargs['y_label']
    if 'title_label' in kwargs :
        title_label = kwargs['title_label']
    if 'x_values' in kwargs :
        x_values = kwargs['x_values']
    if 'y_values' in kwargs :
        y_values = kwargs['y_values']

    fig, ax = plt.subplots() # Challenge - Why "fig" here"

    ax.plot(x_values, y_values)
    ax.set(xlabel=x_label,
        ylabel=y_label,
        title=title_label)

    #plt.show()
    return plt.gcf()


def names_labels(**kwargs):
    """
    This gets an Axes object

    X axis(days), Y axis (celsius_values)

    Args 
          **kwargs lets you pass arguments into this function
    """
    x_label = 'Day'
    y_label = 'Temperature in Celsius'
    title_label = 'Temperature Graph'
    x_values = range(1, 9)
    y_values = [25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]

    if 'x_label' in kwargs :
        x_label = kwargs['x_values']
    if 'y_label' in kwargs :
        y_label = kwargs['y_label']
    if 'title_label' in kwargs :
        title_label = kwargs['title_label']
    if 'x_values' in kwargs :
        x_values = kwargs['x_values']
    if 'y_values' in kwargs :
        y_values = kwargs['y_values']

    fig, ax = plt.subplots() # Challenge - Why "fig" here"

    ax.plot(x_values, y_values)
    ax.set(xlabel=x_label,
        ylabel=y_label,
        title=title_label)
    # See kwargs here https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html

    #plt.show()
    return plt.gcf()


def multiple_plots(**kwargs):
    """
    Plot more than one on a single graph
    Args 
          **kwargs lets you pass arguments into this function
    """
    x_label = 'Day'
    y_label = 'Temperature in Celsius'
    title_label = 'Temperature Graph'

    x_values = list(range(1, 9))
    y_values_1 = [19.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]
    y_values_2 = [24.8, 28.9, 31.3, 33.0, 34.9, 35.6, 38.4, 39.2]

    if 'x_label' in kwargs:
        x_label = kwargs['x_label']
    if 'y_label' in kwargs:
        y_label = kwargs['y_label']
    if 'title_label' in kwargs:
        title_label = kwargs['title_label']
    if 'x_values' in kwargs:
        x_values = kwargs['x_values']
    if 'y_values' in kwargs:
        y_values_1 = kwargs['y_values']
        y_values_2 = [str(int(y)+1) for y in y_values_1]
        # Note: this will currently only accept one y value set through kwargs
        # as the testing data only has one set of y values

        # y_values_1 = [int(y) for y in y_values_1]
        # y_values_2 = [int(y) for y in y_values_2]

        # y_values_1 = [str(y) for y in y_values_1]
        # y_values_2 = [str(y) for y in y_values_2]

        # Note: drastically different output depending on data type

    fig, ax = plt.subplots()

    ax.set(xlabel=x_label,
        ylabel=y_label,
        title=title_label)

    ax.plot(x_values, y_values_1) # Draws lines between points
    ax.plot(x_values, y_values_1, "oy") # Draws yellow circles at points
    ax.plot(x_values, y_values_2) # Draws lines between points
    ax.plot(x_values, y_values_2, "or") # Draws red circles at points

    # Short hand version in one call to plot
    # ax.plot(days, celsius_min,
    #   days, celsius_min, "oy",
    #   days, celsius_max,
    #   days, celsius_max, "or")
    return plt.gcf()


def bar_chart(**kwargs):
    """
    An example of a bar chart

    Args 
          **kwargs lets you pass arguments into this function
    """
    x_values = [str(year) for year in range(2010, 2021)]
    y_values = [1241, 50927, 162242, 222093, 
                665004, 2071987, 2460407, 3799215, 
                5399000, 5474016, 6003672]
    
    x_label = 'Year'
    y_label = 'Number of Users'
    title_label = 'Bar Chart Example'

    if 'x_label' in kwargs:
        x_label = kwargs['x_label']
    if 'y_label' in kwargs:
        y_label = kwargs['y_label']
    if 'title_label' in kwargs:
        title_label = kwargs['title_label']
    if 'x_values' in kwargs:
        x_values = kwargs['x_values']
    if 'y_values' in kwargs:
        y_values = kwargs['y_values']

    plt.bar(x_values, y_values, color="green")

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title_label)

    plt.plot()
     
    return plt.gcf()


def histogram(**kwargs):
    """
    An example of a histogram
    Uses numpy as np to get a list of values in a random range - Gaussian

    Args 
          **kwargs lets you pass arguments into this function

          This includes an example of how to change the plt 'title' by looking for it in **kwargs.
    """
    y_values = np.random.normal(size=10000)
    x_label = 'Value'
    y_label = 'Frequency'
    title_label = 'Gaussian Histogram'

    if 'x_label' in kwargs:
        x_label = kwargs['x_label']
    if 'y_label' in kwargs:
        y_label = kwargs['y_label']
    if 'title_label' in kwargs:
        title_label = kwargs['title_label']
    if 'y_values' in kwargs:
        y_values = kwargs['y_values']
    
    
    plt.hist(y_values, bins=20)
    
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    #plt.show()
    return plt.gcf()


def scatter_plots(**kwargs):
    """
    Three Scatter plots over a range.
    Uses numpy as np.

    Args 
          **kwargs lets you pass arguments into this function
    """
    x_values = np.arange(0, 11)
    y1 = np.random.randint(2, 7, (11,))
    y2 = np.random.randint(9, 14, (11,))
    y3 = np.random.randint(15, 25, (11,))
    x_label = 'Value'
    y_label = 'Frequency'
    title_label = 'Scatter Plot'

    if 'x_label' in kwargs:
        x_label = kwargs['x_label']
    if 'y_label' in kwargs:
        y_label = kwargs['y_label']
    if 'title_label' in kwargs:
        title_label = kwargs['title_label']
    if 'x_values' in kwargs:
        x_values = kwargs['x_values']
    if 'y_values' in kwargs:
        y1 = kwargs['y_values']
        y2 = [str(int(y)+20) for y in y1]
        y3 = [str(int(y)+40) for y in y1]

        # y1 = [int(y) for y in y1]
        # y2 = [int(y) for y in y2]
        # y3 = [int(y) for y in y3]

        y1 = [str(y) for y in y1]
        y2 = [str(y) for y in y2]
        y3 = [str(y) for y in y3]
        # Different data type drastically changes the output?????

    plt.scatter(x_values, y1)
    plt.scatter(x_values, y2, marker='v', color='r')
    plt.scatter(x_values, y3, marker='^', color='m')
    plt.title(title_label)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    #plt.show()
    return plt.gcf()


def stack_plot(**kwargs):
    """
    Stack plot with three lists of values.

    Args 
          **kwargs lets you pass arguments into this function   
    """
    x_values = [ 1,  2,  3,  4,  5,  6,  7,  8,  9]
    y1  = [23, 42, 33, 43,  8, 44, 43, 18, 21]
    y2  = [9, 31, 25, 14, 17, 17, 42, 22, 28]
    y3  = [18, 29, 19, 22, 18, 16, 13, 32, 21]
    
    x_label = 'X Label'
    y_label = 'Y Label'
    title_label = 'Stack Plot Example'

    if 'x_label' in kwargs:
        x_label = kwargs['x_label']
    if 'y_label' in kwargs:
        y_label = kwargs['y_label']
    if 'title_label' in kwargs:
        title_label = kwargs['title_label']
    if 'x_values' in kwargs:
        x_values = kwargs['x_values']
    if 'y_values' in kwargs:
        y1 = kwargs['y_values']
        y2 = [int(y)+20 for y in y1]
        y3 = [int(y)+40 for y in y1]
        
        # Convert data type to integer
        y1 = [int(y) for y in y1]
        y2 = [int(y) for y in y2]
        y3 = [int(y) for y in y3]

    plt.stackplot(x_values, y1, y2, y3)

    plt.title(title_label)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    #plt.show()
    return plt.gcf()


def pie_chart1(**kwargs):
    """
    Pie chart, where the slices will be ordered and plotted counter-clockwise.

    Args 
          **kwargs lets you pass arguments into this function
    """
    labels_val = 'C', 'Python', 'Java', 'C++', 'C#'
    values = [13.38, 11.87, 11.74, 7.81, 4.41]
    explode = (0, 0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Python')
    
    labels = 'X Label'
    title_label = 'TIOBE Index for May 2021'

    if 'x_values' in kwargs:
        labels_val = kwargs['x_values']
    if 'title_label' in kwargs:
        title_label = kwargs['title_label']
    if 'y_values' in kwargs:
        values = kwargs['y_values']

        explode = list(np.zeros(len(values))) # None exploded


    fig1, ax1 = plt.subplots()
    ax1.pie(values, explode=explode, labels=labels_val, autopct='%1.1f%%',
            shadow=True, startangle=0)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title(title_label)
    #plt.show()
    return plt.gcf()


def pie_chart2(**kwargs):
    """
    Another Pie Chart
    Pie chart, where the slices will be ordered and plotted counter-clockwise.

    Args 
          **kwargs lets you pass arguments into this function
    """
    labels_val = 'C', 'Python', 'Java', 'C++', 'C#', 'others'
    values = [13.38, 11.87, 11.74, 7.81, 4.41]
    values.append(100 - sum(values)) # << THIS IS THE "others". "sum(sizes)"" adds up all the items in the tuple?
    explode = (0, 0.1, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Python')
    
    labels = 'X Label'
    title_label = 'TIOBE Index for May 2021'

    if 'x_values' in kwargs:
        labels_val = kwargs['x_values']
    if 'title_label' in kwargs:
        title_label = kwargs['title_label']
    if 'y_values' in kwargs:
        values = kwargs['y_values']

        explode = list(np.zeros(len(values)))


    fig1, ax1 = plt.subplots()
    ax1.pie(values, explode=explode, labels=labels_val, autopct='%1.1f%%',
            shadow=True, startangle=0)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title(title_label)
    #plt.show()
    return plt.gcf()


def show_figFunc(pFigureFunction, **kwargs):
    """
    Shows a figure

    args
        pFigureFunction (a function that returns a matplotlib figure)\n
        **kwargs needs to match kwargs of the function
    """
    current_fig = fig_with_kwargs(pFigureFunction,**kwargs)
    plt.figure(current_fig.number)
    plt.show()


def fig_with_kwargs(pFigureFunction, **kwargs):
    """
    Returns a figure after appying the kwargs

    args
        pFigureFunction (a function that returns a matplotlib figure) \n
        **kwargs needs to match kwargs of the function
    """
    kwarg_fig = None
    if kwargs :
        kwarg_fig = pFigureFunction(**kwargs)
    else:
        kwarg_fig = pFigureFunction()

    return kwarg_fig


if __name__ == "__main__":
    # Test scripts
    # show_figFunc(line_plot)
    # show_figFunc(discrete_plot)
    # show_figFunc(names_labels)

    show_figFunc(multiple_plots, x_label = 'Day', y_label = 'Temperature in Celsius from kwargs', 
                                  title_label = 'Temperature Graph', x_values = list(range(1, 9)), 
                                  y_values_1 = [19.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1], 
                                  y_values_2 = [24.8, 28.9, 31.3, 33.0, 34.9, 35.6, 38.4, 39.2])
    
    # show_figFunc(multiple_plots) -- DEFAULT DATA WORKS

    # show_figFunc(bar_chart)
    # show_figFunc(histogram, title="Our Name for Title")
    # show_figFunc(scatter_plots)
    # show_figFunc(stack_plot)
    # show_figFunc(pie_chart1)
    # show_figFunc(pie_chart2)
