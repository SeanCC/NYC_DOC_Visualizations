import argparse
import pandas as pd
def main(inmates_file,
         file_date,
        demo_output,
        inmates_output):
    inmates = pd.read_csv(inmates_file)
    inmates['ADMITTED_DT'] = pd.to_datetime(inmates['ADMITTED_DT'])
    inmates['length_incarcerated'] = (datetime.strptime(file_date, '%m-%d-%Y') - inmates['ADMITTED_DT']).dt.days
    inmates.to_csv(inmates_output)
    demo_data = inmates.groupby(['RACE', 'GENDER', 'CUSTODY_LEVEL']).count()[['INMATEID']]
    demo_df = demo_data.reset_index()
    demo_df.rename(columns={'INMATEID': 'count'}, inplace=True)
    demo_df[['count']] = demo_df[['count']].fillna(value=0)
    demo_df[['avg_length']] = inmates.groupby(['RACE','GENDER','CUSTODY_LEVEL']).mean()[['length_incarcerated']].reset_index()[['length_incarcerated']]
    demo_df[['avg_length']] = demo_df[['avg_length']].fillna(value=0)
    demo_df.to_csv(demo_output)
    
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--inmates_file", help="path to inmates file")
    parser.add_argumnet("--inmates_date", help="date of inmates file")
    parser.add_argument("--inmates_output", help="path to inmates output file")
    parser.add_argument("--demographics_output", help="path to demographics output file")
    args = parser.parse()
    main(inmates_file = args.inmates_file,
        file_date = args.inmates_date,
        demo_output = args.demographics_output,
        inmates_output = args.inmates_output)