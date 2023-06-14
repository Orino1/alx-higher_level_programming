#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    a = set(set_1)
    b = set(set_2)
    new_set = a ^ b
    return new_set




set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))