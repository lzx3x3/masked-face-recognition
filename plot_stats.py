import matplotlib.pyplot as plt
import numpy as np


def plot_loss():
    train_loss = [0.4236, 0.3027, 0.2692, 0.2506, 0.2361, 0.2061, 0.1952, 0.1868, 0.1772, 0.1759, 0.1670, 0.1684, 0.1674, 0.1647, 0.1608, 0.1606, 0.1581, 0.1584, 0.1600, 0.1601]
    test_loss = [0.3242, 0.2624, 0.2510, 0.2389, 0.2255, 0.1884, 0.1808, 0.1806, 0.1740, 0.1713, 0.1681, 0.1660, 0.1647, 0.1660, 0.1639, 0.1643, 0.1602, 0.1623, 0.1594, 0.1581]
    train_loss =   [0.9132, 0.9320, 0.9224, 0.9137, 0.8927, 0.9037, 0.8979, 0.8858, 0.8821, 0.8805, 0.8444, 0.8147, 0.8242, 0.8192, 0.8479, 0.8410, 0.7969, 0.8045, 0.8412, 0.8490, 0.8007, 0.8152, 0.8131, 0.7972, 0.8156, 0.8052, 0.7584, 0.8020, 0.8123, 0.7859, 0.7851, 0.7613, 0.8126, 0.7674, 0.7629, 0.7610, 0.7442, 0.7560, 0.7380, 0.7585, 0.7729, 0.7356, 0.7403, 0.7301, 0.7145, 0.7241, 0.7054, 0.7165, 0.7090, 0.6941, 0.7067, 0.7175, 0.7022, 0.6989, 0.7081, 0.6980, 0.6943, 0.6876, 0.6895, 0.6626, 0.6608, 0.6772, 0.6531, 0.6850, 0.6498, 0.6401, 0.6550, 0.6424, 0.6349, 0.6688, 0.6554, 0.6249, 0.6304, 0.6406, 0.6310, 0.6372, 0.6217, 0.6230, 0.5988, 0.6214, 0.6106, 0.6215, 0.6179, 0.6409, 0.6066, 0.5992, 0.6136, 0.5734, 0.5921, 0.5724, 0.5300, 0.5855, 0.5967, 0.5794, 0.5877, 0.5720, 0.5678, 0.5637, 0.5584, 0.5658]
    test_loss = [0.9678, 0.9486, 0.8738, 0.8727, 0.8957, 0.8890, 0.8669, 0.8536, 0.8679, 0.8228, 0.8005, 0.8073, 0.8205, 0.8045, 0.7937, 0.7962, 0.7921, 0.7792, 0.7848, 0.7872, 0.7737, 0.7722, 0.7797, 0.7652, 0.7567, 0.7639, 0.7628, 0.7581, 0.7493, 0.7417, 0.7425, 0.7399, 0.7327, 0.7400, 0.7433, 0.7326, 0.7185, 0.7208, 0.7135, 0.7048, 0.7177, 0.7185, 0.7106, 0.7108, 0.7030, 0.7073, 0.6966, 0.7074, 0.6934, 0.6954, 0.6969, 0.6893, 0.6851, 0.6834, 0.6854, 0.6874, 0.6825, 0.6720, 0.6718, 0.6732, 0.6644, 0.6630, 0.6600, 0.6688, 0.6504, 0.6625, 0.6431, 0.6545, 0.6483, 0.6362, 0.6372, 0.6309, 0.6174, 0.6172, 0.6198, 0.6217, 0.6114, 0.6265, 0.6291, 0.6043, 0.6176, 0.6046, 0.6054, 0.5849, 0.6043, 0.6058, 0.5857, 0.5790, 0.6066, 0.5722, 0.5721, 0.5849, 0.5834, 0.5851, 0.5862, 0.5791, 0.5636, 0.5620, 0.5673, 0.5532]
    epoch = list(range(1, 101))
    plt.plot(epoch, train_loss, 'r', label="Train Loss")
    plt.plot(epoch, test_loss, 'b', label = "Validation Loss")
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title("Triplet Loss for transfer training on Real World Data")
    plt.legend(loc="upper right")
    plt.show()

def plot_precision_recall():
    precision = [0.9736390578692872, 0.9582747716092762, 0.942850174782538, 0.9289702233250621, 0.9132986877032938, 0.900076472087688, 0.8855387456495489, 0.8706486655329192, 0.8554895638893603, 0.8404785643070788]
    recall = [0.7289501342987271, 0.8493129354976838, 0.9029545719957959, 0.9326949277901048, 0.9509128420724824, 0.9621627934135233, 0.9706489158783915, 0.9765269181361672, 0.9812371053758417, 0.9844680602592549]
    precision_2 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9997337770382696, 0.9990694109918984, 0.9978741907430669, 0.9956]
    recall_2 = [0.0007396161781307174, 0.013858071548133443, 0.06029818210128849, 0.1532951847094087, 0.2833119233913348, 0.4369963797734439, 0.5847249795632372, 0.7104597298454591,0.8040017127953599, 0.8720074740161159]
    plt.plot(recall, precision, 'r', label="Transfer Trained Model")
    
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title("Precision Recall Curve for transfer learning model on masked LFW")
    plt.show()

    plt.plot(recall_2, precision_2, 'b', label="Base Pretrained Model")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title("Precision Recall Curve for base learning model on masked LFW")
    plt.show()
    


def plot_accuracy():
    thresholds = np.arange(0.1, 1.1, 0.1)
    accuracy = [0.8546070302464089, 0.906166063295574, 0.9241114874070614, 0.9306901786756978, 0.9303203705866324, 0.9276733232122698, 0.9225933278835299, 0.9157226828603683, 0.9077426135700105, 0.8988088286815369]
    accuracy_1 = [0.5003698080890654,  0.5069290357740667, 0.5301490910506442, 0.5766475923547043, 0.6416559616956674,  0.718498189886722, 0.7922846354470785, 0.8548989840009342, 0.9011444587177391, 0.9340768422281911]
    
    plt.plot(thresholds, accuracy, 'r', label="Transfer Trained Model")
    # plt.plot(thresholds, accuracy_1, 'b', label="Base Pretrained Model")
    plt.xlabel("Distance Threshold")
    plt.ylabel("Accuracy")
    plt.title("Accuracy of trained model on masked LFW")
    # plt.legend(loc="upper right")
    plt.show()

if __name__ == '__main__':
    plot_loss()
    # plot_precision_recall()
    # plot_accuracy()