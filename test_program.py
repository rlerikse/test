def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    fib_seq = []
    a, b = 0, 1
    while len(fib_seq) < n:
        fib_seq.append(a)
        a, b = b, a + b
    return fib_seq

def main():
    print("Fibonacci Sequence Generator")
    terms = 10
    result = fibonacci(terms)
    print(f"First {terms} terms of Fibonacci sequence:")
    print(result)

if __name__ == "__main__":
    main()