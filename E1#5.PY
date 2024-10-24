my_list = []
my_list.append("Apple")
my_list.append("Banana")
my_list.append("Cherry")

print("Initial List:", my_list)

my_list.remove("Banana")

print("List after removing 'Banana':", my_list)

my_list.remove("Date")

print("List after removing 'Date':", my_list)

while "Fig" in my_list:
    my_list.remove("Fig")
