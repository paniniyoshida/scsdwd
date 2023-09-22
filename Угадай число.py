# -*- coding: cp1251 -*-
import random

def guess_number():
    number = random.randint(1, 100)
    tries = 0
    
    print("� ������� ����� �� 1 �� 100. �������� �������")
    
    while True:
        guess = int(input("������� �����: "))
        tries += 1
        
        if guess < number:
            print("������� ��������� �����")
        elif guess > number:
            print("������� ������� �����")
        else:
            print(f"�� ������ �����")
            break

guess_number()

