import joblib

def save_model(model, path='outputs/model.pkl'):
    joblib.dump(model, path)
