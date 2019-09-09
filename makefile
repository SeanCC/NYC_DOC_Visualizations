data_dir=data
output_dir=output
parent_dir=C:\Users\seanc\OneDrive\Documents\NYC_DOC_Visualizations

.PHONY: all
.DEFAULT_GOAL: all
all:
	cd $(parent_dir)\load_data && make \
	cd $(parent_dir)\generate_demographics && make \
	cd $(parent_dir)\generate_visualizations && make