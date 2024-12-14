def new_deck():
    cards = []
    for i in range(4):
        for j in range(10):
            cards.append(str(j+1))
    for i in range(12):
        cards.append(str(10))
    return cards


def add(*array):
    total = 0
    for i in array[0]:
        total += int(i)
    return total


def process_aces(permutations, remain):
    possibilities = []
    for j in range(2 ** permutations):
        txt = ''
        numbers = j
        for k in range(permutations):
            if 2 ** (permutations - k) < numbers:
                txt = txt + '1'
                numbers -= 2 ** (permutations - k)
            else:
                txt = txt + '0'
        possibilities.append(txt)
    for j in range(len(possibilities)):
        x = 0
        for k in possibilities[j]:
            if bool(int(k)):
                x += 10
            x += 1
        possibilities[j] = x
    maximum = 0
    for j in possibilities:
        if maximum < j <= remain[0]:
            maximum = j
    return maximum


def scene1():
    import random
    choices = []
    repeat = 10000
    deck = new_deck()
    proceed = False
    pick = 0
    while not proceed:
        pick = input('How many cards? (1-10)')
        try:
            pick = int(pick.strip())
        except ValueError:
            print('Not a valid number')
        else:
            if pick > 10:
                print('Invalid')
            else:
                proceed = True
    remain = 21
    for i in range(pick):
        proceed = False
        while not proceed:
            options = []
            txt = ''
            print("Here are the options:")
            for j in range(10):
                if str(j + 1) in deck:
                    options.append(str(j+1))
                    txt = txt + str(j+1) + ', '
            print(txt)
            choice = str(input('Whats your pick?'))
            choice = choice.strip()
            if choice in options:
                deck.pop(deck.index(choice))
                remain -= int(choice)
                proceed = True
            else:
                print('Invalid')
    for i in range(repeat):
        choices.append(int(deck[random.randint(0, len(deck) - 1)]) > remain)
    total = 0
    for i in choices:
        if i:
            total += 1
    txt = 'There was {} busts out of {}. That\'s {}%'
    print(txt.format(str(total), str(repeat), str(total/len(choices)*100)))


def scene2():
    import random
    counting = []
    repeat = 10000
    for i in range(repeat):
        deck = new_deck()
        total = 0
        count = 0
        while total <= 21:
            pick = random.randint(0, len(deck) - 1)
            total += int(deck[pick])
            count += 1
            deck.pop(pick)
        counting.append(count)
    total = 0
    for i in counting:
        total += i
    total = total/len(counting)
    print('The average is:' + str(total))


def scene3_scene4(scene):
    import random
    counting = []
    repeat = 10000
    proceed = False
    choose = 1
    while not proceed:
        choose = input('How many Cards? (1-10)')
        try:
            choose = int(choose)
        except ValueError:
            print('Invalid')
        else:
            if 1 <= choose <= 10:
                proceed = True
            else:
                print('Invalid')
    for i in range(repeat):
        deck = new_deck()
        total = 0
        remain = 21
        for j in range(choose):
            pick = random.randint(0, len(deck) - 1)
            if j == choose - 1 and deck[pick] == '1' and remain - 11 > 0:
                remain -= 10
            remain -= int(deck[pick])
            deck.pop(pick)
        proceed = False
        if remain < 0:
            counting.append(False)
            continue
        while not proceed:
            pick = random.randint(0, len(deck) - 1)
            if deck[pick] == '1' and 21 >= total + 11 >= 17 and scene == True:
                total += 11
            else:
                total += int(deck[pick])
            if total >= 17:
                proceed = True
            deck.pop(pick)
        counting.append(total > 21 or total < 21 - remain)
    total = 0
    for i in counting:
        if i:
            total += 1
    txt = 'The Dealer lost {} times out of {}. That\'s {}%'
    print(txt.format(str(total), str(repeat), str(total/repeat*100)))


# def scene4():
#     import random
#     counting = []
#     repeat = 10000
#     proceed = False
#     choose = 1
#     while not proceed:
#         choose = input('How many Cards? (1-10)')
#         try:
#             choose = int(choose)
#         except ValueError:
#             print('Invalid')
#         else:
#             if 1 <= choose <= 10:
#                 proceed = True
#             else:
#                 print('Invalid')
#     for i in range(repeat):
#         deck = new_deck()
#         total = 0
#         for j in range(choose):
#             deck.pop(random.randint(0, len(deck) - 1))
#         proceed = False
#         while not proceed:
#             pick = random.randint(0, len(deck) - 1)
#
#             if total >= 17:
#                 proceed = True
#                 counting.append(total > 21)
#             deck.pop(pick)
#     total = 0
#     for i in counting:
#         if i:
#             total += 1
#     txt = 'The Dealer Busted {} times out of {}. That\'s {}%'
#     print(txt.format(str(total), str(repeat), str(total / repeat * 100)))
#




