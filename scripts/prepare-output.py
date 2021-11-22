import pandas as pd
def azureml_main(dataframe1 = None, dataframe2 = None):
    scored_results=dataframe1[['Id', 'Scored Labels']]
    scored_results.rename(columns={'Scored Labels':'Heart disease'},
      inplace=True)
    return scored_results