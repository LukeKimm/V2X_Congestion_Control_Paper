import matplotlib.pyplot as plt

data_f = open("V2X_300_0.08.csv",'r', encoding='utf-8-sig')

BSM_TIMEs = []
CBRs = []
WSA_recieved_TIMEs = []
ITTs = []

for line in data_f:
    (bsm_time, cbr, wsa_recieved_time, itt) = line.split(',')
    BSM_TIMEs.append(bsm_time)
    CBRs.append(cbr)
    WSA_recieved_TIMEs.append(wsa_recieved_time)
    ITTs.append(itt)
    
data_f.close()

BSM_TIMEs = [float (i) for i in BSM_TIMEs]
CBRs = [float (i) for i in CBRs]
WSA_recieved_TIMEs = [float (i) for i in WSA_recieved_TIMEs]
# WSA_recieved_TIMEs = [i-1 for i in WSA_recieved_TIMEs]
ITTs = [float (i) for i in ITTs]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

plt.plot(WSA_recieved_TIMEs, ITTs, color='blue', marker='o', linestyle='dashed', label='ITT')
plt.title("ITT stabilizing", fontsize=20)
plt.xlabel("TIME", fontsize=16)
plt.ylabel("ITT", fontsize=16)
plt.ylim([0.07, 0.17])
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.grid(True)
plt.legend(loc='upper left', fontsize=16)
plt.savefig('V2X_300_0.08_ITT.png')