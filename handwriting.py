import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def fetch_data(file, sheet='Simple Data'):
    arr = pd.read_excel(file, sheet_name=sheet).values
    time = arr[:, 1].transpose()
    acc = arr[:, 2:5].transpose()
    gyr = arr[:, 5:].transpose()
    return time, acc, gyr


def plot_data(t, a_data, g_data, c=750):
    t = t[:c]
    a_data = a_data[:, :c]
    g_data = g_data[:, :c]
    
    plt.plot(t, a_data[0, :], label='AccX')
    plt.plot(t, a_data[1, :], label='AccY')
    plt.plot(t, a_data[2, :], label='AccZ')
    plt.plot(t, g_data[0, :], label='GyrX')
    plt.plot(t, g_data[1, :], label='GyrY')
    plt.plot(t, g_data[2, :], label='GyrZ')
    
    plt.title('Accerlerometer and Gyroscope Data')
    plt.legend()
    plt.show()


def tremor_index(data):
    l = len(data[0])
    avg = np.zeros((3, l))
    avg[:,0] = data[:,0]
    dev = 0
    for i in range(1, l):
        for j in range(3):
            avgr = data[j, max(0, i-50) : min(l-1, i+50)]
            avg[j,i] = sum(avgr) / len(avgr)
            dev += (avg[j,i] - data[j,i]) ** 2

    #plt.plot(a_data[0], label='Acc')
    #plt.plot(avg[0], label='Average')
    #plt.legend()
    #plt.show()
    return math.sqrt(dev / (3*l))




t, a_data, g_data = fetch_data('15.xlsx')
print(tremor_index(g_data))
#plot_data(t, a_data, g_data)


# PTI = Positional tremor index. RTI = Rotational tremor index.
# High values -> worse tremors -> more severe PD

# Normal
# PTI: 426, 1150, 1171, 1132, 1159
# RTI: 477, 1319, 998, 895, 980

# PD
# PTI: 4231, 7027, 4868, 8994, 5178
# RTI: 2573, 3787, 2933, 5976, 3125
