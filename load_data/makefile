
# Source files
load_data = src\load_datasets.py

# Input files
data_config = config\load_data.yml
date_log = $(data_dir)\dates.txt


.PHONY: all

all:
	python $(load_data) \
		--data_config $(data_config) \
		--date_log $(date_log) \
		--output_directory $(output_dir)