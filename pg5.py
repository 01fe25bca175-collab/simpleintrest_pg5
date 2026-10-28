import sys
principal = float(sys.argv[1])
rate = float(sys.argv[2])
time = float(sys.argv[3])

simple_interest = (principal * rate * time) / 100
print(f"The Simple Interest is: {simple_interest}")