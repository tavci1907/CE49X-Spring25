import pandas as pd
#only library I need for this lab is pandas, so I import it.
def load_data(file_path):
#Function I created to read csv file 
    try:
    #attempt to read the csv file
        data=pd.read_csv(file_path)
        print("data loaded succesfully.")#informs user that he/she succeeded reading csv file
        return data
    except Exception as e: #In case if theres an error reading the file
        print(f"Error: {e}")
        return None
def clean_data(data, column): #function for cleaning the data (to get rid of NaN's)
    if data is None:
        return None  # If the data is None, return None (no data to clean)
    data_filled = data.fillna(data.mean())# Fill missing values (NaN) in the dataset with the mean of the respective column

    column_mean = data_filled[column].mean()
    column_std = data_filled[column].std()
    #Removing outliers from  soil ph column by keeping values within 3 standard deviations from the mean
    data_no_outliers = data_filled [ 
        (data_filled[column] > (column_mean -3*column_std)) & (data_filled[column] < (column_mean +3*column_std))
    ]
    return data_no_outliers
def compute_statistics(data, column, stat_type):
    if data is None or column not in data.columns:
        print(f"Error: {column} not found in the dataset.")
        return
    if stat_type == 'min':
        return data[column].min()
    elif stat_type == 'max':
        return data[column].max()
    elif stat_type == 'mean':
        return data[column].mean()
    elif stat_type == 'median':
        return data[column].median()
    elif stat_type == 'std':
        return data[column].std()
    elif stat_type == 'all':
        # If 'all' is selected, return all statistics
        return {
            'min': data[column].min(),
            'max': data[column].max(),
            'mean': data[column].mean(),
            'median': data[column].median(),
            'std': data[column].std()
        }
    else:
        print(f"Error: Statistic type '{stat_type}' is not recognized.")
        return None
def main():
    file_path='C:/Users/can_a/CE49X-Spring25/datasets/soil_test.csv'
    data = load_data(file_path)
    if data is None:
        return # If data is None, exit the function
    
    available_columns = data.drop(columns=['sample_id']).columns
    
    print("Available columns:", list(available_columns))
    column_to_analyze = input("Enter the column name you want to analyze: ").strip()
# If the column exists, clean it by removing outliers
    if column_to_analyze in available_columns:
        cleaned_data = clean_data(data, column_to_analyze)
        print(f"Outliers removed from {column_to_analyze}.")
    else:
        print(f"Error: {column_to_analyze} not found in the dataset.")
        return
    
    valid_statistics = ['min', 'max', 'mean', 'median', 'std', 'all']
    print("Available statistics: min, max, mean, median, std, all")
    stat_type = input("Enter the statistic you want to compute: ").strip().lower()
    result = compute_statistics(data, column_to_analyze, stat_type)
    if result is not None:
        if stat_type == 'all':
            # If "all" statistics are selected, display all stats
            for stat, value in result.items():
                print(f"The {stat} of {column_to_analyze} is: {value}")
        else:
            print(f"The {stat_type} of {column_to_analyze} is: {result}")
        
if __name__ == '__main__':
    main()
