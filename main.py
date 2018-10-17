import sys
from time import time
import MLP
import Dataset



def load_train():
    return

def load_test():
    return

def get_model():
    return

def evaluate():
    return

if __name__ == '__main__':
    t1 = time()
    train_data = load_train()

    model = get_model()

    model.train(train_data)

    test_data = load_test()

    prediction = model.predict(test_data)

    metrics = evaluate(prediction, test_data)

