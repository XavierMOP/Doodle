# Penalty shoot

# 每一轮，你先输入一个方向射门，然后电脑随机判断一个方向扑救。方向不同则算进球得分，方向相同算扑救成功，不得分。
# 之后攻守轮换，你选择一个方向扑救，电脑随机方向射门。
# 第 5 轮结束之后，如果得分不同，比赛结束。
# 5 轮之内，如果一方即使踢进剩下所有球，也无法达到另一方当前得分，比赛结束。
# 5 论之后平分，比赛继续进行，直到某一轮分出胜负。

import datetime
import random
import colorama
import itertools

direction = ['left', 'middle', 'right']

player_point = 0
computer_point = 0

shoot_count = 0


def get_a_direction():
    return direction[random.randint(0, 2)]


def player_shoot(num_p):
    global player_point, computer_point, shoot_count
    print('******************** Round %d ********************' % num_p)

    # player_move = input('Choose a direction to shoot, left, middle or right: ')
    player_move = get_a_direction()
    computer_guess = get_a_direction()

    # while player_move not in direction:
    # player_move = input('Try again, left, middle or right: ')

    print('Player move was %s, computer guess was %s.' %
          (player_move, computer_guess))

    if player_move != computer_guess:
        player_point += 1

    shoot_count += 1
    print_points(shoot_count)


def computer_shoot(num_c):
    global player_point, computer_point, shoot_count
    print('******************** Round %d ********************' % num_c)

    computer_move = get_a_direction()
    # player_guess = input('Guess computer\'s direction, left, middle or right: ')
    player_guess = get_a_direction()

    # while player_guess not in direction:
    # player_guess = input('Try again, left, middle or right: ')

    print('Computer move was %s, player guess was %s.' %
          (computer_move, player_guess))

    if computer_move != player_guess:
        computer_point += 1

    shoot_count += 1
    print_points(shoot_count)


def print_points(rounds):
    print('After round %d, player\'s point is %d, computer\'s point is %d.\n' %
          (rounds, player_point, computer_point))


def win_lose():
    if player_point > computer_point:
        print(colorama.Fore.RED + 'Player wins!!!\n', colorama.Style.RESET_ALL)
        return
    elif player_point < computer_point:
        print(colorama.Fore.GREEN + 'Computer wins!!!\n',
              colorama.Style.RESET_ALL)
        return
    else:
        pass


def points_check_in_10_shoots():
    if (10 - shoot_count) % 2 == 1:
        max_point_left = round((10 - shoot_count) / 2) + 1
    else:
        max_point_left = (10 - shoot_count) / 2

    if ((player_point + max_point_left) < computer_point) or ((computer_point + max_point_left) < player_point):
        return True
    else:
        return False


def rounds_start():
    # when use a function to enclose

    #  if not points_check_in_10_shoots():
    #         pass
    #     else:
    #         return

    # cannot escape the main function properly.
    for ii in range(1, 11):
        if ii % 2 == 1:
            player_shoot(ii)
            if not points_check_in_10_shoots():
                pass
            else:
                win_lose()
                return
        if ii % 2 == 0:
            computer_shoot(ii)
            if not points_check_in_10_shoots():
                pass
            else:
                win_lose()
                return

    print('Sudden death!\n')

    for iii in itertools.count(11, 1):
        if iii % 2 == 1:
            player_shoot(iii)
            if (player_point - computer_point) ** 2 < 4:
                # if player_point == computer_point:
                # ==: sudden death
                # < 4: one parth has to win 2 points over the other
                pass
            else:
                win_lose()
                return
        if iii % 2 == 0:
            computer_shoot(iii)
            if (player_point - computer_point) ** 2 < 4:
                # if player_point == computer_point:
                pass
            else:
                win_lose()
                return


start_time = datetime.datetime.now()

rounds_start()

end_time = datetime.datetime.now()

runtime = str(end_time - start_time)
print(runtime[2:4] + ' min ' + runtime[5:] + ' sec')
