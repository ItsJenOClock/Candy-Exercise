'''
1. 
In `get_friends_favorite_candy_count()`, return a dictionary of candy names 
and the amount of times each candy appears in the `friend_favorites` list.

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]
'''

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

def get_friends_favorite_candy_count(favorites):
    candy_dict = {}

    for candy_list in favorites:
        for candy in candy_list[1]:
            if candy not in candy_dict:
                candy_dict[candy] = 1
            else:
                candy_dict[candy] += 1

    return candy_dict

# print(get_friends_favorite_candy_count(friend_favorites))


'''
2. 
Given the list `friend_favorites`, create a new data structure in the 
function `create_new_candy_data_structure` that describes the different 
kinds of candy paired with a list of friends that like that candy. 

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]
'''
def create_new_candy_data_structure(data):
    candy_dict = {}

    for candy_list in data:
        friend = candy_list[0]
        for candy in candy_list[1]:
            if candy not in candy_dict:
                candy_dict[candy] = [friend]
            else:
                candy_dict[candy].append(friend)

    return candy_dict

# print(create_new_candy_data_structure(friend_favorites))

'''
3. 
In `get_friends_who_like_specified_candy()`, return a tuple of 
friends who like the candy specified in the candy_name parameter.
'''
def get_friends_who_like_specific_candy(data, candy_name):
    candy_dict = create_new_candy_data_structure(data)
    friends_list = []

    if candy_name in candy_dict:
        friends_list = candy_dict[candy_name]

    return tuple(friends_list)

# print(get_friends_who_like_specific_candy(friend_favorites, "sour patch kids"))

'''
4. 
In, `create_candy_set()`, return a set of all the candies from
the data structure made in `create_new_candy_data_structure()`.
'''
def create_candy_set(data):
    candy_set = set()

    for candy_list in data:
        for candy in candy_list[1]:
            candy_set.add(candy)

    return candy_set

# print(create_candy_set(friend_favorites))


'''
5. 
Starting with nominal cases, write tests for each of the functions 
in the file tests/test_candy_data_structure.py then write tests to 
handle edge cases.
'''