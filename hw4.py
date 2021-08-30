# def sequence_sum(first_sequence, second_sequence):
#     sum = 0
#     for i in second_sequence:
#         sum += first_sequence[i]
#     return sum
#
# print(sequence_sum([1.5, 2.5], [1, 1, 1]))


# def most_divisor_rich(A, B):
#     divs = 0
#     num = 0
#     for i in range(A + 1, B):
#         divisors = 0
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 divisors += 1
#                 if divisors > divs:
#                     divs = divisors
#                     num = i
# 
#     return num
# 
# 
# print(most_divisor_rich(1000, 2000))

# def get_primes(n):
#     primes = [2]
#     for i in range(3, n-2):
#         limit = int(i ** 0.5)
#         is_prime = True
#         for j in primes:
#             if j > limit:
#                 break
#             if not i % j:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(i)
#     return primes
#
#
# def get_prime(n):
#     primes = get_primes(n)
#     for prime in primes:
#         if (n - prime) in primes:
#             return prime, n - prime


# print(get_prime(14))



# def tree(num):
#      for i in range(1, num+1):
#          print(" "* (num-i)+"* "*i)
#
#
#
# tree(9)


# def int_reverse(num):
#     result = ""
#     while num != 0:
#         result += str(num % 10)
#         num //= 10
#     return int(result)
#
# def polindrome_numbers(a, b):
#     for i in range(a, b + 1):
#         if i == int_reverse(i):
#             print(i)
#
# polindrome_numbers(13000, 13500)


# def suffix_sums(first_sequence):
#     result_sequence = first_sequence.copy()
#     result = 0.0
#     for i in range(0, len(first_sequence)):
#         result_sequence[i] = float(sum(first_sequence[i:]))
#     return result_sequence
#
#
# print(suffix_sums([1.5, 2.5, 3]))


# def cyclic_shift(N, k):
#     result = ''
#     result_str = ''
#     for i in range(N):
#         result += input('input sequence numbers')
#     for j in range(k):
#         a = str(int(result) % 10)
#         result = str(int(result) // 10)
#         result = a + result
#     return result
#
# print(cyclic_shift(5, 2))
