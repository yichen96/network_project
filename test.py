from BA import *
import log_bin_CN_2016 as lb
import matplotlib.pyplot as plt
import numpy as np

# G = BA(int(1e5),3)
# B = BA(int(1e5),3)
# val, freq = degree_frequency(G)
# val2, freq2 = degree_frequency(B)
# data = degree_to_logbin(G)

all_data, all_val, all_freq = create_many(int(1e6),3,2)

c, b = lb.log_bin(all_data,1.,1.,1.5,drop_zeros=True)
# print av_k(G)
plt.loglog(all_val, all_freq, "x", label="Frequency")

plt.loglog(c,b, "r-", label="Log binned")
plt.xlabel("k")
plt.ylabel("Frequency")
plt.legend()
plt.title("N=10^5, m=2, bin_start=1., first_bin_width=1., a=1.4, drop_zeros=True")
plt.show()

def derivative2nd(x):
    if type(x) is list:
        x = np.array(x)
    k = np.gradient(np.gradient(x,edge_order=2),edge_order=2)
    return k


def turning_pt(logbindata, tol=0.3): #get rid of k<100 in the begining too
    if type(logbindata) is list:
        logbindata = np.array(logbindata)
    data = np.log(logbindata)

    d = derivative2nd(data)
    diff = np.diff(d)
    diff = abs(diff)
    a = diff > tol
    a = list(a)
    index = a.index(1) + 1
    return index



