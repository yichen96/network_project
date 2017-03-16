from BA import *
import log_bin_CN_2016 as lb
import matplotlib.pyplot as plt
import numpy as np

G = BA(int(1e5),3)
B = BA(int(1e5),3)
val, freq = degree_frequency(G)
val2, freq2 = degree_frequency(B)
data = degree_to_logbin(G)

c, b = lb.log_bin(data,3.,1.,1.5,drop_zeros=True)
print av_k(G)
plt.loglog(val, freq, "x", label="Frequency")
plt.loglog(val2, freq2, ".", label="Frequency")
plt.loglog(c,b, "r-", label="Log binned")
plt.xlabel("k")
plt.ylabel("Frequency")
plt.legend()
plt.title("N=10^5, m=2, bin_start=1., first_bin_width=1., a=1.4, drop_zeros=True")
plt.show()