added = {}
grouped = {}
appointments = [
    {"doctor": "Dr. Can", "time": "09:00", "patient": "Ali"},
    {"doctor": "Dr. Ece", "time": "09:15", "patient": "Ayşe"},
    {"doctor": "Dr. Mert", "time": "09:30", "patient": "Mehmet"},
    {"doctor": "Dr. Selin", "time": "09:45", "patient": "Zeynep"},
    {"doctor": "Dr. Kerem", "time": "10:00", "patient": "Ahmet"},
    {"doctor": "Dr. Can", "time": "10:15", "patient": "Elif"},
    {"doctor": "Dr. Ece", "time": "10:30", "patient": "Burak"},
    {"doctor": "Dr. Mert", "time": "10:45", "patient": "Deniz"},
    {"doctor": "Dr. Selin", "time": "11:00", "patient": "Cem"},
    {"doctor": "Dr. Kerem", "time": "11:15", "patient": "Selma"},

    {"doctor": "Dr. Can", "time": "11:30", "patient": "Yusuf"},
    {"doctor": "Dr. Ece", "time": "11:45", "patient": "Ece"},
    {"doctor": "Dr. Mert", "time": "12:00", "patient": "Hakan"},
    {"doctor": "Dr. Selin", "time": "12:15", "patient": "Seda"},
    {"doctor": "Dr. Kerem", "time": "12:30", "patient": "Canan"},
    {"doctor": "Dr. Can", "time": "12:45", "patient": "Furkan"},
    {"doctor": "Dr. Ece", "time": "13:00", "patient": "Fatma"},
    {"doctor": "Dr. Mert", "time": "13:15", "patient": "Okan"},
    {"doctor": "Dr. Selin", "time": "13:30", "patient": "Kemal"},
    {"doctor": "Dr. Kerem", "time": "13:45", "patient": "Derya"},

    {"doctor": "Dr. Can", "time": "14:00", "patient": "Berk"},
    {"doctor": "Dr. Ece", "time": "14:15", "patient": "Nisa"},
    {"doctor": "Dr. Mert", "time": "14:30", "patient": "Melis"},
    {"doctor": "Dr. Selin", "time": "14:45", "patient": "Serkan"},
    {"doctor": "Dr. Kerem", "time": "15:00", "patient": "Gamze"},
    {"doctor": "Dr. Can", "time": "15:15", "patient": "Tuna"},
    {"doctor": "Dr. Ece", "time": "15:30", "patient": "Leyla"},
    {"doctor": "Dr. Mert", "time": "15:45", "patient": "Onur"},
    {"doctor": "Dr. Selin", "time": "16:00", "patient": "Gizem"},
    {"doctor": "Dr. Kerem", "time": "16:15", "patient": "Sibel"},

    {"doctor": "Dr. Can", "time": "16:30", "patient": "Barış"},
    {"doctor": "Dr. Ece", "time": "16:45", "patient": "Buse"},
    {"doctor": "Dr. Mert", "time": "17:00", "patient": "Kaan"},
    {"doctor": "Dr. Selin", "time": "17:15", "patient": "Yasemin"},
    {"doctor": "Dr. Kerem", "time": "17:30", "patient": "Volkan"},
    {"doctor": "Dr. Can", "time": "17:45", "patient": "Emre"},
    {"doctor": "Dr. Ece", "time": "18:00", "patient": "Eda"},
    {"doctor": "Dr. Mert", "time": "18:15", "patient": "Tolga"},
    {"doctor": "Dr. Selin", "time": "18:30", "patient": "Sevgi"},
    {"doctor": "Dr. Kerem", "time": "18:45", "patient": "Kübra"},

    {"doctor": "Dr. Can", "time": "19:00", "patient": "Arda"},
    {"doctor": "Dr. Ece", "time": "19:15", "patient": "Merve"},
    {"doctor": "Dr. Mert", "time": "19:30", "patient": "Cihan"},
    {"doctor": "Dr. Selin", "time": "19:45", "patient": "Suna"},
    {"doctor": "Dr. Kerem", "time": "20:00", "patient": "Hüseyin"},
    {"doctor": "Dr. Can", "time": "20:15", "patient": "Ezgi"},
    {"doctor": "Dr. Ece", "time": "20:30", "patient": "Alper"},
    {"doctor": "Dr. Mert", "time": "20:45", "patient": "Şule"},
    {"doctor": "Dr. Selin", "time": "21:00", "patient": "Orhan"},
    {"doctor": "Dr. Kerem", "time": "21:15", "patient": "Sinem"},

    {"doctor": "Dr. Can", "time": "21:30", "patient": "Halil"},
    {"doctor": "Dr. Ece", "time": "21:45", "patient": "Naz"},
    {"doctor": "Dr. Mert", "time": "22:00", "patient": "Gökhan"},
    {"doctor": "Dr. Selin", "time": "22:15", "patient": "Aylin"},
    {"doctor": "Dr. Kerem", "time": "22:30", "patient": "Rıza"},
    {"doctor": "Dr. Can", "time": "22:45", "patient": "Pelin"},
    {"doctor": "Dr. Ece", "time": "23:00", "patient": "Kadir"},
    {"doctor": "Dr. Mert", "time": "23:15", "patient": "Esra"},
    {"doctor": "Dr. Selin", "time": "23:30", "patient": "Tamer"},
    {"doctor": "Dr. Kerem", "time": "23:45", "patient": "Filiz"},

    {"doctor": "Dr. Can", "time": "08:00", "patient": "İsmail"},
    {"doctor": "Dr. Ece", "time": "08:15", "patient": "Damla"},
    {"doctor": "Dr. Mert", "time": "08:30", "patient": "Umut"},
    {"doctor": "Dr. Selin", "time": "08:45", "patient": "Serra"},
    {"doctor": "Dr. Kerem", "time": "09:00", "patient": "Yunus"},
    {"doctor": "Dr. Can", "time": "09:15", "patient": "İrem"},
    {"doctor": "Dr. Ece", "time": "09:30", "patient": "Samet"},
    {"doctor": "Dr. Mert", "time": "09:45", "patient": "Hale"},
    {"doctor": "Dr. Selin", "time": "10:00", "patient": "Murat"},
    {"doctor": "Dr. Kerem", "time": "10:15", "patient": "Suat"},

    {"doctor": "Dr. Can", "time": "10:30", "patient": "Ferhat"},
    {"doctor": "Dr. Ece", "time": "10:45", "patient": "Şeyma"},
    {"doctor": "Dr. Mert", "time": "11:00", "patient": "Baran"},
    {"doctor": "Dr. Selin", "time": "11:15", "patient": "Seçil"},
    {"doctor": "Dr. Kerem", "time": "11:30", "patient": "Bora"},
    {"doctor": "Dr. Can", "time": "11:45", "patient": "Eren"},
    {"doctor": "Dr. Ece", "time": "12:00", "patient": "Nehir"},
    {"doctor": "Dr. Mert", "time": "12:15", "patient": "Sarp"},
    {"doctor": "Dr. Selin", "time": "12:30", "patient": "Deniz"},
    {"doctor": "Dr. Kerem", "time": "12:45", "patient": "Yelda"}
]
for item in appointments:
    dr = item["doctor"]
    if dr not in grouped:
        grouped[dr] = []
    zaman = item["time"]
    hasta = item["patient"]
    eklenecek_data = {
        "time": item["time"],
        "patient": item["patient"]
    }
    if dr not in added:
        added[dr] = [eklenecek_data]
    else:
        added[dr].append(eklenecek_data)
print(added)
