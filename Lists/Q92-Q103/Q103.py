# Q103. Make your own list. Print the smallest number present in that list

my_list = [51, 85, 1748, 44, 52, -100, -200]
smallest = my_list[0]

for i in my_list:
    if i < smallest:
        smallest = i
print(smallest)


"""
country    year   total_sales volume transaction id 
 Us        2024    25000
 Us        2025    24000
 uk        2025    26000

 o/p:
 country 2024_sales 2025_sales

 select country,case when year=2024 then sales as 2024_sales, when year=2025 then sales as 2025 sales and from data[table name]

"""
