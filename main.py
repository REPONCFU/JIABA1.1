import random

def spin_reels():
    symbols = ['🍒', '🔔', '🍋', '⭐', '💎']
    reels = [random.choice(symbols) for _ in range(3)]
    return reels

def main():
    print("Добро пожаловать в наше казино!")
    # Основной цикл игры
    while True:
        user_input = input("Нажмите Enter, чтобы играть (или 'q' для выхода): ")
        if user_input.lower() == 'q':
            break
        # Вращение барабанов (пока не реализовано)
        spin_reels()

if __name__ == "__main__":
    main()
