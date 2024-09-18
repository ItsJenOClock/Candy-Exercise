import pytest
from candy_problem.candy_problem import * 

# test for #1
def test_create_candy_data_structure_type():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert type(new_candy_data) == dict

# test for #2
# Add your own assertions to the test below
def test_create_candy_data_structure_values():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    friend_licorice = new_candy_data["licorice"]
    # Assert
    assert len(new_candy_data) == 8
    assert friend_licorice == ["Bob"]

    '''
    Add your assertions here!
    '''

'''
5. 
Starting with nominal cases, write tests for each of the functions 
in the file tests/test_candy_data_structure.py then write tests to 
handle edge cases.
'''

# test for #3
def test_create_friends_specific_candy_data_structure_type():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = get_friends_who_like_specific_candy(friend_favorites, "")
    
    # Assert
    assert type(new_candy_data) == tuple

# test for #3
def test_list_friends_specific_candy_values():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data_sour = get_friends_who_like_specific_candy(friend_favorites, "sour patch kids")
    new_candy_data_lolli = get_friends_who_like_specific_candy(friend_favorites, "lollipop")

    # Assert
    assert len(new_candy_data_sour) == 1
    assert len(new_candy_data_lolli) == 2

# test for #3 - edge
def test_list_friends_specific_candy_invalid_input():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]
    friend_favorites_empty = []
    # Act
    new_candy_data_invalid_candy = get_friends_who_like_specific_candy(friend_favorites, "twizzlers")
    new_candy_data_empty_list = get_friends_who_like_specific_candy(friend_favorites_empty, "lollipop")

    # Assert
    assert len(new_candy_data_invalid_candy) == 0
    assert len(new_candy_data_empty_list) == 0

# test for #4
def test_create_candy_set_data_structure_type():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_candy_set(friend_favorites)
    
    # Assert
    assert type(new_candy_data) == set

# test for #4
def test_create_candy_set_values():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_candy_set(friend_favorites)
    
    # Assert
    assert len(new_candy_data) == 8

# test for #4 - edge
def test_create_candy_set_empty_input():
    # Arrange
    friend_favorites = []
    # Act
    new_candy_data = create_candy_set(friend_favorites)
    
    # Assert
    assert new_candy_data == set()