def scene5():
    import random
    counting = []
    repeat = 10000
    proceed = False
    choice = 0
    while not proceed:
        choice = input('Do you want to see the chances of winning under normal circumstances (Incorrect Version), or want to choose cards (Updated Version)? (Select 1 or 2)')
        if choice == '1' or choice == '2':
            proceed = True
        else:
            print('Invalid')
    if choice == '1':
        for i in range(repeat):
            deck = new_deck()
            hands = [[], []]
            remain = [21, 21]
            # 2nd one is dealer
            chances = [0, 0]
            done = [False, False]
            for k in range(2):
                for j in range(len(hands)):
                    pick = random.randint(0, len(deck) - 1)
                    hands[j].append(deck[pick])
                    deck.pop(pick)
            shown = hands[1][random.randint(0, len(hands[0]) - 1)]
            for j in range(len(hands)):
                for k in hands[j]:
                    remain[j] = remain[j] - int(k)
            while (remain[0] > 0 and remain[1] > 0) and not(done[0] and done[1]):
                repeating = 100
                test_deck = new_deck()
                test_deck.remove(shown)
                for j in hands[0]:
                    test_deck.remove(j)
                for j in range(repeating):
                    if remain[0] < int(test_deck[random.randint(0, len(test_deck) - 1)]):
                        chances[0] = chances[0] + 1
                chances[0] = repeating - chances[0]
                if (not done[1] and chances[0] == repeating) or (done[0] and 21 - remain[0] < 17):
                    pick = random.randint(0, len(deck) - 1)
                    hands[0].append(deck[pick])
                    deck.pop(pick)
                    remain[0] = 21
                    done[0] = False
                    permutations = 0
                    for k in hands[0]:
                        if k != '1':
                            remain[0] = remain[0] - int(k)
                        else:
                            permutations += 1
                    maximum = process_aces(permutations, remain)
                    remain[0] = remain[0] - maximum
                    if remain[0] < 0:
                        continue
                else:
                    done[0] = True
                if not 21 >= 21 - remain[1] >= 17:
                    pick = random.randint(0, len(deck) - 1)
                    hands[1].append(deck[pick])
                    deck.pop(pick)
                    remain[1] = 21
                    done[1] = False
                    permutations = 0
                    for k in hands[1]:
                        if k != '1':
                            remain[1] = remain[1] - int(k)
                        else:
                            permutations += 1
                    maximum = process_aces(permutations, remain)
                    remain[1] = remain[1] - maximum
                else:
                    done[1] = True
            if not (remain[0] > 0 and remain[1] > 0):
                counting.append(remain[0] > 0)
            else:
                counting.append(remain[0] < remain[1])
        total = 0
        for i in counting:
            if i:
                total += 1
        total = total/len(counting) * 100
        print('You won an average of ' + str(total) + '%')
    else:
        proceed = False
        pick = 0
        deck = new_deck()
        while not proceed:
            pick = input('How many cards? (1-10)')
            try:
                pick = int(pick.strip())
            except ValueError:
                print('Not a valid number')
            else:
                if pick > 10:
                    print('Invalid')
                else:
                    proceed = True
        remain = 21
        dealer_remain = 21
        for i in range(pick + 1):
            proceed = False
            while not proceed:
                options = []
                txt = ''
                print("Here are the options:")
                for j in range(10):
                    if str(j + 1) in deck:
                        options.append(str(j + 1))
                        txt = txt + str(j + 1) + ', '
                print(txt)
                if not i == pick:
                    choice = str(input('Whats your pick?'))
                else:
                    choice = str(input('Whats your pick for the shown card of the dealer?'))
                choice = choice.strip()
                if choice in options:
                    deck.pop(deck.index(choice))
                    if not i == pick:
                        if choice == '1' and remain > 11:
                            remain -= 10
                        remain -= int(choice)
                    else:
                        if choice == '1' and dealer_remain > 11:
                            dealer_remain -= 10
                        dealer_remain -= int(choice)
                    proceed = True
                else:
                    print('Invalid')
        proceed = False
        bot_choice = 0
        done = [False, False]
        remaining = [remain, dealer_remain]
        while not proceed:
            bot_choice = input('Do you want the bot to hit, stand, or pick randomly? (Select 1, 2, 3)')
            proceed = True
            if not bot_choice == '1' and not bot_choice == '2' and not bot_choice == '3':
                print('Invalid')
                proceed = False
        preserve = []
        for i in deck:
            preserve.append(i)
        for i in range(repeat):
            done[0] = False
            done[0] = False
            remain = remaining[0]
            dealer_remain = remaining[1]
            deck.clear()
            for j in preserve:
                deck.append(j)
            count = 0
            while not (remain < 0 or dealer_remain < 0 or (done[0] and done[1])):
                if (bot_choice == '1' or (bot_choice == '3' and random.randint(0, 1) == 1)) and not remain == 0:
                    pick = random.randint(0, len(deck) - 1)
                    if deck[pick] == '1' and remain - 11 == 0:
                        remain -= 10
                    remain -= int(deck[pick])
                    deck.pop(pick)
                    done[0] = False
                    count += 1
                else:
                    done[0] = True
                if 21 - dealer_remain < 17:
                    pick = random.randint(0, len(deck) - 1)
                    if deck[pick] == '1' and 21 >= dealer_remain - 11 >= 17:
                        dealer_remain -= 10
                    dealer_remain -= int(deck[pick])
                    deck.pop(pick)
                    done[1] = False
                    count += 1
                else:
                    done[1] = True
            if done[0] and done[1]:
                counting.append(21 - remain > 21 - dealer_remain)
            else:
                counting.append(remain > 0)
        total = 0
        for i in counting:
            if i:
                total += 1
        txt = 'You won {} times out of {}. That\'s {}%'
        print(txt.format(str(total), str(repeat), str(total / repeat * 100)))


