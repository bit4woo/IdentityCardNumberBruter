#python utf-8
#code by bit4
import datetime
import sys

def calculate(identity):
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7,9, 10, 5, 8, 4, 2]
    checkcode = {
    0 : '1',
    1 : '0',
    2 : 'x',
    3 : '9',
    4 : '8',
    5 : '7',
    6 : '6',
    7 : '5',
    8 : '4',
    9 : '3',
    10 : '2'
    }

    sum = 0
    if len(identity) !=18:
        return 0
    else:
        for i in range(0,17): #0-16
            sum = sum + (int(identity[i]) * weight[i])
        identity = "{0}{1}".format(identity, checkcode[(sum%11)])
        return identity

def getDays(year): #1989
    date_list = []
    begin_date = datetime.datetime.strptime(year+"0101", "%Y%m%d")
    end_date = datetime.datetime.strptime(str(int(year)+1)+"0101", "%Y%m%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%m%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    #print date_list
    return date_list



if __name__ == "__main__":
    if len(sys.argv) == 2:
        if len(sys.argv[1]) == 18 and sys.argv[1][10:14] == "****":
            year = sys.argv[1][6:10]
            sum = sys.argv[1][-1]
            #print year
            #print sum
			print "Possible ID card Numbers:"
            for x in getDays(year):
                   ID =calculate(sys.argv[1].replace("****",x))
                   #print ID
                   if str(ID).endswith(sum):
                       print ID
    else:
        print "Please input the Identity Number, example: 4452811995****7041"
