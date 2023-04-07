import numpy as np

# parameters for plot
title_font = 20
axis_font = 18
tick_font = 16
title_info = {'fontsize': title_font,
            'fontweight' : "bold",
            'verticalalignment': 'baseline',
            'horizontalalignment': "center"}

marker_size = 13
line_width = 2.5
tick_font_inaxis = 10
haveGrid = False
showPlot = True
bar_width = 0.2

# edit this if you want to change the algorithms you can plot
algorithms = ["EIGER", "EIGER_PORT", "EIGER_PORT_PLUS"]
# save the images as pdfs here
saveTo = "/home/luca/ETH/Thesis/EIGERPORT+/results/"

colors = {
    "EIGER": "#1f77b4",
    "EIGER_PORT": "#ff7f0e",
    "EIGER_PORT_PLUS": "#2ca02c",
}

markers = {
    "EIGER": "o",
    "EIGER_PORT": "s",
    "EIGER_PORT_PLUS": "v",
}

names = {
    "EIGER": "Eiger",
    "EIGER_PORT": "Eiger-PORT",
    "EIGER_PORT_PLUS": "Eiger-PORT+",
}