def scene6():
    import random
    booleans = [True, False]
    counting = []
    repeat = 10000
    for i in range(repeat):
        count = 0
        deck = new_deck()
        hands = [[], []]
        holding = []
        while len(deck) > 0:
            for j in range(len(hands)):
                pick = random.randint(0, len(deck) - 1)
                hands[j].append(deck[pick])
                deck.pop(pick)
        while len(hands[0]) > 0 and len(hands[1]) > 0:
            if int(hands[0][0]) == int(hands[1][0]):
                while int(hands[0][0]) == int(hands[1][0]):
                    count += 1
                    for j in range(len(hands)):
                        holding.append(hands[j][0])
                        hands[j].pop(0)
                    if not(len(hands[0]) > 0 and len(hands[1]) > 0):
                        break
            else:
                count += 1
                for j in range(len(hands)):
                    holding.append(hands[j][0])
                for j in range(len(holding)):
                    pick = random.randint(0, len(holding)-1)
                    hands[booleans.index(int(hands[0][0]) > int(hands[1][0]))].append(holding[pick])
                    holding.pop(pick)
                for j in range(len(hands)):
                    hands[j].pop(0)
        counting.append(count)
    total = 0
    for i in counting:
        total += i
    total = total/len(counting)
    print('You played an average of ' + str(total) + ' rounds before winning')


