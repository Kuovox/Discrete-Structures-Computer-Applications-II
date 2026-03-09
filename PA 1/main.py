import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

def closest_pair(points):
  points.sort(key=lambda point: point.x)
  return closest_pair_util(points)

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def brute_force_closest_pair(points):
    n = len(points)
    min_distance = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            dist = distance(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                closest_pair = (points[i], points[j])
    return closest_pair, min_distance

def strip_closest(strip, d):
    min_distance = d
    closest_pair = None
    n = len(strip)
    for i in range(n):
        for j in range(i+1, min(i+8, n)):
            if distance(strip[i], strip[j]) < min_distance:
                min_distance = distance(strip[i], strip[j])
                closest_pair = (strip[i], strip[j])
    return closest_pair, min_distance

def closest_pair_util(points):
    n = len(points)
    if n <= 3:
        return brute_force_closest_pair(points)
    mid = n // 2
    mid_point = points[mid]
    left_pair, left_distance = closest_pair_util(points[:mid])
    right_pair, right_distance = closest_pair_util(points[mid:])
    min_distance = min(left_distance, right_distance)
    if min_distance == left_distance:
      closest_pair = left_pair
    else:
      closest_pair = right_pair
      
    strip = [point for point in points if abs(point.x - mid_point.x) < min_distance]
    strip.sort(key=lambda point: point.y)
    strip_pair, strip_distance = strip_closest(strip, min_distance)
    if strip_distance < min_distance:
        return strip_pair, strip_distance
    return closest_pair, min_distance

def read_coordinates_from_file(file_path):
    points = []
    with open(file_path, 'r') as file:
        line = file.readline().strip()  # Read the entire line from the file and remove leading/trailing whitespace
        line = line.strip('{}')  # Remove outer curly braces
        pairs = line.split('}, {')  # Split the line into pairs of coordinates
        for pair in pairs:
            x, y = map(float, pair.strip('{}').split(','))
            points.append(Point(x, y))
    return points

def main():
  file_path = '10.txt'
  points = read_coordinates_from_file(file_path)
  closest, min_distance = closest_pair(points)
  print("Closest pair:", closest_pair)
  print("Distance:", min_distance)

main()