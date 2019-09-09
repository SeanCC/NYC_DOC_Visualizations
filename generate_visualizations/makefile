# Source files
visualizations = src/gen_visuals.py
# Input files
date_file=$(data_dir)/dates.txt
inmate_dir = $(data_dir)
demo_dir = $(data_dir)

.PHONY: all
.DEFAULT: all
all: 
	python  $(visualizations) \
	--datelog $(date_file) \
	--inmate_data_directory $(inmate_dir) \
	--demo_data_directory $(demo_dir) \
	--output_directory $(output_dir)
