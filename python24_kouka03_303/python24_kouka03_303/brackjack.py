#ブラックジャックを行う機能
import random,time

def host_card():#ディーラー側のカード
    return [random.randint(1,10),random.randint(1,10)]

def player_card():#プレイヤー側のカード
    return [random.randint(1,10),random.randint(1,10)]

def bj_sum(*person):#カードの合計を求める関数
    if 1 in person:#１のカードがあった場合
        if 10 + sum(person) > 21:
            return [sum(person)]#1を１とした時の合計のみ返す
        else:
            return [sum(person),10+sum(person)]#１，１１どっちのパターンも返す
    else:#１がない場合
        return [sum(person)]

def judge(t,*person):#t=1:バーストしてるかしてないか、t=2:合計が１６を超えているか判断する関数
    if t == 1:
        for i in person:
            if i > 21:
                return False
            else:
                return True
            
    if t == 2:
        if person[0] > 16:
            return False
        else:
            return True


def hit(t,*person):#ヒットの処理を行う関数
    person = list(person)
    if t == 1:#プレイヤー側のヒットの処理
        person.append(random.randint(1,10))
        print(f">>{person}",end =" ")
        print(f"合計：{bj_sum(*person)}")
        return person
    
    if t == 2:#ディーラー側のヒットの処理
        if judge(2,max(bj_sum(*person))) == False:#既に１６を超えていた場合
            return person
        else:
            while True:#16を超えるまでカードを引く
                person.append(random.randint(1,10))
                print(f">>{person}",end=" ")
                print(f"合計：{bj_sum(*person)}")
                time.sleep(1)
                for i in bj_sum(*person):
                    if i > 16:
                        return person
                        break
                    else:
                        continue