'''Lab_RockPaperScissor'''
def rock(str_s, list_n, score_a, score_b):
    '''return win or draw'''
    for i in xrange(0, len(str_s), 2):
        list_n.append(str_s[i]+str_s[i+1])
    #print list_n
    for i in xrange(len(list_n)):
        if list_n[i] == 'PR' or list_n[i] == 'SP' or list_n[i] == 'RS':
            score_a += 1
        elif list_n[i] == 'RP' or list_n[i] == 'PS' or list_n[i] == 'SR':
            score_b += 1
    if score_a > score_b:
        return 'A win ' + str(score_a) + '-' + str(score_b)
    elif score_b > score_a:
        return 'B win ' + str(score_b) + '-' + str(score_a)
    return 'DRAW ' + str(score_a)
print 'ac'
print rock(raw_input(), [], 0, 0)