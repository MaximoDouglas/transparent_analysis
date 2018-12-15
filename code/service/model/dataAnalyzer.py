#deprecated class - Not enough data to apply apriori

import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder


class DataAnalyzer():
    def analyze(filePath):
        #Reading CSV as a pandas dataframe
        df = pd.read_csv(filePath)

        #converting the DataFrame into a list
        dataset = df.values.tolist()

        #instanciating the TransactionEncoder
        te = TransactionEncoder()

        #converting the list into a dummie dataset
        te_ary = te.fit(dataset).transform(dataset)

        #converting the dummie dataset into a pandas DataFrame
        df = pd.DataFrame(te_ary, columns=te.columns_)

        #applying the apriori algorithm with 0.1 min_support
        result = apriori(df, min_support=0.1, use_colnames=True)

        return result
