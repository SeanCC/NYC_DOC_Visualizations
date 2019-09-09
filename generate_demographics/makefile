# Source files
demographics=src/demographic_dat.py
# Input files
date_file=$(data_dir)/dates.txt
# Output files
inmates_out=$(output_dir)
demographics_out=$(output_dir)
.PHONY: all
.DEFAULT: all
all: 
	python  $(demographics) \
		--inmates_dir $(data_dir) \
		--date_file $(date_file) \
		--inmates_output_dir $(inmates_out) \
		--demographics_output $(demographics_out) \
