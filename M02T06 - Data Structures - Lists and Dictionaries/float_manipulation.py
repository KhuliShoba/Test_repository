import statistics

# Initialize an emplty list to store the numbers 
float_lists = []
# Loop the current value within the range
for i in range(10):
    value = float(input(f"Enter float {i+1:} "))
    float_lists.append(value)

total_sum = sum(float_lists)
print(f" Sum: {total_sum}")
maximum = max(float_lists)
print(f" Maximun: {maximum}")
minimum = min(float_lists)
print(f" Minimum: {minimum}" )
ave_mean = statistics.mean(float_lists)
rounded_mean = round(ave_mean,2)
print(f" Mean: {rounded_mean}")
median = statistics.median(float_lists)
print(f" Median: {median}")