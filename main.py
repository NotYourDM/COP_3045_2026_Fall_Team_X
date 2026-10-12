import src.data.pipe as data_pipe
import src.eda.pipe as eda_pipe
import src.report.pdf_export as pdf_export
import pandas

def bool_prompt(prompt : str) -> bool:
	a = input(prompt).lower()
	return a == 'y' or a == 'yes'

if __name__ == "__main__":
	print("\nInitializing project...\n")
	print("Note that this project may stop and require hitting [enter] to view more information.")
	input("This is intentional as to attempt to prevent having more than one screen's worth of information given at a time.")

	input("Running Main...")
	print("Piping data frame.")
	
	include_merge : bool = bool_prompt("Include dataset merging? [y/n]: ")
	include_clean_report : bool = bool_prompt("Include data cleanliness report? [y/n]: ")
	input("\nPreparing data...")
	
	df : pandas.DataFrame = data_pipe.get_data_frame(include_merge, include_clean_report)
	
	input("Data preparation complete.")

	include_summary : bool = bool_prompt("Include summary statistics? (mean, range, std, etc.) [y/n]: ")
	include_visual : bool = bool_prompt("Include visualization? (graphs) [y/n]: ")
	input("\nPreparing analyticals...")

	eda_pipe.display_data(df, include_summary, include_visual)

	input("Data analysis complete.")

	include_pdf : bool = bool_prompt("\nInclude PDF export? [y/n]: ")
	if include_pdf:
		pdf_export.make_pdf("movie_data_analysis.pdf", df, include_summary, include_visual)
		input("PDF export complete.")
	print("\nNo tasks remain. Thank you for running this project!")