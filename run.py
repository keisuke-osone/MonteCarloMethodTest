# coding: UTF-8
import random

# 同じ相手と一定数以上当たった数
overNum = 0;

# モンテカルロシミュレーションの試行回数	
trials = 100000
# 試合数
games = 100
# 対戦相手の数
opponentPlayersNumber = 454
# 当たった数
times = 3

for i in range(trials):
	# リストの初期化
	opponentPlayers = [0] * opponentPlayersNumber # 0で初期化された要素が対戦相手数分のリスト
	
	# print 'challenge number is %s'% i
	for j in range(games):  # lenでリストの要素数を求める, rangeにループ回数(回数分の要素のリストが戻り値), inはリストをとる
	    opponent = random.randint(0,(opponentPlayersNumber - 1));
	    # print '%s game opponent player is No.%s'%(j, opponent)
	    opponentPlayers[opponent] += 1
	if max(opponentPlayers) >= times:
		overNum += 1
print overNum
print trials
print '確率は%s％'%(100 * float(overNum) / trials)
print '期待値は%s人'%((100 * float(overNum) / trials) * (opponentPlayersNumber + 1))
