from matplotlib import pyplot as plt

movies = ["spider man ", "Cats", "Iron man", "Before sunset"]
num_oscars = [5, 11, 8, 10]

xs = [i + 0.1 for i , _ in enumerate(movies)]   # adjusting bar width  (enumerate: listing all of components in dictionary _ means string input)
plt.bar(xs, num_oscars)
plt.xlabel("Movie title")
plt.ylabel("Academy Awards")
plt.title("My favorite movies")
plt.xticks([i+0.5 for i, _ in enumerate(movies)], movies)    # label x-axis with movie names at bar centers

plt.show()







