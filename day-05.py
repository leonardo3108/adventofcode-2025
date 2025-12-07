'''
--- Day 5: Cafeteria ---
As the forklifts break through the wall, the Elves are delighted to discover that there was a cafeteria on the other side after all.

You can hear a commotion coming from the kitchen. "At this rate, we won't have any time left to put the wreaths up in the dining hall!" Resolute in your quest, you investigate.

"If only we hadn't switched to the new inventory management system right before Christmas!" another Elf exclaims. You ask what's going on.

The Elves in the kitchen explain the situation: because of their complicated new inventory management system, they can't figure out which of their ingredients are fresh and which are spoiled. When you ask how it works, they give you a copy of their database (your puzzle input).

The database operates on ingredient IDs. It consists of a list of fresh ingredient ID ranges, a blank line, and a list of available ingredient IDs. For example:

3-5
10-14
16-20
12-18

1
5
8
11
17
32
The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all fresh. The ranges can also overlap; an ingredient ID is fresh if it is in any range.

The Elves are trying to determine which of the available ingredient IDs are fresh. In this example, this is done as follows:

Ingredient ID 1 is spoiled because it does not fall into any range.
Ingredient ID 5 is fresh because it falls into range 3-5.
Ingredient ID 8 is spoiled.
Ingredient ID 11 is fresh because it falls into range 10-14.
Ingredient ID 17 is fresh because it falls into range 16-20 as well as range 12-18.
Ingredient ID 32 is spoiled.
So, in this example, 3 of the available ingredient IDs are fresh.

Process the database file from the new inventory management system. How many of the available ingredient IDs are fresh?

Solution:
 - Parse the input into two sections: fresh ranges and available IDs.
 - For each available ID, check if it falls within any of the fresh ranges.
 - Count and return the number of fresh IDs.

Optional Optimization:
 - Merge overlapping fresh ranges to reduce the number of checks needed for each available ID.

--- Part Two ---
The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.

So that they can stop bugging you when they get new inventory, the Elves would like to know all of the IDs that the fresh ingredient ID ranges consider to be fresh. An ingredient ID is still considered fresh if it is in any range.

Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:

3-5
10-14
16-20
12-18
The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20. So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.

Process the database file again. How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?

Solution:
 - Merge overlapping fresh ranges.
 - For each merged range, calculate the total number of IDs it covers.
 - Sum these counts to get the total number of fresh IDs.
'''

input = '''
3-5
10-14
16-20
12-18

1
5
8
11
17
32
'''

input = open('input-05.txt').read()

# Preparation: Parse input into fresh ranges and available IDs
input_lines = input.strip().split('\n')
separator_index = input_lines.index('')
fresh_ranges = [tuple(map(int, line.split('-'))) for line in input_lines[:separator_index]]
# print(fresh_ranges)
available_ids = [int(line) for line in input_lines[separator_index + 1:]]
# print(available_ids)

# Optional Optimization: Merge overlapping fresh ranges
changed = True
while changed:
    new_fresh_ranges = []
    changed = False
    for start, end in fresh_ranges:
        # print(f"Fresh range: {start} to {end}")
        startf, endf = start, end
        for start2, end2 in fresh_ranges:
            if (start2, end2) != (start, end):
                if start2 <= end and end2 >= start:
                    # print(f"  Overlaps with: {start2} to {end2}")
                    startf = min(startf, start2)
                    endf = max(endf, end2)
                    # print(f"  Merged range: {startf} to {endf}")
        if (startf, endf) != (start, end):
            changed = True
        if (startf, endf) not in new_fresh_ranges:
            new_fresh_ranges.append((startf, endf))

    # print(f"Merged fresh ranges: {new_fresh_ranges}")
    fresh_ranges = new_fresh_ranges

# print(f"Merged fresh ranges: {new_fresh_ranges}")
fresh_count = 0

# Final check of available IDs
for available_id in available_ids:
    is_fresh = any(start <= available_id <= end for start, end in fresh_ranges)
    # print(f"ID {available_id} is {'fresh' if is_fresh else 'spoiled'}")
    if is_fresh:
        fresh_count += 1

print(f"Part One - Total fresh ingredient IDs: {fresh_count}")

# Part Two: Count total fresh IDs from merged ranges
total_fresh_ids = sum(end - start + 1 for start, end in fresh_ranges)
print(f"Part Two - Total ingredient IDs considered fresh by ranges: {total_fresh_ids}")

