# importing libraries and functions
from fastapi import APIRouter, Request
import re
import json
import skops.io as sio
import pandas as pd

from utils import sklearn


# instantiating the router
router = APIRouter(prefix='/api')


# index test route
@router.get('/')
async def get_index():
    return 'OK'


# student analysis route
@router.post('/analyze_student')
async def post_analyze_student(request: Request):
    request_content = await request.json()
    X = pd.DataFrame.from_dict(request_content).T

    X_transformed = sklearn.PREPROCESSOR.transform(X)
    X_transformed = pd.DataFrame(X_transformed, columns=[re.sub(r'.+__', '', item) for item in sklearn.PREPROCESSOR.get_feature_names_out()], index=X.index)
    X_transformed = X_transformed.drop(columns=['PARTICIPANTE_TP_SEXO_M'])

    preds = {
        'knn_classifier': sklearn.KNN_CLASSIFIER.predict(X_transformed),
        'knn_regressor': sklearn.KNN_REGRESSOR.predict(X_transformed),
        'linear_regression': sklearn.LINEAR_REGRESSION.predict(X_transformed),
        'logistic_regression': sklearn.LOGISTIC_REGRESSION.predict(X_transformed),
        'naive_bayes': sklearn.NAIVE_BAYES.predict(X_transformed),
        'svm_classifier': sklearn.SVM_CLASSIFIER.predict(X_transformed),
        'svm_regressor': sklearn.SVM_REGRESSOR.predict(X_transformed),
        'randomforest_classifier': sklearn.RANDOMFOREST_CLASSIFIER.predict(X_transformed),
        'randomforest_regressor': sklearn.RANDOMFOREST_REGRESSOR.predict(X_transformed),
    }
    preds = pd.DataFrame(preds, index=X_transformed.index)

    classifiers = ['knn_classifier', 'logistic_regression', 'naive_bayes', 'svm_classifier', 'randomforest_classifier']
    regressors = ['knn_regressor', 'linear_regression', 'svm_regressor', 'randomforest_regressor']

    preds = preds.apply(lambda column: round(column, 2), axis=0)

    preds['classifiers_summary'] = preds.apply(lambda row: int(pd.Series([row[classifier] for classifier in classifiers]).mode()), axis=1)
    preds['regressors_summary'] = preds.apply(lambda row: round(pd.Series([row[regressor] for regressor in regressors]).mean(), 2), axis=1)


    return json.loads(preds.to_json(orient='index'))
