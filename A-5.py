bob_info = ["Bob", "Dylan", 79]

# str.formatを用いた要素出力繰り返し
profile = "Name: {} {}, Age: {}".format(*bob_info)
print(profile)
