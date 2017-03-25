from BA import *
import pickle
m_list = [1,2,3,5,10,30]
N = int(1e5)
data_dict = {} # {m:all_data, all_val, all_freq}

for m in m_list:
    all_data, all_val, all_freq, max_k = create_many(N, m,10)
    data_dict[m] = [all_data, all_val, all_freq, max_k]

with open("NewBAN4m12351030run10.pickle","w") as f:
    pickle.dump(data_dict,f)


N_list = [int(1e2),int(1e3),int(1e4),int(1e5)]
m = 3
data_dict = {} # {m:all_data, all_val, all_freq}

for N in N_list:
    all_data, all_val, all_freq, max_k = create_many(N, m,20)
    data_dict[N] = [all_data, all_val, all_freq, max_k]

with open("FinalBAN2345m3.pickle","w") as f:
    pickle.dump(data_dict,f)