#天気を答える機能

'''
チャットボットでつかう変数
latest_temp 現在の気温
today_weather 今日の天気
max_tommorow_temp 明日の最高気温
min_tommorow_temp 明日の最低気温
tommorow_weather 明日の天気
overview_forecast_text 天気概況
'''

import requests
from datetime import datetime

def find_index(data:list, code:str) -> int:
  """
  対象のエリアのデータが格納されているインデックス番号を返す
  input : list
  return : int
  """
  index = [num for num, i in enumerate(data) if i["area"]["code"] == code][0]
  return index

latest_time = datetime.now()
yyyymmdd = latest_time.strftime('%Y%m%d') # 年月日　- アメダスデータ取得時に必要
h3 = ("0" + str((latest_time.hour//3)*3))[-2:] # 3時間ごとの時間 - アメダスデータ取得時に必要
area = "180000" # エリア番号 
detail_area = "180010" # 詳細の予報エリア番号
stnid = "57066" # 観測所番号

# 天気概況
overview_forecast_url = f"https://www.jma.go.jp/bosai/forecast/data/overview_forecast/{area}.json"
overview_forecast_req = requests.get(overview_forecast_url)
overview_forecast_data = overview_forecast_req.json() # 天気概況
overview_forecast_text = "\n".join(overview_forecast_data["text"].split())

# 天気予報
forecast_url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{area}.json"
forecast_req = requests.get(forecast_url)
forecast_data = forecast_req.json()
w_forecast_data = forecast_data[0]["timeSeries"][0]["areas"] #エリア毎の予報データ（天気, 風速, 風向...etc）が格納
t_forecast_data = forecast_data[0]["timeSeries"][2]["areas"]#エリア毎の予報データ（気温）が格納
w_forecast_data_target_index = find_index(w_forecast_data, detail_area)
weathers = w_forecast_data[w_forecast_data_target_index]["weathers"] # 天気
t_forecast_data_target_index = find_index(t_forecast_data,stnid)
temps = t_forecast_data[t_forecast_data_target_index]["temps"]#気温
today_weather = " ".join(weathers[0].split())
tommorow_weather = " ".join(weathers[1].split())
max_tommorow_temp = temps[3]
min_tommorow_temp = temps[2]

# アメダス
amedas_url = f"https://www.jma.go.jp/bosai/amedas/data/point/{stnid}/{yyyymmdd}_{h3}.json"
amedas_req = requests.get(amedas_url)
amedas_data = amedas_req.json()
latest_key = max(amedas_data) # 最新のアメダスデータが入っているキー
latest_temp = str(amedas_data[latest_key]["temp"][0]) # 最新の気温データを取得