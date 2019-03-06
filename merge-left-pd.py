import pandas as pd

import sys
from io import StringIO
    
    
    
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 25)

x = pd.read_csv(r'c:\temp\out4.tsv',sep="\t",error_bad_lines=0,index_col=False,nrows=15000)
y = x.head(100) 



comparetable = StringIO("""
sku;status
9780671493172;yes
9780803985643;yes
9780803985650;yes
9780226484549;yes
9780521434614;yes
9780521434611;yes
9780521434622;yes
9780521434633;yes
9780521434544;yes
9780195076066;yes
""")

comparetable = pd.read_csv(comparetable, sep=";")

# adds 'comparetable' to the right of x dataframe
z = pd.merge(x,comparetable,how='left',on='sku')
