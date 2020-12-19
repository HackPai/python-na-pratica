
import numpy as np

number = np.random.randint(1, 101) # загадываем число

count = 0

while True:
    count += 1
    predict_number = int(input("Угадай число от 1 до 100"))