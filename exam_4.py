def calculate_points(self):
    points = 0
    sayac = 0
    for i in self:
        if i == "snack":
            points += 1
        elif i == "beverage":
            points += 2
        sayac += 1
    if sayac > 5:
        points += 5
    return points
