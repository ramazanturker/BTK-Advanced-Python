listing = [1, 2, 3]

print(len(listing))

# number = 10
# print(len(number))

text = "hello, btk academy"
print(len(text))

class Movie:
    def __init__(self, title, director, year, duration):
        self.title = title
        self.director = director
        self.year = year
        self.duration = duration

    def __repr__(self):
        return f"{self.title}, published by {self.director} in {self.year}"
    
    def __len__(self):
        return self.duration
    
    def __del__(self):
        print("movie deleted")

movie1 = Movie("Ahlat Ağacı - The Wild Pear Tree", "Nuri Bilge Ceylan", 2018, 120)

print(movie1.__repr__())
print(len(movie1))

del movie1