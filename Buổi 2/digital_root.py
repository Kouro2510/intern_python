# def digital_root(n):
#     # If n is 0.
#     if (n == "0"):
#         return 0
#
#     # Count sum of digits under mod 9
#     ans = 0
#     for i in range(0, len(n)):
#         ans = (ans + int(n[i])) % 9
#
#     # If digit sum is multiple of 9, answer
#     # 9, else remainder with 9.
#     if (ans == 0):
#         return 9
#     else:
#         return ans % 9
#
#
# # Driver method
# n = "16"
#
# # Calling digitalRoot function
# print(digital_root(n))
#
# # This code is contributed by Gitanjali.
