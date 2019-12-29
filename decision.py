import csv
from math import log2


def root(node, index):
    m = node[index]
    if m == gain1:
        return miles
    elif m == gain2:
        return speeding
    elif m == gain3:
        return alcohol
    elif m == gain4:
        return distract
    elif m == gain5:
        return accident
    elif m == gain6:
        return insurance


def test(data, quality, index):
    maximum = max(data)
    minimum = min(data)
    sep = (maximum - minimum) / 5
    b1 = minimum
    l1 = b1 + sep
    b2 = l1
    l2 = b2 + sep
    b3 = l2
    l3 = b3 + sep
    b4 = l3
    l4 = b4 + sep
    b5 = l4
    p = 0
    n = 0
    tp = 0
    tn = 0
    test_range = int((len(data) * 70) / 100)
    for i in range(test_range, len(data)):
        if b1 <= data[i] < l1:
            if quality[i] == 1:
                p = p + 1
            else:
                n = n + 1
        if p > 0 and n > 0:
            index = index + 1
            if index > 5:
                tn = tn + 1
                continue
            m = root(node, index)
            test(m, quality, index)
        tp = tp + 1

    for i in range(test_range, len(data)):
        if b2 <= data[i] < l2:
            if quality[i] == 1:
                p = p + 1
            else:
                n = n + 1
        if p > 0 and n > 0:
            index = index + 1
            if index > 5:
                tn = tn + 1
                continue
            m = root(node, index)
            test(m, quality, index)
        tp = tp + 1

    for i in range(test_range, len(data)):
        if b3 <= data[i] < l3:
            if quality[i] == 1:
                p = p + 1
            else:
                n = n + 1
        if p > 0 and n > 0:
            index = index + 1
            if index > 5:
                tn = tn + 1
                continue
            m = root(node, index)
            test(m, quality, index)
        tp = tp + 1
    for i in range(test_range, len(data)):
        if b4 <= data[i] < l4:
            if quality[i] == 1:
                p = p + 1
            else:
                n = n + 1
        if p > 0 and n > 0:
            index = index + 1
            if index > 5:
                tn = tn + 1
                continue
            m = root(node, index)
            test(m, quality, index)
        tp = tp + 1
    for i in range(test_range, len(data)):
        if b5 <= data[i]:
            if quality[i] == 1:
                p = p + 1
            else:
                n = n + 1
        if p > 0 and n > 0:
            index = index + 1
            if index > 5:
                tn = tn + 1
                continue
            m = root(node, index)
            test(m, quality, index)
        tp = tp + 1
    acy = (tp) / (tp + tn)
    return acy


def info_gain(p, n):
    i1 = ((-p) / (p + n)) * (log2(p / (p + n)))
    i2 = (n / (p + n)) * (log2(n / (p + n)))
    i = i1 - i2
    return i


def entropy(dp, dn, p, n, i):
    et = 0
    for j in range(0, 5):
        et = et + ((p[j] + n[j]) / (dp + dn)) * i[j]
    return et


def calculate(data, quality):
    dp = 0
    dn = 0
    p = [0] * len(data)
    n = [0] * len(data)
    maximum = max(data)
    minimum = min(data)
    sep = (maximum - minimum) / 5
    b1 = minimum
    l1 = b1 + sep
    b2 = l1
    l2 = b2 + sep
    b3 = l2
    l3 = b3 + sep
    b4 = l3
    l4 = b4 + sep
    b5 = l4

    for i in range(0, int((len(data) * 70) / 100)):
        p[i] = 0
        n[i] = 0

    for i in range(0, int((len(data) * 70) / 100)):
        if b1 <= data[i] < l1:
            p[0] = p[0] + 1
        else:
            n[0] = n[0] + 1
        if b2 <= data[i] < l2:
            p[1] = p[1] + 1
        else:
            n[1] = n[1] + 1
        if b3 <= data[i] < l3:
            p[2] = p[2] + 1
        else:
            n[2] = n[2] + 1
        if b4 <= data[i] < l4:
            p[3] = p[3] + 1
        else:
            n[3] = n[3] + 1
        if data[i] >= b5:
            p[4] = p[4] + 1
        else:
            n[4] = n[4] + 1
        if quality[i] == 1:
            dp = dp + 1
        else:
            dn = dn + 1

    di = info_gain(dp, dn)
    i = [0] * 10

    for j in range(0, 5):
        if p[j] == 0 or n[j] == 0:
            i[j] = 0
        else:
            i[j] = info_gain(p[j], n[j])

    et = entropy(dp, dn, p, n, i)
    g = di - et
    return g


miles = []
speeding = []
alcohol = []
distract = []
accident = []
insurance = []
quality = []
i = 0

with open('quality_of_drivers.csv', newline='') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        if i != 0:
            miles.append(float(row[1]))
            speeding.append(float(row[2]))
            alcohol.append(float(row[3]))
            distract.append(float(row[4]))
            accident.append(float(row[5]))
            insurance.append(float(row[6]))
            quality.append(int(row[8]))
        i = i + 1

gain1 = float("{0:.2f}".format(calculate(miles, quality)))
gain2 = float("{0:.2f}".format(calculate(speeding, quality)))
gain3 = float("{0:.2f}".format(calculate(alcohol, quality)))
gain4 = float("{0:.2f}".format(calculate(distract, quality)))
gain5 = float("{0:.2f}".format(calculate(accident, quality)))
gain6 = float("{0:.2f}".format(calculate(insurance, quality)))

node = [gain1, gain2, gain3, gain4, gain5, gain6]
node.sort(reverse=True)
accuracy = test(root(node, 0), quality, 0)

accuracy = float("{0:.2f}".format(accuracy * 100))
print("\nAccuracy is: ", accuracy, "%")
