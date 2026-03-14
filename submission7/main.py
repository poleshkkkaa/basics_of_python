import logging

logging.basicConfig(
    filename="log.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(message)s",
    encoding="utf-8")

try:
    value = input("Введіть ціле число: ")

    number = int(value)
    print(number) 

except ValueError:

    print("Помилка: введено некоректне значення. Потрібно вводити ціле число.")

    logging.error("Некоректний ввід: %s", value)


finally:
    print("Програма завершила виконання.")
  
