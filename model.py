import pandas as pd
from sklearn import metrics
from sklearn.dummy import DummyClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
import itertools as it


def x_y_split(data_set, target, features):
    X = data_set[features]
    y = data_set[target]
    return X, y

def run_baseline_model(train, validate, target):
    
    # Make Dummy classifier 
    clf = DummyClassifier(strategy="most_frequent")
    
    # Fit Dummy classifier
    clf.fit(X_train, y_train)
    
    # Predict
    y_pred_train = clf.predict(X_train)
    y_pred_val = clf.predict(X_validate)

    scores = []

    output = {
    'features': features,
    'model': 'baseline',
    'train_accuracy': metrics.accuracy_score(y_train, y_train_pred),
    'train_precision': metrics.precision_score(y_train, y_train_pred),
    'train_recall/TPR': metrics.recall_score(y_train, y_train_pred),
    'train_f1': metrics.f1_score(y_train, y_train_pred),
    'validate_accuracy':  metrics.accuracy_score(y_validate, y_val_pred),
    'validate_precision': metrics.precision_score(y_validate, y_val_pred),
    'validate_recall/TPR': metrics.recall_score(y_validate, y_val_pred),
    'validate_f1': metrics.f1_score(y_validate, y_val_pred),
    }
    scores.append(output)
    
    scores_df = pd.DataFrame(scores)
    
