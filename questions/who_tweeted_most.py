# Assignment: Find who tweeted the most
#
# You will be given a list of tweets
# Your program should find the user who has tweeted the most
#
# Note:
# If multiple users are having same number of tweets, then print all the users in alphabetical order of user names.
#
# Input format:
# Read the input from console.
# First line of input should be number of test cases
# Remaining lines of input should contain each test case input.
#
# For each test case input:
# First line should contain number of tweets.
# Followed by N lines, each containing user name and tweet id separated by a space.
#
# Output format:
# Find the user with max number of tweets. Print user name and total number of tweets.
#
#
# Sample 1:
# Input
# 1
# 4
# sachin tweet_id_1
# sehwag tweet_id_2
# sachin tweet_id_3
# sachin tweet_id_4
#
# Output
# sachin 3
#
#
# Sample 2:
# Input
# 1
# 6
# sachin tweet_id_1
# sehwag tweet_id_2
# sachin tweet_id_3
# sehwag tweet_id_4
# kohli tweet_id_5
# kohli tweet_id_6
#
# Output
# kohli 2
# sachin 2
# sehwag 2
#
#
#
# Sample 3:
# Input
# 2
# 4
# sachin tweet_id_1
# sehwag tweet_id_2
# sachin tweet_id_3
# sehwag tweet_id_4
# 5
# dhoni tweet_id_10
# dhoni tweet_id_11
# kohli tweet_id_12
# dhoni tweet_id_13
# dhoni tweet_id_14
#
# Output
# sachin 2
# sehwag 2
# dhoni 4
#
#
#
# two inbuilt functions used -
#if key in dict ==> to check if a key is present in the dictionary
#sort function to sort the array alphabetically
#I have intentionally not used Counter module which also stores keys and their count in a dictionary
#instead I have manually implemented that

number_of_test_cases = int(input("enter number of test cases\n"))
#print(number_of_test_cases)

curr_test_case = 1
output_list = []
max_number_of_tweets = 0

while curr_test_case <= number_of_test_cases:
	number_of_input_for_curr_test_case = int(input("enter the number of input for the test case {}\n".format(curr_test_case)))
	#print(number_of_input_for_curr_test_case)

	#creating a dictionary
	# key represemts a user_name
	# value is a list containing all the tweets for that user and its current count
	tweet_dict = {}
	for i in range(number_of_input_for_curr_test_case):
		user_tweet = input("enter the name of the user followed by tweet ID separated by a space\n")
		user_name, tweet_id = user_tweet.split(' ')
		#print('user_name= {} tweet_id= {}'.format(user_name, tweet_id))

		if user_name in tweet_dict.keys():
			tweet_dict[user_name][0].append(tweet_id)
			tweet_dict[user_name][1] += 1
		else:
			tweet_dict[user_name] = [[tweet_id],1]

	#print(tweet_dict)
	output_list.append([])
	for user_name in tweet_dict:
		if(tweet_dict[user_name][1] == max_number_of_tweets):
			output_list[curr_test_case - 1].append(user_name)
		elif(tweet_dict[user_name][1] > max_number_of_tweets):
			output_list[curr_test_case - 1] = [user_name]
			max_number_of_tweets = tweet_dict[user_name][1]
		else:
			pass

	output_list[curr_test_case-1].sort()
	output_list[curr_test_case -1].append(max_number_of_tweets)
	#print(output_list[curr_test_case-1])
	#print(output_list)
	curr_test_case = curr_test_case + 1

for i in output_list:
	for j in range(len(i) -1):
		print("{} {}".format(i[j], i[-1]))
