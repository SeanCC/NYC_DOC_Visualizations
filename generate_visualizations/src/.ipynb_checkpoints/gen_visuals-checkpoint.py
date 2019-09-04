import pandas as pd
import seaborns as sns
import matplotlib.pyplot as plt
import argparse


def main(demo_file,
        inmates_file):
    demographics = pd.read_csv(demo_file)
    inmates = pd.read_csv(inmates_file)
    
    
def dist_plots(inmates_file):
    grid = sns.FacetGrid(inmates.dropna(subset=['RACE']), col='RACE', col_wrap=3, hue = 'RACE', palette=sns.color_palette('deep', 6))
    grid.map(sns.distplot, 'length_incarcerated')
    
def pie_charts(demo_file):
    return()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--inmates_file", help="Path to inmates file")
    parser.add_argument("--demo_file", help="Path to demographics file")
    parser.add_argument("--output_directory", help="Path to output demographics")