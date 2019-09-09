import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import argparse
import pyarrow

def main(datelog,
    inmate_data_directory,
    demo_data_directory,
    output_directory):
    last_date = ""
    with open(datelog, "r") as log:
        dates = log.readlines()
        last_date = dates[len(dates)-1].rstrip()
    
    demographics = pd.read_feather(f'{demo_data_directory}/{last_date}_demographics.feather')
    inmates = pd.read_feather(f'{inmate_data_directory}/{last_date}_inmates.feather')
    incarcerated_dists(inmates, last_date, output_directory)
    incarc_level(demographics, last_date, output_directory)
    incarc_race_chart(demographics, last_date, output_directory)
    
def incarcerated_dists(inmates, date, output_directory):
    fig, ax = plt.subplots(figsize=(12,8))
    ax.set_xlim(0, 2000)
    for race in ['W', 'B', 'O']:
        rsub = inmates[inmates['race'] == race]
        sns.distplot(rsub['length_incarcerated'], hist=False, kde=True, label = race )
    fig.savefig(f'{date}_length_incarcerated_dists.png')


def incarc_level(demographics, date, output_directory):
    incarc_level_df = demographics.groupby(['custody_level', 'race']).sum()['count'].reset_index()

    # Pivot by incarceration level
    pivot=incarc_level_df.pivot(index='custody_level', columns='race', values='count')
    plot = pivot.plot(kind = 'barh', stacked=True, alpha=0.9, colormap='viridis')
    plot.set_facecolor('whitesmoke')
    plot.xaxis.grid(True, linestyle='-', linewidth=0.5)
    fig = plot.get_figure()
    fig.savefig(f'{date}_stacked_bar_incarc_pivot.png')

    # Pivot by race
    pivot=incarc_level_df.pivot(index='race', columns='custody_level', values='count')
    plot = pivot.plot(kind='barh', stacked=True, alpha=0.9, colormap='cividis')
    plot.set_facecolor('whitesmoke')
    plot.xaxis.grid(True, linestyle='-', linewidth=0.5)
    fig=plot.get_figure()
    fig.savefig(f'{date}_stacked_bar_race_pivot.png')

    # Pivot by gang affiliation
    incarc_level_df = demographics.groupby(['custody_level', 'srg_flg']).sum()['count'].reset_index()
    pivot = incarc_level_df.pivot(index='srg_flg', columns='custody_level', values='count')
    plot=pivot.plot(kind='barh', stacked=True, alpha=0.9, colormap='viridis')
    plot.set_facecolor('whitesmoke')
    plot.xaxis.grid(True, linestyle='-', linewidth=0.5)
    fig=plot.get_figure()
    fig.savefig(f'{date}_stacked_bar_gang_pivot.png')
    return()

    
def incarc_race_chart(demographics, date, output_directory):
    incarc_df = demographics.groupby(['race', 'gender']).sum().reset_index().sort_values("count", ascending=False)
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.set_color_codes("deep")
    sns.barplot(x="count", y="race", color="r", data=incarc_df, ci=None)
    sns.set_color_codes("muted")
    sns.barplot(x="count", y="race", color="b", data=incarc_df[incarc_df['gender'] == 'F'], ci=None )
    fig.savefig(f'{date}_incarc_race_chart.png')

    incarc_df.sort_values("sum_days", ascending=False, inplace=True)
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.set_color_codes("deep")
    sns.barplot(x="sum_days", y="race", color="r", data=incarc_df, ci=None)
    sns.set_color_codes("muted")
    sns.barplot(x="sum_days", y="race", color="b", data=incarc_df[incarc_df['gender'] == 'F'], ci=None)
    fig.savefig(f'{date}_incarc_race_chart_time.png')



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--datelog", help="Path to log of inmates file downloads")
    parser.add_argument("--inmate_data_directory", help="Path to inmate data directory")
    parser.add_argument("--demo_data_directory", help="Path to demographic data directory")
    parser.add_argument("--output_directory", help="Path to output demographics")
    args = parser.parse_args()
    main(
        datelog=args.datelog,
        inmate_data_directory=args.inmate_data_directory,
        demo_data_directory=args.demo_data_directory,
        output_directory=args.output_directory
    )