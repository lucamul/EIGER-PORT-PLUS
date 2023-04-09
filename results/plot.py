import argparse
from os import listdir
import os
from sys import argv
import matplotlib.pyplot as plt
from matplotlib import rcParams
from parameters import *

paths = {
    "num_clients" : "/home/luca/ETH/Thesis/EIGERPORT+/results/num_clients.csv",
    "num_servers" : "/home/luca/ETH/Thesis/EIGERPORT+/results/num_servers.csv",
    "zipf" : "/home/luca/ETH/Thesis/EIGERPORT+/results/zipf.csv",
}

labels = {
    "num_clients" : "Number of Clients",
    "num_servers" : "Number of Servers",
    "zipf" : "Zipf Parameter",
}

titles = {
    "num_clients" : " vs. Number of Client Threads",
    "num_servers" : " vs. Number of Servers",
    "zipf" : " vs. Zipf Parameter",
}

nums = ["(a)", "(b)", "(c)", "(d)", "(e)", "(f)", "(g)", "(h)", "(i)", "(j)", "(k)", "(l)", "(m)", "(n)", "(o)", "(p)", "(q)", "(r)", "(s)", "(t)", "(u)", "(v)", "(w)", "(x)", "(y)", "(z)"]
idx = 0

def plot(path, title):
    global idx
    num = nums[idx]
    idx+=1
    with open(path) as f:
        lines = f.readlines()
        x_label = labels[title]
        x_axis = []
        y_axises = { "throughput" : {}, "latency" : {} }
        for line in lines[1:]:
            line = line.strip().split(",")
            algorithm = line[0]
            if algorithm not in algorithms:
                continue
            if algorithm not in y_axises["throughput"]:
                y_axises["throughput"][algorithm] = []
            if algorithm not in y_axises["latency"]:
                y_axises["latency"][algorithm] = []
            if line[1] not in x_axis:
                x_axis.append(line[1])
            y_axises["throughput"][algorithm].append(line[2])
            y_axises["latency"][algorithm].append(line[3])
        bar = False
        throughput_label = "Throughput (ops/s)"
        latency_label = "Latency (ms)"
        if title == "zipf":
            bar = True
            throughput_label = "Normalized Throughput"
            latency_label = "Normalized Latency"
        generate_plot(x_axis, y_axises["throughput"], "Throughput" + titles[title], x_label,throughput_label, path, bar, num)
        num = nums[idx]
        idx += 1
        generate_plot(x_axis, y_axises["latency"], "Latency" + titles[title], x_label,latency_label, path, bar, num)
        if title == "num_clients":
            num = nums[idx]
            generate_plot(y_axises["throughput"],y_axises["latency"], "Latency vs. Throughput",throughput_label, latency_label, path, bar, num)
            idx += 1
    return

def plot_all():
    for i, path in enumerate(paths):
        plot(paths[path], path)
    return

def convert_str_to_int(x_axis, y_axises):
    # check if x_axis is a dict
    if isinstance(x_axis, dict):
        for algorithm in x_axis:
            x_axis[algorithm] = [float(x) for x in x_axis[algorithm]]
        if all(all(x.is_integer() for x in x_axis[algorithm]) for algorithm in x_axis):
            for algorithm in x_axis:
                x_axis[algorithm] = [int(x) for x in x_axis[algorithm]]
        for algorithm in y_axises:
            y_axises[algorithm] = [float(y) for y in y_axises[algorithm]]
        if all(all(y.is_integer() for y in y_axises[algorithm]) for algorithm in y_axises):
            for algorithm in y_axises:
                y_axises[algorithm] = [int(y) for y in y_axises[algorithm]]
        return x_axis, y_axises
    
    x_axis = [float(x) for x in x_axis]
    for algorithm in y_axises:
        y_axises[algorithm] = [float(y) for y in y_axises[algorithm]]
    # if the floats have no decimals then convert them to int
    if all(x.is_integer() for x in x_axis):
        x_axis = [int(x) for x in x_axis]
    if all(all(y.is_integer() for y in y_axises[algorithm]) for algorithm in y_axises):
        for algorithm in y_axises:
            y_axises[algorithm] = [int(y) for y in y_axises[algorithm]]
    return x_axis, y_axises

