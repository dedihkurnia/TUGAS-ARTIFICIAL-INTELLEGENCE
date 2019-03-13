import csv

def Keputusan(BANTU, TidakDiBantu):
    return (BANTU*60 + TidakDiBantu*40)/(BANTU+TidakDiBantu)

def Aturan(PendapatantRendah, PendapatantRendahLokal, PendapatantTinggiLokal, PendapatantTinggi, HutangRendah, HutangRendahLokal, HutangTinggiLokal, HutangTinggi):
    BANTU = [0, 0, 0]
    TidakDiBantu = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    if (PendapatantRendah > 0) and (HutangTinggiLokal > 0):
        BANTU[0] = min(PendapatantRendah, HutangTinggiLokal)
    if (PendapatantRendah > 0) and (HutangTinggi > 0):
        BANTU[1] = min(PendapatantRendah, HutangTinggi)
    if (PendapatantRendahLokal > 0) and (HutangRendahLokal > 0):
        TidakDiBantu[0] = min(PendapatantRendahLokal, HutangRendahLokal)
    if (PendapatantRendahLokal > 0) and (HutangTinggiLokal > 0):
        TidakDiBantu[1] = min(PendapatantRendahLokal, HutangTinggiLokal)
    if (PendapatantRendahLokal > 0) and (HutangTinggi > 0):
        BANTU[2] = min(PendapatantRendahLokal, HutangTinggi)
    if (PendapatantTinggiLokal > 0) and (HutangRendah > 0):
        TidakDiBantu[2] = min(PendapatantTinggiLokal, HutangRendah)
    if (PendapatantTinggiLokal > 0) and (HutangRendahLokal > 0):
        TidakDiBantu[3] = min(PendapatantTinggiLokal, HutangRendahLokal)
    if (PendapatantTinggiLokal > 0) and (HutangTinggiLokal > 0):
        TidakDiBantu[4] = min(PendapatantTinggiLokal, HutangTinggiLokal)
    if (PendapatantTinggiLokal > 0) and (HutangTinggi > 0):
        TidakDiBantu[5] = min(PendapatantTinggiLokal, HutangTinggi)   
    if (PendapatantTinggi > 0) and (HutangRendah > 0):
        TidakDiBantu[6] = min(PendapatantTinggi, HutangRendah)
    if (PendapatantTinggi > 0) and (HutangRendahLokal > 0):
        TidakDiBantu[7] = min(PendapatantTinggi, HutangRendahLokal)
    if (PendapatantTinggi > 0) and (HutangTinggiLokal > 0):
        TidakDiBantu[8] = min(PendapatantTinggi, HutangTinggiLokal)
    if (PendapatantTinggi > 0) and (HutangTinggi > 0):
        TidakDiBantu[9] = min (PendapatantTinggi, HutangTinggi)
    if (PendapatantRendah > 0) and (HutangRendah > 0):
        TidakDiBantu[10] = min(PendapatantRendah, HutangRendah)
    if (PendapatantRendahLokal > 0) and (HutangRendah > 0):
        TidakDiBantu[11] = min(PendapatantRendahLokal, HutangRendah)
    if (PendapatantRendah > 0) and (HutangRendahLokal > 0 ):
        TidakDiBantu[12]= min(PendapatantRendah, HutangRendahLokal)
    
    return max(BANTU), max(TidakDiBantu)

def HitungRentang(PENDAPATAN, HUTANG):
    PendapatantRendah, PendapatantRendahLokal, PendapatantTinggiLokal, PendapatantTinggi = 0, 0, 0, 0
    HutangRendah, HutangRendahLokal, HutangTinggiLokal, HutangTinggi = 0, 0, 0, 0 
          
    if(PENDAPATAN <= 0.4):
        PendapatantRendah = 1
    elif (PENDAPATAN > 0.4) and (PENDAPATAN < 0.8):
        PendapatantRendah = (0.8 - PENDAPATAN)/(1.1 - 0.4)
        PendapatantRendahLokal = 1 - PendapatantRendah
    elif (PENDAPATAN == 0.8):
        PendapatantRendahLokal = 1
    elif (PENDAPATAN > 0.8) and (PENDAPATAN < 1.3):
        PendapatantRendahLokal = (1.3 - PENDAPATAN)/(1.3 - 0.8)
        PendapatantTinggiLokal = 1 - PendapatantRendahLokal
    elif (PENDAPATAN == 1.3):
        PendapatantTinggiLokal = 1
    elif (PENDAPATAN > 1.3) and (PENDAPATAN < 1.6):
        PendapatantTinggiLokal = (1.6 - PENDAPATAN)/(1.6 - 1.3)
        PendapatantTinggi = 1- PendapatantTinggiLokal
    elif (PENDAPATAN >= 1.6):
        PendapatantTinggi = 1

    if(HUTANG <= 10):
        HutangRendah = 1
    elif (HUTANG > 10) and (HUTANG < 20):
        HutangRendah = (20 - HUTANG)/(20 - 10)
        HutangRendahLokal = 1 - HutangRendah
    elif (HUTANG == 20):
        HutangRendahLokal = 1
    elif (HUTANG > 20) and (HUTANG < 45):
        HutangRendahLokal = (45 - HUTANG)/(45 - 20)
        HutangTinggiLokal = 1 - HutangRendahLokal
    elif (HutangTinggiLokal == 45):
        HutangTinggiLokal = 1
    elif (HUTANG > 45) and (HUTANG < 50):
        HutangTinggiLokal = (50-HUTANG)/(50-45)
        HutangTinggi = 1 - HutangTinggiLokal
    elif (HUTANG >= 50):
        HutangTinggi = 1
    return PendapatantRendah, PendapatantRendahLokal, PendapatantTinggiLokal, PendapatantTinggi, HutangRendah, HutangRendahLokal, HutangTinggiLokal, HutangTinggi

with open('DataTugas2.csv') as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)
    with open('KEPUTUSAN DATA.csv','w',newline='')as f:
        fieldnames=['DATA YANG BISA DI BANTU', ' PENDAPATAN', ' HUTANG']
        writer=csv.DictWriter(f,fieldnames=fieldnames)
        
        writer.writeheader()
        for row in reader:
            PendapatantRendah, PendapatantRendahLokal, PendapatantTinggiLokal, PendapatantTinggi, HutangRendah, HutangRendahLokal, HutangTinggiLokal, HutangTinggi = HitungRentang(float(row[1]), float(row[2]))
            BANTU, TidakDiBantu = Aturan(PendapatantRendah, PendapatantRendahLokal, PendapatantTinggiLokal, PendapatantTinggi, HutangRendah, HutangRendahLokal, HutangTinggiLokal, HutangTinggi)
            hasil = Keputusan(BANTU, TidakDiBantu)
            if( hasil > 46):
                writer.writerow({'DATA YANG BISA DI BANTU':row[0], ' PENDAPATAN':row[1], ' HUTANG':row[2]})
