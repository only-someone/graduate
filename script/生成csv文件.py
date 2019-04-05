import csv
import time
import random
from datetime import datetime

def getid():
    with open(r'./MMSI.txt', 'r') as f:
        return str(f.read()).split("\n")

if __name__ == "__main__":
    while True:
        now = datetime.now()
        with open(str(int(time.time()))+".csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)

            '''
            means=["shipinfo", "发电机功率", '主机平均转速','增压器转速','气缸排气量',
                   '气缸冷却水温度','燃料油量','柴油量','活塞冷却水温度','机油温度',
                   '减速箱油压','增压器压强','海水温度','机舱温度', '更新时间']
            writer.writerow(means)#means.to_list().join(','))
            '''


            for userid in getid():
                v1=userid
                v2=str(random.random()*20)[0:6]
                v3=str(2000+random.random()*5000)[0:6]
                v4=str(2000+random.random()*5000)[0:6]
                v5=str(random.random()*50)[0:6]
                v6=str(random.random()*30)[0:6]
                v7=str(500+random.random()*1000)[0:6]
                v8=str(500+random.random()*1000)[0:6]
                v9=str(random.random()*30)[0:6]
                v10=str(70+random.random()*20)[0:6]
                v11=str(50+random.random()*40)[0:6]
                v12=str(50+random.random()*40)[0:6]
                v13=str(20+random.random()*20)[0:6]
                v14=str(25+random.random()*15)[0:6]
                v15=str(now.date())+"/"+str(now.time().hour)+"/"+str(now.time().minute)
                data=[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15]
                writer.writerow(data)
            csvfile.close()
        print("========休息======")
        time.sleep(2800+1600*random.random())