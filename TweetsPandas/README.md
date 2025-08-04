# Project Tweets Pandas

### Folders:

- **Data**: This folder has the data for the project.
- **SRC**: This folder has the project files.
- **Results**: This folder saves the final JSON file and the clean CSV file.

### Main Files:

- **Loader.py**: This file gets the data folder and saves the data as a DataFrame (DF). **All the data is as strings.**

- **DataCleaner.py**: This file has functions to make a clean CSV file from the data, as the project needs.

- **DataAnalyzer.py**: This class takes the data and splits it by the project rules.
- **ReportBuilder.py**: This file builds the final JSON file. It uses the functions from the data analyzer.
  - It have a dictionary: the key is the data type name, and the value is the data.
  - It have a list of keys that are in the dictionary.
  - It has a function for each JSON request.
  
- **DataExporter.py**: This file has a class with two functions:
  - 1. Make a CSV file.
  - 2. Make a JSON file.
  
- **Manager.py**: This file runs everything.
  - It gets the clean data from the DataCleaner and makes a CSV.
  - It gets the data from the ReportBuilder and makes a JSON.
