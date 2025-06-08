Here’s a comprehensive overview of **all common approaches** to generate or get the `n`th **Fibonacci number** in Python, covering:

---

### ✅ What is Fibonacci?

The Fibonacci sequence is:

```
0, 1, 1, 2, 3, 5, 8, 13, ...
```

Formula:
**F(n) = F(n-1) + F(n-2)**
With base cases: **F(0) = 0, F(1) = 1**

---

## 🔹 1. **Recursive Approach (Naive, Exponential Time)**

```python
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# Example
print(fib_recursive(7))  # Output: 13
```

⛔️ **Time complexity:** O(2ⁿ)
⛔️ **Not recommended** for large `n`

---

## 🔹 2. **Memoization (Top-Down DP)**

```python
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# Example
print(fib_memo(50))  # Output: 12586269025
```

✅ **Time complexity:** O(n)
✅ Much faster than naive recursion

---

## 🔹 3. **Tabulation (Bottom-Up DP)**

```python
def fib_tabulation(n):
    if n <= 1:
        return n
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[-1] + dp[-2])
    return dp[n]

# Example
print(fib_tabulation(10))  # Output: 55
```

✅ **Time complexity:** O(n)
✅ **Space complexity:** O(n)

---

## 🔹 4. **Space Optimized Iterative**

```python
def fib_space_optimized(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Example
print(fib_space_optimized(10))  # Output: 55
```

✅ **Time:** O(n)
✅ **Space:** O(1)

---

## 🔹 5. **Matrix Exponentiation (O(log n))**

```python
def fib_matrix(n):
    def multiply(F, M):
        x = F[0][0]*M[0][0] + F[0][1]*M[1][0]
        y = F[0][0]*M[0][1] + F[0][1]*M[1][1]
        z = F[1][0]*M[0][0] + F[1][1]*M[1][0]
        w = F[1][0]*M[0][1] + F[1][1]*M[1][1]
        F[0][0], F[0][1] = x, y
        F[1][0], F[1][1] = z, w

    def power(F, n):
        if n == 0 or n == 1:
            return
        M = [[1, 1], [1, 0]]
        power(F, n // 2)
        multiply(F, F)
        if n % 2 != 0:
            multiply(F, M)

    F = [[1, 1], [1, 0]]
    if n == 0:
        return 0
    power(F, n - 1)
    return F[0][0]

# Example
print(fib_matrix(50))  # Output: 12586269025
```

✅ **Time complexity:** O(log n)

---

## 🔹 6. **Using Binet's Formula (Mathematical Formula)**

```python
import math

def fib_binet(n):
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    return round((phi ** n) / sqrt5)

# Example
print(fib_binet(10))  # Output: 55
```

⚠️ Good for small `n`, but may suffer from floating point inaccuracies for large `n`.

---

## 🔹 7. **Print All Fibonacci Numbers up to `n` Terms**

```python
def print_fib_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Example
print_fib_series(10)  # Output: 0 1 1 2 3 5 8 13 21 34
```

---

## ✅ Summary Table:

| Approach               | Time     | Space | Notes                           |
| ---------------------- | -------- | ----- | ------------------------------- |
| Recursive              | O(2ⁿ)    | O(n)  | Very slow, avoid                |
| Memoization (Top-Down) | O(n)     | O(n)  | Fast and easy                   |
| Tabulation (Bottom-Up) | O(n)     | O(n)  | Clean and iterative             |
| Space Optimized DP     | O(n)     | O(1)  | Best for most use cases         |
| Matrix Exponentiation  | O(log n) | O(1)  | Best for large `n`              |
| Binet’s Formula        | O(1)     | O(1)  | Fast, less accurate for large n |
| Print All              | O(n)     | O(1)  | For generating full series      |

---


