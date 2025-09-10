"""Programming Assignment 5
This program includes 5 functions that use dictionaries and recursion to analyze hashtag trends on social media.
Tasks include counting hashtags, identifying their popularity, and merging hashtag lists using recursion."""
# Task 1 : It count how many times each hashtag appears in a week's dictionary
def count_hashtags(data=None):
    if not data:
        return {}
    result = {} #create empty dictionary
    for day in data: #loop through each day in the dictionary
        for tag in data[day]:
            if tag in result:
                result[tag] += 1
            else:
                result[tag] = 1
    return result #return the final hashtag counts

# Task 2 : track the count and days on which each hashtag appears
def days_of_hashtags(data=None):
    if not data:
        return {}
    counts = count_hashtags(data)
    result = {}
    for day, tags in data.items():
        for tag in tags:
            if tag not in result: #if Hashtag is not in result, add it with count and day
                result[tag] = [counts[tag], day]
            elif day not in result[tag]:
                result[tag].append(day)
    return result

# Task 3 : Identify the most frequently used hashtags of the week
def most_popular_hashtags(data=None):
    if not data:
        return {}
    tag_info = days_of_hashtags(data)
    if not tag_info:
        return {}

    max_count=max([info[0] for info in tag_info.values()])
    result = {}
    for tag, info in tag_info.items():
        if info[0] == max_count:
            for day in info[1:]:
                if day not in result: #add the day if is not in result yet
                    result[day] = [tag]
                else:
                    result[day].append(tag)
    return result

# Task 4 (Recursive) : Recursively it counts how many times a specific hashtag appears in a list
def hashtag_counter(lst=None, word=None):
    if not lst or not word:
        return 0
    if lst[0] == word: 
        return 1 + hashtag_counter(lst[1:], word)
    else:
        return hashtag_counter(lst[1:], word)

# Task 5 (Recursive) : Recursively it merges 2 hashtag list by alternating elements into one string
def merge_hashtags(list1, list2):
    if not list1 and not list2: # both lists empty in that case I used it
        return ''
    return list1[0] + ' ' + list2[0] + (
        ' ' + merge_hashtags(list1[1:], list2[1:]) if list1[1:] else ''
    )

#Example test cases
#testing problem 1
"""d_1 = {"Monday": ["#reading", "#hiking", "#reading", "#cycling"],
 "Tuesday": ["#gaming", "#gaming", "#painting", "#gaming"],
 "Friday": ["#dancing", "#painting", "#dancing", "#painting"],
 "Sunday": []}
d_2 = {"Saturday": ["#cooking", "#cooking", "#painting", "#painting"],
 "Sunday": ["#photography", "#gaming", "#photography",
 "#gaming", "#gaming"]}

print(count_hashtags(d_1))"""
 #testing problem 2
"""d_1 = {"Monday": ["#reading", "#hiking", "#reading", "#cycling"],
 "Tuesday": ["#gaming", "#gaming", "#painting", "#gaming"],
 "Friday": ["#dancing", "#painting", "#dancing", "#painting"],
 "Sunday": []}
d_2 = {"Saturday": ["#cooking", "#cooking", "#painting", "#painting"],
 "Sunday": ["#photography", "#gaming", "#photography",
 "#gaming", "#gaming"]} 
print(days_of_hashtags(d_1))
print(days_of_hashtags(d_2))"""
#testing problem 3
"""d_1 = {"Monday": ["#reading", "#hiking", "#reading", "#cycling"],
 "Tuesday": ["#gaming", "#gaming", "#painting", "#gaming"],
 "Friday": ["#dancing", "#painting", "#dancing", "#painting"],
 "Sunday": []}
d_2 = {"Saturday": ["#cooking", "#cooking", "#painting", "#painting"],
 "Sunday": ["#photography", "#gaming", "#photography",
 "#gaming", "#gaming"]} 
most_popular_hashtags(d_1)
most_popular_hashtags(d_2)"""
#testing problem 4
"""print(hashtag_counter(["#fun", "#fun", "#coding", "#fun", "#coding"], "#fun"))"""

#testing problem 5
"""print(merge_hashtags(["#love", "#fun", "#coding"], ["#python", "#life", "#learning"]))"""