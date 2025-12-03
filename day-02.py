'''
--- Day 2: Gift Shop ---
You get inside and take the elevator to its only other stop: the gift shop. "Thank you for visiting the North Pole!" gleefully exclaims a nearby sign. You aren't sure who is even allowed to visit the North Pole, but you know you can access the lobby through here, and from there you can access the rest of the North Pole base.

As you make your way through the surprisingly extensive selection, one of the clerks recognizes you and asks for your help.

As it turns out, one of the younger Elves was playing on a gift shop computer and managed to add a whole bunch of invalid product IDs to their gift shop database! Surely, it would be no trouble for you to identify the invalid product IDs for them, right?

They've even checked most of the product ID ranges already; they only have a few product ID ranges (your puzzle input) that you'll need to check. For example:

11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
(The ID ranges are wrapped here for legibility; in your input, they appear on a single long line.)

The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).

Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)

Your job is to find all of the invalid IDs that appear in the given ranges. In the above example:

11-22 has two invalid IDs, 11 and 22.
95-115 has one invalid ID, 99.
998-1012 has one invalid ID, 1010.
1188511880-1188511890 has one invalid ID, 1188511885.
222220-222224 has one invalid ID, 222222.
1698522-1698528 contains no invalid IDs.
446443-446449 has one invalid ID, 446446.
38593856-38593862 has one invalid ID, 38593859.
The rest of the ranges contain no invalid IDs.
Adding up all the invalid IDs in this example produces 1227775554.

What do you get if you add up all of the invalid IDs?

Solution:
 - Read the input ranges from the file.
 - For each range, check each number to see if it is made of a repeated sequence.
 - If it is, add it to the total sum.

--- Part Two ---
The clerk quickly discovers that there are still invalid IDs in the ranges in your list. Maybe the young Elf was doing other silly patterns as well?

Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.

From the same example as before:

11-22 still has two invalid IDs, 11 and 22.
95-115 now has two invalid IDs, 99 and 111.
998-1012 now has two invalid IDs, 999 and 1010.
1188511880-1188511890 still has one invalid ID, 1188511885.
222220-222224 still has one invalid ID, 222222.
1698522-1698528 still contains no invalid IDs.
446443-446449 still has one invalid ID, 446446.
38593856-38593862 still has one invalid ID, 38593859.
565653-565659 now has one invalid ID, 565656.
824824821-824824827 now has one invalid ID, 824824824.
2121212118-2121212124 now has one invalid ID, 2121212121.
Adding up all the invalid IDs in this example produces 4174379265.

What do you get if you add up all of the invalid IDs using these new rules?

Solution:
 - Modify the check_id function to check for any sequence repeated at least twice.
   - Check all possible substring lengths that divide the total length evenly, from half the length of the ID down to 1.
'''
part_one_sum = 0
part_two_sum = 0

input = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,' + \
        '1698522-1698528,446443-446449,38593856-38593862,565653-565659,' + \
        '824824821-824824827,2121212118-2121212124'

input = open('input-02.txt').read().strip()

def check_id(id: str, debug: bool = False) -> tuple[bool, bool]:
    length = len(id)
    if debug:
        print(f'Checking ID: {id} (length: {length})')
    for sub_len in range(length // 2, 0, -1):
        if debug:
            print(f'  Trying substring length: {sub_len}')
        if length % sub_len == 0:
            times = length // sub_len
            substring = id[:sub_len]
            if substring * times == id:
                return (times == 2, True)
    return (False, False)

for each_range in input.split(','):
    start, end = [int(x) for x in each_range.split('-')]
    for id in range(start, end + 1):
        is_invalid_half, is_invalid_any = check_id(str(id))
        if is_invalid_any:
            part_two_sum += id
            if is_invalid_half:
                part_one_sum += id
                # print(f'Invalid ID (half): {id}')
            else:
                # print(f'Invalid ID (any): {id}')
                pass

print(f'Part One - Sum of invalid IDs: {part_one_sum}')
print(f'Part Two - Sum of invalid IDs: {part_two_sum}')
