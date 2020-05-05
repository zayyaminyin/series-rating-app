import csv
import html

series_filename = "series.csv"
ratings_filename = "ratings.csv"

def get_series():
  series = {}
  with open(series_filename) as fileData:
    reader = csv.reader(fileData)
    for row in reader:
      series_id = row[0]
      title = row[1]
      network = row[2]
      series[series_id] = {
        "series_id": series_id,
        "title": title,
        "network": network,
        "ratings": []
      }
  with open(ratings_filename) as fileData:
    reader = csv.reader(fileData)
    for row in reader:
      series_id = row[0]
      rating = int(row[1])
      if series_id in series:
        serie = series[series_id]
        serie["ratings"].append(rating)
  return series


def add_series(serie):
  series = get_series()
  if 'series_id' in serie and 'title' in serie and 'network' in serie:
    if len(serie['series_id']) == 8 and serie['series_id'] not in series and \
       serie['title'] != "" and serie['network'] != "":
      print(serie)
      with open(series_filename, "a") as csvFile:
        writer = csv.writer(csvFile)
        rowToWrite = [serie['series_id'], serie['title'], serie['network']]
        writer.writerow(rowToWrite)
  return None


def rate_series(series_rating):
  series = get_series()
  if 'series_id' in series_rating and 'rating' in series_rating:
    if series_rating['series_id'] in series and \
       series_rating['rating'] in [1, 2, 3, 4, 5]:
      with open(ratings_filename, "a") as csvFile:
        writer = csv.writer(csvFile)
        rowToWrite = [series_rating['series_id'], series_rating['rating']]
        writer.writerow(rowToWrite)
  return None