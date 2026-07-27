
def stats(numbers): 
   """Return the min, max, and mean of a list of numbers."""
   highest_number = max(numbers)
   lowest_number = min(numbers)
   mean = sum(numbers) / len(numbers)
   return highest_number, lowest_number, mean

def summarise_scores(scores, passing_grade=40):
   """Returns the highest, lowest, and number passed from a list of scores"""
   highest_score = max(scores)
   lowest_score = min(scores)
   count = 0
   
   for n in scores:
      if n >= passing_grade:
         count += 1

   return highest_score, lowest_score, count

low, high, mean = stats([3, 1, 4, 1, 5, 9])
print(high)
print(low)
print(mean)

highest, lowest, number_passed = summarise_scores([72, 45, 18, 90, 39, 55])
print(highest)
print(lowest)
print(number_passed)


def add(item, items=None):
   if items is None:
      items = []
   items.append(item)
   return items
    
