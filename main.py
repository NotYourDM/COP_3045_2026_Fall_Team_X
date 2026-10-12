import src.data.pipe as data_pipe
import src.eda.pipe as eda_pipe
import src.eda.summary_stats as summary_stats
import pandas

if __name__ == "__main__":
	print("Note that this project may stop and require hitting enter to view more information.")
	input("This is on purpose as to attempt to prevent having more than one screen's worth of information given at a time.")

	input("Running Main...")
	print("Piping data frame.")
	
	merge_response : str = input("Include data merging process? [y/n]: ").lower()
	include_merge : bool = merge_response == 'y' or merge_response == 'yes'

	clean_report_response : str = input("Include data cleanliness reponrt? [y/n]: ").lower()
	include_clean_report : bool = clean_report_response == 'y' or clean_report_response == 'yes'
	
	df : pandas.DataFrame = data_pipe.get_data_frame(include_merge, include_clean_report)

	eda_pipe.display_data(df)