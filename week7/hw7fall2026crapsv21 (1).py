# CH200 Introduction to Computers & Programming
# Prof. Dalkilic @ IU Bloomington
# Homework 7 Fall 2026 Craps
# Information Header

import random as rn

def roll_die(dice_throws):
    d1 = rn.randint(1, 6)
    d2 = rn.randint(1, 6)
    dice_throws.append((d1,d2))
    total = sum((d1, d2))
    return total

def craps():
    history = []
    dice_throws = []
    while True:
        show = roll_die(dice_throws)
        history.append(show)
        if show in [7, 11]:
            history.append("wins")
            break
        elif show in [2, 3, 12]:
            history.append("loses")
            break
        else:
            point = show
            while True:
                show = roll_die(dice_throws)
                history.append(show)
                if show == 7:
                    history.append("loses")
                    break
                elif show == point:
                    history.append("wins")
                    break
        break

    return history,dice_throws

def gamble(starting_bankroll, wager, target_bankroll):
    bankroll = starting_bankroll
    session_log = []
    cnt = 0               # for counting throws   

    while True:
        # check stop conditions before rolling
        if bankroll <= 0:
            session_log.append("Busted!")
            break
        if bankroll >= target_bankroll:
            session_log.append("Doubled!")
            break
            
        # adjust wager if player has less than their standard bet left
        current_bet = min(wager, bankroll)
        
        # play one hand of craps
        # dice_throws hold history of your throws
        hand, dice_throws = craps()
        outcome = hand[-1]
        cnt += 1

        # update bankroll
        if outcome == "wins":
            bankroll = bankroll + current_bet
        else:
            bankroll = bankroll - current_bet

        # (cnt,) is the game within game number, dice_throws the history of throws
        session_log.append(((cnt,), dice_throws,current_bet, outcome, bankroll))
        
    return session_log

# to be completed
def simulate(k, starting_bankroll, wager, target_bankroll):
    win_loss = {"Busted!":0, "Doubled!":0}
    for _ in range(k):
        pass


if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here

    """
    starting_bankroll = 50
    wager = 10
    target_bankroll = 100

    session = gamble(starting_bankroll,wager,target_bankroll)
    for entry in session:
            print(entry)

    betting_data = [(50,50,100),(50,10,100),(50,5,100),(50,1,100)]
    k = 5000
    for bet in betting_data:
         print(bet, simulate(k,*bet))