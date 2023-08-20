list1 = [5484,
5489,
5500,
5501,
5502,
5703,
5744,
5745,
1030,
1031,
1792,
5406,
5412,
5414,
5416,
5440,
5442,
5454,
5456,
5461,
5530,
5656,
5660,
5724,
5775,
2281,
2283,
5405,
5417,
5420,
5429,
5433,
5434,
5443,
5460,
5464,
5468,
5480,
5506,
5508,
5512,
5586,
5725,
5183,
5184,
5361,
5362,
5531,
5532,
5537,
5468,
9863,
5472,
5470,
5595,
5596,
5668,
5513,
5667,
5666,
5707,
5659,
5658,
5743,
5742,
5770,
5548,
5547,
5515,
5514,
5739,
9890]



while True:
    name = input("Enter recloser number: ")

    if name =='e' or name == 'E':
        print('Exiting aplication')
        break


    recloser = int(name)
    if recloser in list1:
        print(f'{recloser} is in the existing single line. DO NOT REMOVE')
    else:
        print(f'{recloser} not in single line. CAN BE COMMENTED OUT')