def scene7(order):
    import random
    counting = []
    repeat = 10000
    if order:
        priority = ['W', 'W4', '2', 'O', 'S', 'C', 'N']
    else:
        priority = ['C', 'N', 'O', 'S', '2', 'W', 'W4']
    for i in range(repeat):
        hands = [[], []]
        deck = []
        discard = []
        per_color = []
        color = ['R', 'Y', 'B', 'G']
        for j in range(10):
            for k in range(2):
                per_color.append(str(j))
        per_color.remove('0')
        per_color.extend(['2', 'O', 'S'])
        for j in color:
            for k in per_color:
                deck.append(j + ',' + k)
        for j in range(8):
            if j >= 4:
                deck.append('W4')
            else:
                deck.append('W')
        for j in range(7):
            for k in range(len(hands)):
                pick = random.randint(0, len(deck) - 1)
                hands[k].append(deck[pick])
                deck.pop(pick)
        turn = random.randint(0, 1)
        pick = 0
        for j in range(10):
            while str(j) in per_color:
                per_color.remove(str(j))
        while pick == 0 or pick in per_color or pick == 'W4' or pick == 'W':
            pick = deck[random.randint(0, len(deck) - 1)]
        discard.append(pick)
        color_choose = pick[0]
        deck.remove(pick)
        while len(hands[0]) > 0 and len(hands[1]) > 0:
            done = False
            while len(deck) < 20:
                pick = random.randint(1, len(discard) - 1)
                deck.append(discard[pick])
                discard.pop(pick)
            for j in priority:
                if j == 'C':
                    options = []
                    for k in hands[turn % 2]:
                        if k[0] == color_choose:
                            options.append(k)
                    if not len(options) == 0:
                        pick = random.randint(0, len(options) - 1)
                        discard.insert(0, options[pick])
                        hands[turn % 2].pop(pick)
                        done = True
                        turn += 1
                        break
                elif j == 'N':
                    options = []
                    for k in hands[turn % 2]:
                        if ',' in k and ',' in discard[0]:
                            if k[k.index(',') + 1] == discard[0][discard[0].index(',') + 1]:
                                options.append(k)
                    if len(options) > 0:
                        color_hand = []
                        color_amount = []
                        for k in color:
                            boolean = False
                            for a in hands[turn % 2]:
                                if ',' in a:
                                    if a[a.index(',') + 1] == discard[0][discard[0].index(',') + 1] and a[0] == k:
                                        boolean = True
                            color_hand.append(boolean)
                        for k in color:
                            count = 0
                            for a in hands[turn % 2]:
                                if a[0] == k:
                                    count += 1
                            color_amount.append(count)
                        indexing = 0
                        for k in range(len(color)):
                            if color_hand[k]:
                                indexing = k
                                break
                        for k in range(len(color)):
                            if color_amount[k] > color_amount[indexing] and color_hand[k]:
                                indexing = k
                        pick = color[indexing] + ',' + discard[0][discard[0].index(',') + 1]
                        discard.insert(0, pick)
                        hands[turn % 2].remove(pick)
                        done = True
                        turn += 1
                        break
                else:
                    if j in per_color:
                        options = []
                        for k in hands[turn % 2]:
                            if len(discard) > 0:
                                if ',' in discard[0] and ',' in k:
                                    if (k[0] == color_choose or discard[0][discard[0].index(',') + 1] == k[k.index(',') + 1]) and k[k.index(',') + 1] == j:
                                        options.append(k)
                        if not len(options) == 0:
                            pick = random.randint(0, len(options) - 1)
                            discard.insert(0, options[pick])
                            hands[turn % 2].pop(pick)
                            done = True
                            if j == '2':
                                for k in range(2):
                                    pick = random.randint(0, len(deck) - 1)
                                    hands[(turn + 1) % 2].append(deck[pick])
                                    deck.pop(pick)
                            break
                    else:
                        options = []
                        for k in hands[turn % 2]:
                            if k[0] == 'W':
                                options.append(k)
                        if len(options) > 0:
                            done = True
                            pick = color_choose
                            while pick == color_choose:
                                pick = color[random.randint(0, len(color) - 1)]
                            color_choose = pick
                            if j == 'W4' and 'W4' in options:
                                pick = 'W4'
                                discard.insert(0, pick)
                                hands[turn % 2].remove(pick)
                                for k in range(4):
                                    pick = random.randint(0, len(deck) - 1)
                                    hands[(turn + 1) % 2].append(deck[pick])
                                    deck.pop(pick)
                            elif j == 'W' and 'W' in options:
                                pick = 'W'
                                discard.insert(0, pick)
                                hands[turn % 2].remove(pick)
            if not done:
                for k in range(2):
                    pick = random.randint(0, len(deck) - 1)
                    hands[turn % 2].append(deck[pick])
                    deck.pop(pick)
        counting.append(len(hands[0]) == 0)
    total = 0
    for i in counting:
        if i:
            total += 1
    txt = 'There was {} wins out of {}. That\'s {}%'
    print(txt.format(str(total), str(repeat), str(total/len(counting)*100)))


def main():
    options = []
    functions = [scene1, scene2, scene3_scene4, scene3_scene4, scene5, scene6, scene7, scene7]
    for i in range(len(functions)):
        options.append(str(i+1))
    while True:
        proceed = False
        choice = ''
        while not proceed:
            print('------------------------------------')
            for i in range(6):
                print(str(i + 1) + ': Scenario ' + str(i + 1))
            print('7: Extra Credit 1')
            print('8: Extra Credit 2')
            choice = input('Which Option?')
            if choice in options:
                proceed = True
        print('You chose option: ' + choice)
        if int(choice) >= 7:
            scene7(int(choice) == 7)
        elif int(choice) == 3 or int(choice) == 4:
            scene3_scene4(int(choice) == 2)
        else:
            functions[int(choice) - 1]()


main()
