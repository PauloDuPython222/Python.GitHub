from random import randint
from time import sleep
b = 0
ip = str(input("Esolha \33[35m[ÍMPAR] \33[mou \33[35m[PAR]: ")).strip().upper()
while ip != "ÍMPAR" and ip != "PAR":
    ip = str(input("Esolha \33[35m[ÍMPAR] \33[mou \33[35m[PAR]: ")).strip().upper()

n = int(input("\33[mDigite um valor entre 1 e 10: "))
while n > 10 or n < 0:
    n = int(input("\33[mDigite um valor entre 1 e 10: "))




pc = randint(1, 10)

print("\33[34mCalculando os valores...")
sleep(0.5)
print(".")
sleep(0.5)
print("..")
sleep(0.5)
print("...")
sleep(1)

print(f"\33[mO computador escolheu \33[34m{pc} \33[me você escolheu \33[34m{n}. \33[mA soma é \33[34m{pc+n}")

if (pc+n) % 2 == 0:
    pc = "PAR"
else:
    pc = "ÍMPAR"

if ip == "ÍMPAR" and pc == "ÍMPAR":
    pc = "WIN"
    print("\33[32mPARABÉNS, VOCÊ GANHOU!")

elif ip == "PAR" and pc == "PAR":
    pc = "WIN"
    print("\33[32mPARABÉNS, VOCÊ GANHOU!")
else:
    pc = "LOSE"
    print("\33[31mSINTO MUITO, VOCê PERDEU.")

