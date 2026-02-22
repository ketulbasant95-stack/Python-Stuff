import matplotlib.pyplot as plt

#Line Graph

def linegraph():
    "Used to plot a line graph in the Cartesian plane."

    numx = int(input("Enter number of values of X-axis: "))
    numy = int(input("Enter number of values of Y-axis: "))
    xval = []
    yval = []
    
    for i in range(numx):
        x = float(input("Enter the values of x-axis (one by one): "))
        xval.append(x)
        print("Number of values left:", numx-i)
    for j in range(numy):
        y = float(input("Enter the values of y-axis (one by one): "))
        yval.append(y)
        print("Number of values left:", numy-j)

    xaxis = input("Define X-axis (optional): ")
    yaxis = input("Define Y-axis (optional): ")
    title = input("Enter a title for the graph (optional): ")
    if xaxis=="":
        xaxis = "X-axis"
    if yaxis=="":
        yaxis = "Y-axis"
    if title=="":
        title = "Graph"

    flag = 0
    ch = input("Would you like to modify the graph appearance? (y/n): ")
    if ch=="y":
        flag = 1
        color = input("Enter the color of line: ")
        linestyle = input("Enter the line style: ")
        linewidth = int(input("Enter the line width: "))
    else:
        pass

    opt = input("Would you like to review your data? (y/n): ")
    if opt=="y":
        print(xval)
        print(yval)
    else:
        pass

    if flag==0:
        plt.plot(xval, yval)
        plt.title(title)
        plt.ylabel(yaxis)
        plt.xlabel(xaxis)
        plt.show()
    else:
        plt.plot(xval, yval, color=color, linestyle=linestyle, linewidth=linewidth)
        plt.title(title)
        plt.ylabel(yaxis)
        plt.xlabel(xaxis)
        plt.show()

#Bar graph

def bargraph():
    "Used to plot bar graph with given data."

    numx = int(input("Enter the number of values for X-axis: "))
    numy = int(input("Enter the number of values for Y-axis: "))
    xval = []
    yval = []
    
    for i in range(numx):
        x = float(input("Enter the value of X-axis:"))
        xval.append(x)
        print("Number of entries remaining:", numx-i)
    for j in range(numy):
        y = float(input("Enter the value of Y-axis: "))
        yval.append(y)
        print("Number of entries remaining:", numy-j)
    
    xaxis = input("Define X-axis (optional): ")
    yaxis = input("Define Y-axis (optional): ")
    title = input("Enter a title for the graph (optional): ")
    if xaxis=="":
        xaxis = "X-axis"
    if yaxis=="":
        yaxis = "Y-axis"
    if title=="":
        title = "Graph"

    opt = input("Would you like to review your data? (y/n): ")
    if opt=="y":
        print(xval)
        print(yval)
    else:
        pass

    plt.bar(xval, yval)
    plt.title(title)
    plt.ylabel(yaxis)
    plt.xlabel(xaxis)
    plt.show()

#Histogram

def histogram():
    "Used to plot a histogram of given data."
    numx = int(input("Enter the number of values of X-axis: "))
    bins = int(input("Enter bins: "))
    xval = []
    
    for i in range(numx):
        x = float(input("Enter the value of X-axis:"))
        xval.append(x)
        print("Number of entries remaining:", numx-i)
        
    xaxis = input("Define X-axis (optional): ")
    yaxis = input("Define Y-axis (optional): ")
    title = input("Enter a title for the graph (optional): ")
    if xaxis=="":
        xaxis = "X-axis"
    if yaxis=="":
        yaxis = "Y-axis"
    if title=="":
        title = "Graph"

    opt = input("Would you like to review your data? (y/n): ")
    if opt=="y":
        print(xval)
    else:
        pass

    plt.hist(xval, bins)
    plt.title(title)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.show()

#Scatter plot

def scatter():
    "Used to observe relationships between variables visually."

    numx = int(input("Enter the number of values of X-axis: "))
    numy = int(input("Enter the number of values of Y-axis: "))
    xval = []
    yval = []
    
    for i in range(numx):
        x = float(input("Enter the value of X-axis:"))
        xval.append(x)
        print("Number of entries remaining:", numx-i)
    for j in range(numy):
        y = float(input("Enter the value of Y-axis: "))
        yval.append(y)
        print("Number of entries remaining:", numy-j)

    xaxis = input("Define X-axis (optional): ")
    yaxis = input("Define Y-axis (optional): ")
    title = input("Enter a title for the graph (optional): ")
    if xaxis=="":
        xaxis = "X-axis"
    if yaxis=="":
        yaxis = "Y-axis"
    if title=="":
        title = "Graph"

    opt = input("Would you like to review your data? (y/n): ")
    if opt=="y":
        print(xval)
    else:
        pass

    plt.scatter(xval, yval)
    plt.title(title)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.show()

#Pie Graph

def pie():
    "Used to visually compare data proportions."

    numx = int(input("Enter the number of labels: "))
    label = []
    data = []

    for i in range(numx):
        x = input("Enter the label: ")
        label.append(x)
        print("Number of entries remaining: ", numx-i)
    
    for j in range(0, len(label)):
        y = float(input(f"Enter the value for {label[j]}: "))
        data.append(y)

    title = input("Enter title (optional): ")
    if title=="":
        title = "Pie Chart"
    
    plt.pie(data, label)
    plt.title(title)
    plt.show()
