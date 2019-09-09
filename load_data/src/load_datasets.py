import pandas as pd
import argparse
import yaml
import sodapy
import datetime
import pyarrow

def main(data_config,
    date_log,
    output_directory):
    inmates_client = sodapy.Socrata(data_config['service_url'], None)
    data = inmates_client.get(data_config['endpoint'], content_type='json')
    date = inmates_client.get_metadata(data_config['endpoint'])["rowsUpdatedAt"]
    inmates_df = pd.io.json.json_normalize(data)
    inmates_df.to_feather(f'{output_directory}/{date}_inmates.feather')
    with open(date_log, 'a') as log:
        log.write(f'{date}\n')
    return()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_config', help="Path to config for downloading data files")
    parser.add_argument('--date_log', help="Path to date log")
    parser.add_argument('--output_directory', help="Path to inmates output file")
    args = parser.parse_args()
    with open(args.data_config, 'r') as file:
        data_config = yaml.load(file)
    main(data_config=data_config,
    date_log = args.date_log,
    output_directory = args.output_directory)