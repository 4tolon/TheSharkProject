#CLEANING FUNCTIONS 

# Libraries 
import pandas as pd

def dic_list(values):
    """
    This function gets a list and returns a dictionarie with keys as index of list,
    and values the list items.
    """ 
    import pandas as pd
    return dict(list(enumerate(values)))

def RAS_the_one_and_only_one_cell_output_analisys_program(data):
    """
    This function ask for changes in columns names of a DataFrame and more
    """
    import pandas as pds
    from IPython.display import clear_output
    from src import cleanning_func as cf
    import time 
    col_list = list(data.columns)
    data_shape = data.shape
    a = cf.dic_list(col_list)  #Frist function defined in this file
    new_a = []
    for i in range(len(a)):
        # Information variables about each column
        null = data[a[i]].isna().sum()
        lenn = len(data[a[i]])
        null_percent = round((null/lenn*100), 1)
        uniq = data[a[i]].unique()[:3]
        print('-----------SOME DATA TO HELP-----------')
        print(f'Column index   : {1} of {len(a)}')
        print(f'Number of rows : {data_shape[0]}')
        print(f'Number nam/nul : {null} thats the {null_percent} %')
        print(f'Example unique : {uniq}')
        #print(f'Number uniques : {len(uniq)} some of them are: {uniq_show}')
        # Input stament
        b = (input(f"Enter a new value:\nor skip to next by pressing enter\ntype 'del' to show next function to drop this column\n\n\n\n\b'{a[i]}'"))
        # Loops for mange the unmodified and refreshing the output
        if b == '':
            new_a.append(a[i])
            time.sleep(0.2)
            clear_output(wait = True)
            continue
        else:
            new_a.append(b)
            time.sleep(0.2)
            clear_output(wait = True)
    # Creation of the new dataframe
    df = data.set_axis(new_a, axis=1)
    # Delete the columns name as "del"
    del df['del']
    # Delete all rows with at least 4 Nan
    df.dropna(axis=0, how='all',thresh=4, inplace = True)
    return df

def del_col(data_to_clean):
    """
    This function returns a dataframe with rename columns and removed non relevance of your choice 
    """
    import pandas as pd
    from src import cleanning_func as cf
    colu = chan_col(data_to_clean)
    to_drop = [ d == 'drop' for d in colu]
    df_shape_clean = data_to_clean.drop(to_drop)
    return df_shape_clean

