import json

datapath_train = "RL_train_TR_sub.question"
with open(datapath_train, "r", encoding='UTF-8') as webQaData:
    train_inputDict = {}
    test_inputDict = {}
    load_dict = json.load(webQaData)
    for key, value in load_dict.items():
        if key.startswith("WebQTrn"):
            train_inputDict.update()

