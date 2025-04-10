#西暦から和暦を求める機能
def transyear(year):
    #各和暦の区切りとなる年
    wareki = {
    "令和":2019,
    "平成":1989,
    "昭和":1926,
    "大正":1912,
    "明治":1868,
}

    if wareki["令和"] <= year:
        year -= wareki["令和"] - 1
        if year == 1:
            return "令和元年"
        else:
            return f"令和{year}年"
        
    if wareki["平成"] <= year:
        year -= wareki["平成"] - 1
        if year == 1:
            return "平成元年"
        else:
            return f"平成{year}年"
        
    if wareki["昭和"] <= year:
        year -= wareki["昭和"] - 1
        if year == 1:
            return "昭和元年"
        else:
            return f"昭和{year}年"
        
    if wareki["大正"] <= year:
        year -= wareki["大正"] - 1
        if year == 1:
            return "大正元年"
        else:
            return f"大正{year}年"
        
    if wareki["明治"] <= year:
        year -= wareki["明治"] - 1
        if year == 1:
            return "明治元年"
        else:
            return f"明治{year}年"