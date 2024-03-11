# main.py
def generate_sequence(n):
    result = []
    count = 1
    num = 1

    while len(result) < n:
        for _ in range(num):
            if len(result) < n:
                result.append(num)
            else:
                break
        count += 1
        num = count

    return result


if __name__ == "__main__":
    try:
        n = int(input("Введите количество элементов последовательности: "))
        sequence = generate_sequence(n)
        print(sequence)
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")
    except KeyboardInterrupt:
        print("\nВыход из программы.")
