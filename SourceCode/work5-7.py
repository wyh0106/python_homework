
fn = 'resource\pi_million_digits.txt'

with open(fn) as pi_file:
    lines = pi_file.readlines()

pi_num = ''

for line in lines:
    pi_num += line.strip()

print(lines)