def generate_plot(x_axis, y_axises, title, x_label, y_label, directory, barPlot = False, num = ""):
    if barPlot:
        _, y_axises = convert_str_to_int([], y_axises)
        fig, ax = plt.subplots()

        x_positions = np.arange(len(x_axis))  # create an array of x positions for each set of bars
        le = 0
        for i, algorithm in enumerate(y_axises):
            if(algorithm not in algorithms):
                continue
            
            offset = le * bar_width
            le += 1
            ax.bar(x=x_positions + offset, height=y_axises[algorithm], width=bar_width, label=names[algorithm], color=colors[algorithm])
        
        mid_pos = (le - 1) / 2.0

        # Set the tick position to the middle position of the middle bar
        ax.set_xticks(x_positions + (mid_pos * bar_width))

        ax.set_title(num + " " + title, **title_info)
        ax.set_xlabel(x_label, fontsize=axis_font)
        ax.set_ylabel(y_label, fontsize=axis_font)
        ax.tick_params(axis='both', which='major', labelsize=tick_font)
        ax.set_xticklabels(x_axis, fontsize=tick_font)
        legend = ax.legend(bbox_to_anchor=(0.5, 1.8), loc='center', ncol = len(algorithms),frameon = False ,prop = {"size" : 16}, fontsize = 12)
        legend.get_frame().set_edgecolor('black')
        legend.get_frame().set_linewidth(1.4)
        export_legend(legend)
        if haveGrid:
            ax.grid(haveGrid, color='gray', linestyle='--', linewidth=1, axis='y')
        
        title_no_spaces = title.replace(" ", "_")
        filename = os.path.basename(directory)

        dir_name = filename.replace(".csv", "")

        new_dir_path = os.path.join(saveTo, dir_name)

        if not os.path.exists(new_dir_path):
            os.mkdir(new_dir_path)
        
        dir_name += "/"
        plt.gcf().set_size_inches(10, 6)
        plt.savefig(saveTo + dir_name + title_no_spaces + ".pdf",dpi=200)
        if showPlot:
            plt.show()
        return
    x_axis, y_axises = convert_str_to_int(x_axis, y_axises)
    fig, ax = plt.subplots()
    for algorithm in y_axises:
        if(algorithm not in algorithms):
            continue
        # if x_axis is a dict
        if isinstance(x_axis, dict):
            ax.plot(x_axis[algorithm], y_axises[algorithm], label=names[algorithm], color=colors[algorithm], marker=markers[algorithm], linewidth=line_width,markersize=marker_size,markeredgewidth=2, markeredgecolor= colors[algorithm], markerfacecolor='None')
        else:
            ax.plot(x_axis, y_axises[algorithm], label=names[algorithm], color=colors[algorithm], marker=markers[algorithm],linewidth = line_width,markersize=marker_size,markeredgewidth=2, markeredgecolor= colors[algorithm], markerfacecolor='None')
    ax.set_title(num + " " + title, **title_info)
    ax.set_xlabel(x_label, fontsize=axis_font)
    ax.set_ylabel(y_label, fontsize=axis_font)
    ax.tick_params(axis='both', which='major', labelsize=tick_font)
    #ax.legend()
    if haveGrid:
        ax.grid(haveGrid, color='gray', linestyle='--', linewidth=1, axis='y')
    title_no_spaces = title.replace(" ","_")
    filename = os.path.basename(directory)

    dir_name = filename.replace(".csv", "")

    new_dir_path = os.path.join(saveTo, dir_name)

    if not os.path.exists(new_dir_path):
        os.mkdir(new_dir_path)
    
    dir_name += "/"
    plt.gcf().set_size_inches(10, 6)
    plt.savefig(saveTo+dir_name+title_no_spaces+".pdf",dpi=200)
    
    if showPlot:
        plt.show()
    return
def export_legend(legend, filename="legend.pdf"):
    fig  = legend.figure
    fig.canvas.draw()
    bbox  = legend.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig(saveTo + filename, dpi="figure", bbox_inches=bbox)

if __name__ == "__main__":
    plot_all()