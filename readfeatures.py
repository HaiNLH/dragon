import numpy as np
import pandas as pd


text_features = np.load('data/baby/text_feat-v1.npy')
# print(text_features[:5])
print(text_features.shape)

img_features = np.load('data/baby/image_feat.npy')
print(img_features.shape)
print(img_features[0])

# adj_mat = np.load('data/baby/user_graph_dict.npy')
# print(adj_mat.shape)

df = pd.read_csv('data/baby/baby14-indexed-v4.inter')
print(df.head(5))
print(df.shape)