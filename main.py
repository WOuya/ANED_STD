import math

if __name__ == "__main__":
    entry = 0

    mu = 0
    sigma = 0
    q = 0
    n = 0
    
    entry = input("Enter the next real number:")
    while entry.isnumeric():
        x = float(entry)
        mu = (n * mu + x )/(n+1)
        q += x ** 2
        n += 1
        sigma = q / n - mu**2

        print(f"Mean:{mu}\nStandard_dev:{math.sqrt(sigma)}")
        entry = input("Enter the next real number:")
