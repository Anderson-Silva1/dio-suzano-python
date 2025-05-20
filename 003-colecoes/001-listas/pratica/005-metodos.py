# append
append_list = []

append_list.append(1)
append_list.append("Python")
append_list.append([1, 2, 3])

print(append_list) # [1, "Python", [1, 2, 3]]

# clear
clear_list = append_list
clear_list.clear()
print(clear_list) # []

# count
count_list = ["azul", "amarelo", "vermelho", "azul"]
print(count_list.count("azul"))

# extend
extend_list = [1,2,3,4]
extend_list2 = [5,6,7,8]
extend_list.extend(extend_list2)
print(extend_list)