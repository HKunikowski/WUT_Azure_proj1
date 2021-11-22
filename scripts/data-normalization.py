import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, OrdinalEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer

def azureml_main(dataframe1 = None, dataframe2 = None):
	encode_cols = {"Sex": {"M": 1, "F": 0}, 
	"ExerciseAngina": {True: 1, False: 0 }}
	preprocessor = ColumnTransformer(
    transformers = [
        ('onehotcat', OneHotEncoder(), ['ChestPainType', 'ST_Slope', 'RestingECG']),
        ('num', MinMaxScaler(), ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']),
    ],
    remainder = 'passthrough'
	)
	features = ['x0_ASY', 'x0_ATA', 'x0_NAP', 'x0_TA', 'x1_Down', 'x1_Flat', 'x1_Up', 'x2_LVH', 'x2_Normal', 'x2_ST', 'Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak', 'Sex', 'FastingBS', 'ExerciseAngina', 'HeartDisease'] 
	dataframe = dataframe1.replace(encode_cols)
	dataframe = pd.DataFrame(preprocessor.fit_transform(dataframe), columns=features)
	return dataframe