#author: Guido Kurz
import random
stats = {
    "Badhand": 0,
    "Pair": 0,
    "Two Pair": 0,
    "Drilling": 0,
    "Vierling": 0,
    "Full House": 0,
    "Straight": 0,
    "Flush": 0,
    "Straight Flush": 0,
    "Royal Flush": 0
}

def ziehung(min, max, wieoft = 5):
    liste = ziehen(min,max,wieoft)
    hand = []

    for i in range(wieoft):
        karte = []
        k = liste[0]
        liste.remove(k)
        f = k % 4
        k = k % 13
        karte.append(f)
        #print(k)
        karte.append(k)
        hand.append(karte)

    checkhand(hand)
    #print(hand)

def checkhand(hand):
    colours = []
    numbers = []

    for i in hand:
        colours.append(i[0])
        numbers.append(i[1])
    maxcol = colours.count(max(colours, key=colours.count))
    maxnum = numbers.count(max(numbers, key=numbers.count))
    numbers.sort()

    if(maxcol==5):
        if((numbers[0]+numbers[1]+numbers[2]+numbers[3]+numbers[4])==50):
            stats["Royal Flush"] += 1
            return
        if(numbers[0]+4 == numbers[-1]):
            stats["Straight Flush"] += 1
            return
        stats["Flush"] += 1
        return

    if(maxnum == 2):
        stats["Pair"] += 1
        return

    if (maxnum == 3):
        if(numbers.count(min(numbers, key=numbers.count)) != 2):
            stats["Drilling"] += 1
        else:
            stats["Full House"] += 1
        return

    if (maxnum == 4):
        stats["Vierling"] += 1
        return

    if (numbers[0] + 4 == numbers[-1]):
        stats["Straight"] += 1
        return

    stats["Badhand"] += 1


def ziehen(min,max,wieoft=5):
    kartennummern = []
    for i in range(min, max + 1):
        kartennummern.append(i)

    for j in range(wieoft):
        index = random.randrange(0, max - min + 1)
        lastposition = len(kartennummern) - 1 - j
        kartennummern[index], kartennummern[lastposition] = kartennummern[lastposition], kartennummern[index]
    #print(kartennummern[-wieoft:])
    return kartennummern[-wieoft:]


if __name__ == '__main__':
    for i in range(1000000):
        ziehung(0,51)
    print(stats)

