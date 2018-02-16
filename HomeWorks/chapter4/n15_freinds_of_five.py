from n14_friends import friendships

friends_of_five = [ i for i, is_friend in enumerate(friendships[5]) if is_friend]
print friends_of_five


