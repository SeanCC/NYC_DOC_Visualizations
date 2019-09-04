import pandas as pd
import argparse
import yaml
import sodapy

def main(data_config, 
    inmates_output_file):
    inmates_client = sodapy.Socrata(data_config['service_url'], None)
    data = inmates_client.get(data_config['endpoint'], content_type='json')
    inmates_df = pd.io.json.json_normalize(data)
    inmates_df.to_csv(inmates_output_file)
    return()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_config', help="Path to config for downloading data files")
    parser.add_argument('--inmates_output_file', help="Path to inmates output file")
    args = parser.parse()
    with open(args.data_config, 'r') as file:
        data_config = yaml.load(file)

    main(data_config=data_config,
    inmates_output_file = args.inmates_output_file)