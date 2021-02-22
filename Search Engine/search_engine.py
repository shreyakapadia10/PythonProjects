"""The task you have to perform is “Search Engine”.
This task consists of a total of 20 points to evaluate your performance.

Problem Statement:-
You are given few sentences as a list (Python list of sentences).
Take a query string as an input from the user.
You have to pull out the sentences matching this query inputted by the user
in decreasing order of relevance after converting every word in the query and the sentence to lowercase.
Most relevant sentence is the one with the maximum number of matching words with the query.
Sentences = [“Python is cool”, “python is good”, “python is not python snake”]

Input:
Please input your query string
“Python is”

Output:
3 results found:

python is not python snake
python is good
Python is cool """

from time import time

# Creating List of sentences
sentences = ["Python is cool", "python is good", "python is not python snake"]


def search_query():
    # Creating an empty list to store results
    search_result = []

    # Iterating over list
    for sentence in sentences:
        # Checking if the sentence contains query
        if query in sentence.lower():
            # If so, counting occurrences of query word in the sentence
            cnt = sentence.lower().count(query)
            # Appending to search_result
            search_result.append([sentence, cnt])

    # Sorting search_result according to maximum counts of words
    search_result.sort(key=lambda count: count[1], reverse=True)

    # Getting current time of result
    result_time = time()

    # Printing result
    if len(search_result) > 0:
        # Printing how many results found and in how much time
        print(f"{len(search_result)} results found({result_time-query_time} seconds):")

        # Printing result sentences
        for result in search_result:
            print(result[0])
    else:
        print("No result found")


if __name__ == '__main__':
    # Getting user query
    query = input("Please input your query string: ")

    # Getting current time of query
    query_time = time()

    # Converting user input to lower case
    query = query.lower()

    search_query()