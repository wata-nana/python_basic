# randint関数をインポート
from random import randint


# dice関数の定義
def dice():
    return randint(1, 6)


# 出力確認用
print(dice())
