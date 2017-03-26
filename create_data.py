from BA import *
import pickle
m_list = [1,2,3,4,8,16,32]
N = int(1e5)
data_dict = {} # {m:all_data, all_val, all_freq}

for m in m_list:
    all_data, all_val, all_freq, max_k = create_many(N, m,10)
    data_dict[m] = [all_data, all_val, all_freq, max_k]

with open("FFFBAN5m123481632run10.pickle","w") as f:
    pickle.dump(data_dict,f)


N_list = [int(1e2),int(1e3),int(1e4),int(1e5),int(5e5)]
m = 4
data_dict = {} # {m:all_data, all_val, all_freq}

for N in N_list:
    all_data, all_val, all_freq, max_k = create_many(N, m,100)
    data_dict[N] = [all_data, all_val, all_freq, max_k]

with open("FFFBAN23456m4run100.pickle","w") as f:
    pickle.dump(data_dict,f)