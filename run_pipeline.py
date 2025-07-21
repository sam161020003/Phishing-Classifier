from src.load_data import load_data
from src.preprocessing import preprocess_data
from src.train_model import train_and_evaluate
from src.save_model import save_model

def main():
    df = load_data('data/raw/phishing_data.csv')
    X_train, X_test, y_train, y_test = preprocess_data(df)
    model, acc = train_and_evaluate(X_train, X_test, y_train, y_test)
    print(f"Accuracy: {acc:.4f}")
    save_model(model)

if __name__ == "__main__":
    main()
