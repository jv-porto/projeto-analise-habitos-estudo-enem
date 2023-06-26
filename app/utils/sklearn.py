# importing libraries and functions
import skops.io as sio


# preprocessing
PREPROCESSOR = sio.load('assets/sklearn/preprocessor.skops', trusted=True)


# models
KNN_CLASSIFIER = sio.load('assets/sklearn/models/knn_classifier.skops', trusted=True)
KNN_REGRESSOR = sio.load('assets/sklearn/models/knn_regressor.skops', trusted=True)

LINEAR_REGRESSION = sio.load('assets/sklearn/models/linear_regression.skops', trusted=True)

LOGISTIC_REGRESSION = sio.load('assets/sklearn/models/logistic_regression.skops', trusted=True)

NAIVE_BAYES = sio.load('assets/sklearn/models/naive_bayes.skops', trusted=True)

SVM_CLASSIFIER = sio.load('assets/sklearn/models/svm_classifier.skops', trusted=True)
SVM_REGRESSOR = sio.load('assets/sklearn/models/svm_regressor.skops', trusted=True)

RANDOMFOREST_CLASSIFIER = sio.load('assets/sklearn/models/randomforest_classifier.skops', trusted=True)
RANDOMFOREST_REGRESSOR = sio.load('assets/sklearn/models/randomforest_regressor.skops', trusted=True)
