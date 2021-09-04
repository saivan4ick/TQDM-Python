# TQDM-Python

import random
from time import sleep
from tqdm import tqdm

print('Взлом серверов Mail.ru Group в процессе ...')
for i in tqdm(range(100), colour="green"):
	sleep(random.uniform(0.01, 0.1))

print('Mail.ru Group успешно взломана!!!')
