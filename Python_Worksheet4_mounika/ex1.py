"""Create a module, CSVProcessor. It should contain functions for loading CSV data from an external file (titanic.csv), calculating
total number of columns, calculating total number of rows and filling missing values in any column with zero. Use Pandas read_csv
and other Pandas and Numpy functions. Import this module into another program and demonstrate invoking these methods.
"""
import CSVProcessor

def main():
   #load the titanic dataset
   file_path="titanic.csv"
   df=CSVProcessor.load_csv_file(file_path)

   #get the total number of columns
   print("Total columns:",CSVProcessor.total_col(df))

   #get the total number of rows
   print("Total number of rows:",CSVProcessor.total_rows(df))

   #fill missing places with zeros
   df_filled=CSVProcessor.fill_zeros_in_missing_value(df)
   print(df_filled.head(10))

if __name__=="__main__":
    main()
