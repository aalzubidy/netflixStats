import csv

if __name__ == "__main__":
    print('started...')

    movies = []
    tvShows = []

    moviesCount = {}
    tvShowsCount = {}

    with open('netflix.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            item = row[0]
            if(':' in item):
                tvShows.append(item)
                if(item in tvShowsCount.keys()):
                    tvShowsCount[item] = tvShowsCount[item] + 1
                else:
                    tvShowsCount[item] = 1
            else:
                movies.append(item)
                if(item in moviesCount.keys()):
                    moviesCount[item] = moviesCount[item] + 1
                else:
                    moviesCount[item] = 1

    
    print('Movies: ', len(movies))
    print('TV Shows: ', len(tvShows))

    print(moviesCount)