import random

def spin_reels():
    symbols = ['🍒', '🔔', '🍋', '⭐', '💎']
    reels = [random.choice(symbols) for _ in range(3)]
    print("Результаты:", " | ".join(reels))
    return reels

def check_win(reels, bet):
    if len(set(reels)) == 1:
        win_amount = bet * 10
        print(f"Поздравляем! Вы выиграли {win_amount} монет!")
        return win_amount
    elif len(set(reels)) == 2:
        win_amount = bet * 2
        print(f"Неплохо! Вы выиграли {win_amount} монет!")
        return win_amount
    else:
        print("Попробуйте еще раз.")
        return 0



balance = 100

def main():
    global balance
    print("Добро пожаловать в наше казино!")
    print(f"Ваш начальный баланс: {balance} монет")
    while True:
        user_input = input("Нажмите Enter, чтобы играть (или 'q' для выхода): ")
        if user_input.lower() == 'q':
            break
        bet = int(input(f"Сколько хотите поставить? (Ваш баланс: {balance}): "))
        if bet > balance:
            print("Недостаточно средств!")
            continue
        balance -= bet
        reels = spin_reels()
        check_win(reels)


if __name__ == "__main__":
    main()
