import os, io, ast, json
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def check_directories(root, target):
    '''Checks for a directory and a target file/folder. If it doesn't exist, it creates it.'''
    try:
        if not os.path.exists(f"{root}/{target}"):
            os.mkdir(f"{root}/{target}")
    except:
        print(f"Error checking/creating directory '{root}/{target}'")
        exit()
    else:
        return f"{root}/{target}"

def main():
    dataFolder = check_directories(os.getcwd(), "raw_data")
    graphFolder = check_directories(os.getcwd(), "plotted_data")

    days = []
    values = []
    day_labels = []

    for file in os.listdir(dataFolder):
        with open(f"{dataFolder}/{file}") as f:
            data = f.read()
            print(data)
        fileData = ast.literal_eval(data)
        days.append(f"{fileData['weekday']}, {fileData['day']}")
        values.append(float(fileData['average rating']))
        
    print(days)
    print(values)

    # Save data
    

    # Create the graph
    fig, ax = plt.subplots()
    
    ax.bar(days, values)
    ax.set_ylabel("rating")
    ax.set_title("Average rating per day")

    fig.show()

    f = io.BytesIO()
    fig.savefig(f, format="png")

    input()
    # Save the graph as pdf

if __name__ == "__main__":
    main()