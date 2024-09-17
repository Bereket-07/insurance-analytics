import pandas as pd
from sklearn.preprocessing import LabelEncoder , StandardScaler
from sklearn.model_selection import  train_test_split
from sklearn.preprocessing import OneHotEncoder
from scipy import sparse
from sklearn.decomposition import PCA




def data_load(path):
    return pd.read_csv(path)
def drop_the_unwanted_data_column(data ,columns_to_drop):
    data1 = data.drop(columns=columns_to_drop)
    return data1
def see_for_missing_values(data):
    return data.isnull().sum()
def delete_duplicated_rows(data):
    data = data.drop_duplicates(keep="first")
    return data
def change_object_to_number(data,numeric_cols):
    dataframe = data.copy()
    dataframe[numeric_cols] = data[numeric_cols].apply(pd.to_numeric, errors='coerce')
    return dataframe
def lable_encoding(data , catagoricalcols):
    dataframe = data.copy()
    le = LabelEncoder()
    for col in catagoricalcols:
        dataframe[col] = le.fit_transform(data[col])
    return dataframe
def one_hot_encoding(data,catagoricalcols):
    dataframe = data.copy()
    one_hot_encoder = OneHotEncoder(sparse_output=True)
    one_hot_encoded_matrix = one_hot_encoder.fit_transform(dataframe[catagoricalcols])
    # Convert dense data (non-categorical) to sparse and combine
    rest_of_data = sparse.csr_matrix(dataframe.drop(columns=catagoricalcols))
    final_data = sparse.hstack([rest_of_data, one_hot_encoded_matrix])
    
    # reduce dimentinality
    # Apply PCA to reduce dimensions
    pca = PCA(n_components=100)  # Adjust n_components based on the explained variance
    reduced_data = pca.fit_transform(final_data.toarray())


    return reduced_data
def target_variable_and_features(data):
    X= data.drop(columns=['TotalClaims'])
    y_claims = data['TotalClaims']
    return X ,y_claims
def train_test_split_selection(X , y_claims):
    x_train , x_test ,  y_train_claims , y_test_claims = train_test_split(X,y_claims , test_size=0.2, random_state=42)
    return x_train , x_test ,  y_train_claims , y_test_claims
def feature_scaling(x_train , x_test):
    scalar = StandardScaler()
    x_trian_scaled = scalar.fit_transform(x_train)
    x_test_scaled = scalar.transform(x_test)
    return x_trian_scaled ,x_test_scaled




