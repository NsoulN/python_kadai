#チャットボット本体
from datetime import datetime,time
import re,to_wareki,brackjack
import time as tm
try:#時間によってエラーになるため例外処理
    import wheather
except:
    print("※天気情報の更新中につき、ただ今天気情報をお答えすることができません")

def warikan(price,people):#割り勘計算機能
        result = int(price)/int(people)
        return result
    
def hello():#時間に沿った挨拶を返す機能
    tm = datetime.now().time()
    if time(5,0) <= tm < time(12,0):
        return "おはようごさいます"
    elif time(12,0) <= tm < time(19,0):
        return "こんにちは"
    else:
        return "こんばんは"

#反応する言葉のパターン
pattern1 = '[1-9][0-9][0-9][0-9]年.*和暦.*'#西暦から和暦を求める機能
pattern2 = '天気.*'#天気を答える機能
pattern3 = 'おはよう|こんにちは|こんばん(は|わ)'#あいさつを返す機能
pattern4 = 'ゲーム.*'#ブラックジャックで遊ぶ機能
pattern5 = '割り勘.*'#割り勘機能


#チャットボット
name = str(input("お名前を教えてください>>"))
print(f"{name}さん、{hello()}")
while True:
        text = input("ご用件は何でしょう？>>")

        #パターンマッチ
        result1 = re.match(pattern1,text)
        result2 = re.match(pattern2,text)
        result3 = re.match(pattern3,text)
        result4 = re.match(pattern4,text)
        result5 = re.match(pattern5,text)

#各機能の処理
#-----------------------西暦から和暦を求める機能--------------------------------------
        if result1:
            Year = re.findall("[1-9][0-9][0-9][0-9]",text)#入力から西暦の部分を取得
            wareki = to_wareki.transyear(int(Year[0]))
            if wareki == None or int(Year[0]) > datetime.now().year:#明治以前の西暦だった場合の処理
                print("すみません。対応していません")
            else:
                print(f"{Year[0]}年は{wareki}です。")

#-----------------------天気を答える機能----------------------------------------------
        elif result2:
            try:
                print("福井県の天気を教えます。")
                print(f"{datetime.now().month}月{datetime.now().day}日今日の天気は、{wheather.today_weather}")
                print(f"現在の気温は{wheather.latest_temp}度です。")
                print(f"また、明日の天気は{wheather.tommorow_weather}")
                print(f"最高気温は{wheather.max_tommorow_temp}度、\n最低気温は{wheather.min_tommorow_temp}度です。")
                print("\n天気の概況について教えます。")
                print(wheather.overview_forecast_text)
            except:
                print("天気情報を更新中です。しばらく待ってからお聞きください。")

        #あいさつを返す機能
        elif result3:
            print(name + "さん" + hello())

#-----------------------ブラックジャックを行う機能-------------------------------------
        elif result4:
            #ブラックジャック説明
            print("では、簡単なブラックジャックをしましょう。")
            tm.sleep(1)
            print("最初に私のカード、次にあなたのカードが表示されます。")
            tm.sleep(1)
            print("次に「ヒット(カードを引く)しますか？」と聞くのでy(yes)かn(no)を入力してください")
            tm.sleep(1)
            print("nを入力した後、私のターンが来ます")
            tm.sleep(1)
            print("私は数字の合計が16を超えるまで引き続けます")
            tm.sleep(1)
            print("数字の合計が21に近い方が勝ち、21を超えた場合負けとなります")
            tm.sleep(1)
            while True:
                ans = input("よろしいですか?(よろしい場合[y]と入力してください)>>")
                if ans == "y":
                    print("では始めます\n")
                    break
                else:
                    print("yと入力してください")
            
            #ブラックジャック開始
            host_card = brackjack.host_card()#ディーラー（チャットボット側）のカード
            player_card = brackjack.player_card()#プレイヤー（ユーザ側)のカード
            tm.sleep(1)

            print("私の手札>>",end="")
            print(host_card,end=" ")
            print(f"合計：{brackjack.bj_sum(*host_card)}\n")

            print(name + "さんの手札>>",end="")
            print(player_card,end=" ")
            print(f"合計：{brackjack.bj_sum(*player_card)}\n")

            #プレイヤーターンの処理
            while True:
                ans = input("ヒットしますか？(y/n)>>")
                if ans == "y":#ヒット（カードを引く）したとき
                    player_card = brackjack.hit(1,*player_card)
                    if brackjack.judge(1,*brackjack.bj_sum(*player_card)) == False:#バーストしたときの処理
                        print("21を超えました。バーストです。")
                        player_card = 0#最後の勝敗の判断のために0としています
                        break

                elif ans == "n":#スタンド(カードを引かない)したとき
                    player_card = max(brackjack.bj_sum(*player_card))
                    break

            #ディーラーターンの処理
            print("では、私のターンです。")
            host_card = brackjack.hit(2,*host_card)#合計が17以上になるまでの処理
            if brackjack.judge(1,*brackjack.bj_sum(*host_card)) == True:#合計が21以下だった時の処理
                print("16を超えました。スタンドです。")
                host_card = max(brackjack.bj_sum(*host_card))
            else:#バーストした時の処理
                print("バーストしました。")
                host_card = 1#互いにバーストしたときは、ディーラーが勝つので0ではなく1としています

            if host_card == 1:
                h_result = "バースト"
            else:
                h_result = host_card
            
            if player_card == 0:
                p_result = "バースト"
            else:
                p_result = player_card
            
            tm.sleep(1)
            print(f"結果：私>{str(h_result)} {name}さん>{str(p_result)}")
            tm.sleep(1)

            #勝敗判断
            if host_card > player_card:
                print("私の勝ちです！やったー！")
            elif host_card < player_card:
                print(f"{name}さんの勝ちです。おめでとうございます")
            else:
                print("引き分けです")
        
#------割り勘機能---------------------------------
        elif result5:
            price = input("価格はいくらですか(整数で)>>")
            people = input("何人で割り勘しますか(整数で)>>")
            try:
                print(f"一人当たり{warikan(price,people)}円です")
            except ZeroDivisionError:
                print("0で割ろうとしています")
            except ValueError:
                print("整数以外が入力されました")

#-------------会話を終了するときの処理--------------------------------
        elif text == "さよなら" or text == "さようなら":
            print("さようなら。お元気で")
            break

#-------------想定されていない質問を受け取ったときの処理---------------
        else:
            print("すみませんよくわかりません。")
