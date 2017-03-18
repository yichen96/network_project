from BA import *
import pickle
m_list = [1,2,3,4,5]
N = int(1e6)
data_dict = {} # {m:all_data, all_val, all_freq}

for m in m_list:
    all_data, all_val, all_freq = create_many(N, m)
    data_dict[m] = [all_data, all_val, all_freq]

with open("BAdata1time.pickle","w") as f:
    pickle.dump([data_dict],f)
