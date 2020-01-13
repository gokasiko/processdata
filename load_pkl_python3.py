import pickle


data = pickle.load(open("WebQSP_gold_data_test.pkl", 'rb'), encoding="ascii")
print(data)
