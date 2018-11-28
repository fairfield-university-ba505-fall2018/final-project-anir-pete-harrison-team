import pandas as pd
def citations_per_warning(df):
     return (pd.Series({'citations_per_warning':len(df[df['Violation Type']== 'Citation'])/len(df[df['Violation Type'] == 'Warning'])}))