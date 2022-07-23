def divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i ==0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Ingrese numero: "))
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Please enter a number")
        
if __name__ == '__main__':
    run()