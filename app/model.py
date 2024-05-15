import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from main import tg1,targets


###Данный код нужен для найстроки гиперпараметров создает и обучает сам объект модели
targets_visible = targets
df_encoded = pd.get_dummies(targets)
model = RandomForestRegressor(n_estimators=100, random_state=8056, n_jobs=-1, oob_score=True, min_samples_leaf=8)
X_train, X_test, y_train, y_test = train_test_split(df_encoded, tg1, test_size=0.2, random_state=42)
model.fit(X_train, y_train)