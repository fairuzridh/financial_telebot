from models import Transaction

category_mapping = [
    ["Gaji", "Upah Tambahan"],
    ["Kuliah", "Kosan"],
    ["Listrik", "Wifi", "Orang Tua"],
    ["Makan", "Transport", "Kuota Internet"],
    ["Rokok", "Netflix", "Hiburan"],
    ["Tabungan","Dana Darurat"]
]

category_mapping_2 = [[
        {"name" : "Gaji", "status" : "1"},
        {"name" : "Upah Tambahan", "status" : "1"}
    ],[
        {"name" : "Kuliah", "status" : "2"},
        {"name" : "Kosan", "status" : "2"},
    ],[
        {"name" : "Listrik", "status" : "2"},
        {"name" : "Wifi", "status" : "2"},
        {"name" : "Orang Tua", "status" : "2"},
    ],[
        {"name" : "Makan", "status" : "2"},
        {"name" : "Transport", "status" : "2"},
        {"name" : "Kuota Internet", "status" : "2"},
    ],[
        {"name" : "Rokok", "status" : "2"},
        {"name" : "Netflix", "status" : "2"},
        {"name" : "Hiburan", "status" : "2"},
    ],[
        {"name" : "Tabungan", "status" : "3"},
        {"name" : "Dana Darurat", "status" : "3"}
]]

instrument_mapping = [
    {"name" : "Cash"},
    {"name" : "BCA"},
    {"name" : "Mandiri"},
    {"name" : "Dana"},
    {"name" : "LinkAja"}
]

transaction_data = [
    Transaction(
        id=1, 
        tele_id=1851975506, 
        created_date="2024-06-01", 
        category=category_mapping[3][0], 
        description="Makan siang di Warteg", 
        nominal=15000, 
        instrument=instrument_mapping[0]["name"]
    ),
    Transaction(
        id=2, 
        tele_id=1851975506, 
        created_date="2024-06-02", 
        category=category_mapping[0][0], 
        description="Salary Bulan June", 
        nominal=4000000, 
        instrument=instrument_mapping[1]["name"]
    )
]
