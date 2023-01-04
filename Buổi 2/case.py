#Option 1:
# def likes(names):
#     if len(names) == 0:
#         return "no one likes this"
#     elif len(names) == 1:
#         return names[0] + " likes this"
#     elif len(names)==2:
#         return " and " .join(names)+ " like this"
#     elif len(names) ==3:
#         return ", ".join(names[0:2])+ " and "+str(names[len(names)-1]) + " like this"
#     else:
#         return ", ".join(names[0:2]) + f" and {str(len(names)-2)} others like this"

# print(likes([]))                  # must be "no one likes this"
# print(likes(["Peter"]))            # must be "Peter likes this"
# print(likes(["Jacob", "Alex"]))    # must be "Jacob and Alex like this"
# print(likes(["Max", "John", "Mark"]))          # must be "Max, John and Mark like this"
# print(likes(["Alex", "Jacob", "Mark", "Max"])) # must be "Alex, Jacob and 2 others like this"
#Tối ưu nhất
def likes(names):
    formats = {
            0: "no one likes this",
            1: "{} likes this",
            2: "{} and {} like this",
            3: "{}, {} and {} like this",
            4: "{}, {} and {others} others like this"
        }
    n = len(names)
    return formats[min(n,4)].format(*names, others=n-2)