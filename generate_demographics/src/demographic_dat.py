import argparse
import datetime
import pandas as pd
import pyarrow
from datetime import datetime

def main(inmates_dir,
         date_file,
        demo_output,
        inmates_output):
    date = ""
    with open(date_file, 'r') as log:
        dates = log.readlines()
        last_date = dates[len(dates)-1].rstrip()

    inmates = pd.read_feather(f'{inmates_dir}/{last_date}_inmates.feather')

    last_date_dt = pd.to_datetime(datetime.utcfromtimestamp(int(last_date)).strftime('%m-%d-%Y'))
    inmates['admitted_dt'] = pd.to_datetime(inmates['admitted_dt'])
    inmates['length_incarcerated'] = (last_date_dt - inmates['admitted_dt']).dt.days
    inmates.to_feather(f'{inmates_output}/{last_date}_inmates.feather')
    inmates.loc[inmates['race'].isin(['I', 'U']), 'race'] = 'O'
    demo_data = inmates.groupby(['race', 'gender', 'custody_level', 'srg_flg']).count()[['inmateid']]
    demo_df = demo_data.reset_index()
    demo_df.rename(columns={'inmateid': 'count'}, inplace=True)
    demo_df[['count']] = demo_df[['count']].fillna(value=0)
    demo_df[['avg_length']] = inmates.groupby(['race','gender','custody_level', 'srg_flg']).mean()[['length_incarcerated']].reset_index()[['length_incarcerated']]
    demo_df[['avg_length']] = demo_df[['avg_length']].fillna(value=0)
    demo_df['sum_days'] = demo_df['avg_length']*demo_df['count']
    demo_df.to_feather(f'{demo_output}/{last_date}_demographics.feather')
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--inmates_dir", help="path to inmates file directory")
    parser.add_argument("--date_file", help="log of retrieval dates")
    parser.add_argument("--inmates_output_dir", help="path to inmates output file")
    parser.add_argument("--demographics_output_dir", help="path to demographics output file")
    args = parser.parse_args()
    main(inmates_dir = args.inmates_dir,
        date_file = args.date_file,
        demo_output = args.demographics_output_dir,
        inmates_output = args.inmates_output_dir)