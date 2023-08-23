import matplotlib.pyplot as plt

data_f = open("V2X_400_0.16.csv",'r', encoding='utf-8-sig')

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
WSA_recieved_TIMEs = [i-1 for i in WSA_recieved_TIMEs]
ITTs = [float (i) for i in ITTs]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

plt.plot(BSM_TIMEs, CBRs, color='magenta', marker='o', linestyle='dashed', label='CBR')
plt.title("CBR stabilizing", fontsize=20)
plt.xlabel("TIME", fontsize=16)
plt.ylabel("CBR", fontsize=16)
plt.grid(True)
plt.legend(loc='upper left', fontsize=16)
plt.savefig('V2X_400_0.16_CBR.png')