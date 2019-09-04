# Source files
demographics = src/demographic_dat.py

# Input files
inmates_in = $(data_dir)/Daily_Inmates_In_Custody_08312019.csv
inmates_date = "08-31-2019"

# Output files
inmates_out = $(output_dir)/Inmates_With_Features.csv
demographics = $(output_dir)/Demographics.csv



$(inmates_out) $(demographics): $(inmates_in) $(demographics)
    python $(demographics) \
        --inmates_file $(inmates_in) \
        --inmates_date $(inmates_date) \
        --inmates_output $(inmates_out) \
        --demographics_output $(demographics) \
