import pandas as pd
import numpy as np
import pickle
import joblib

# cluster dictionary
mapping = {0:'cleanser', 1:'mask', 2:'spot treatment', 3:'moisturizer', 4:'essence', 5:'serum', 6:'face mist', 7:'lip care', 8:'eye treatment', 9:'sun screen', 10:'booster', 11:'face oil', 12:'others'}

def get_cluster(input_list):
    input_list = np.array(input_list).reshape(1,20)
    model_path = "kmeans.pkl"
    loaded_model = pickle.load(open(model_path,"rb"))
    result = loaded_model.predict(input_list)
    result = [mapping[i] for i in result]
    return result[0]

def get_recommendation(product_name_search):
    df = pd.read_csv('beautyhaulclean.csv')
    # Ingredient Matrix

    ing_matrix = df[['Dry','Sensitive','Oily','Water','Cica', 'Salicylic Acid', 'Niacinamide', 'Ceramide', 'allantoin', 'Glycol', 'Retinol', 'Glycerin', 'Bakuchiol', 'Panthenol']].astype(int)
    ing_matrix


    cs_list = [] # cosine similarity value list
    brands = [] # brands list
    output = []
    ing_list_1 = [] # ingredients list
    # get index of product

    exists = product_name_search in df.product_name.values
    if exists == False:
        return []
    else:
        idx = df[df['product_name'] == product_name_search].index.item()

        # get ingredient list of product
        for i in ing_matrix.iloc[idx][0:]:
            ing_list_1.append(i) 

        # point1: product_name_search
        point1 = np.array(ing_list_1).reshape(1, -1)
        point1 = [val for sublist in point1 for val in sublist]
        product_type = df['Category'][df['product_name'] == product_name_search].iat[0]
        brand_search = df['brand'][df['product_name'] == product_name_search].iat[0]
        data_by_type = df[df['Category'] == product_type]

        for j in range(data_by_type.index[0], data_by_type.index[0] + len(data_by_type)):
            # point2: other product
            ing_list_2 = []
            for k in ing_matrix.iloc[j][0:]:
                ing_list_2.append(k)
            point2 = np.array(ing_list_2).reshape(1, -1)
            point2 = [val for sublist in point2 for val in sublist]
            
            dot_product = np.dot(point1, point2)
            norm_1 = np.linalg.norm(point1)
            norm_2 = np.linalg.norm(point2)
            # menghitung cosine similarity dari point1 dan point2
            cos_sim = dot_product / (norm_1 * norm_2)
            cs_list.append(cos_sim)

        data_by_type = pd.DataFrame(data_by_type)
        data_by_type['cos_sim'] = cs_list
        data_by_type = data_by_type.sort_values('cos_sim', ascending=False)
        data_by_type = data_by_type[data_by_type.product_name != product_name_search] 

        for n in range(len(data_by_type)):
            output.append(data_by_type.iloc[n])

        df_result = pd.DataFrame(output)[['product_name', 'brand','cos_sim']].head(5)
        
        
        recommendation = df_result.to_numpy().tolist()
        return recommendation

def get_examples():
    df = pd.read_csv('beautyhaulclean.csv')
    examples = df.head(5)['product_name'].to_numpy().tolist()
    return examples
