import pandas as pd
import pickle
from semanticpy.vector_space import VectorSpace

data = pd.read_json('cc_jokes_valid.json')
df = pd.DataFrame(data)
dfList = df['content'].tolist()

#builds vector space model and saves to picle (takes long time)
vector_space = VectorSpace(dfList)
filehandler = open('vsm.obj', 'w')
pickle.dump(vector_space, filehandler)
