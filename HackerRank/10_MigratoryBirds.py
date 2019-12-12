'''
You have been asked to help study the population of birds migrating across
the continent. Each type of bird you are interested in will be identified by
an integer value. Each time a particular kind of bird is spotted, its id number
will be added to your array of sightings. You would like to be able to find out
which type of bird is most common given a list of sightings. Your task is to
print the type number of that bird and if two or more types of birds are
equally common, choose the type with the smallest ID number.

For example, assume your bird sightings are of types arr = [1, 1, 2, 2, 3].
There are two each of types 1 and 2, and one sighting of type 3. Pick the lower
of the two types seen twice: type 1.

Input Format
The first line contains an integer denoting n, the number of birds sighted and
reported in the array arr.
The second line describes arr as n space-separated integers representing the
type numbers of each bird sighted.

Output Format
Print the type number of the most common bird; if two or more types of birds
are equally common, choose the type with the smallest ID number.

Sample Input 0
6
1 4 4 4 5 3

Sample Output 0
4

Sample Input 1
11
1 2 3 4 5 4 3 2 1 3 4

Sample Output 1
3
'''


# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    max_seq = 0
    sorted_arr = sorted(arr)
    max_count_type = sorted_arr[0]
    temp_seq = 0
    for i in range(1, len(sorted_arr)):
        if sorted_arr[i - 1] == sorted_arr[i]:
            temp_seq += 1
        else:
            if max_seq < temp_seq:
                max_seq = temp_seq
                temp_seq = 0
                max_count_type = sorted_arr[i - 1]
    return max_count_type


def migratoryBirds2(arr):
    max_count_type = arr[0]
    max_type = max(arr)
    temp_max = [0] * (max_type + 1)
    cur_max = 0
    for bird in arr:
        temp_max[bird] += 1
    # print(temp_max)
    for i in range(1, len(temp_max)):
        if cur_max < temp_max[i]:
            cur_max = temp_max[i]
            max_count_type = i
    return max_count_type


def migratoryBirds3(arr):
    birds = {}
    for bird in arr:
        if bird not in birds:
            birds[bird] = 1
        else:
            birds[bird] += 1
    cur_type = max(arr)
    cur_max = 0
    for v in birds.values():
        if cur_max < v:
            cur_max = v
    for k, v in birds.items():
        if v == cur_max and cur_type > k:
            cur_type = k
    return cur_type

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # arr_count = int(input().strip())
    # arr = list(map(int, input().rstrip().split()))

    arr = [1, 1, 2, 2, 3]
    result = migratoryBirds(arr)
    print(result)  # 1

    arr = [1, 4, 4, 4, 5, 3]
    result = migratoryBirds(arr)
    print(result)  # 4

    arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
    result = migratoryBirds(arr)
    print(result)  # 3

    # fptr.write(str(result) + '\n')
    # fptr.close()
