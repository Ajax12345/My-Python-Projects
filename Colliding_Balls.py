def main():
  ball1 = [5, 5, 2]
  ball2 = [2,8,3]
  colliding(ball1, ball2)

def colliding(ball, two_ball):
  radius1 = int(input("Enter the radius of your first sphere: "))
  radius2 = int(input("Enter the radius of your second sphere: "))
  xo1 = ball[0]
  xo2 = two_ball[0]
  yo1 = ball[1]
  yo2 = two_ball[1]
  zo1 = ball[2]
  zo2 = two_ball[2]

  distance_squared = pow((xo2-xo1), 2) + pow((yo2-yo1), 2) + pow((zo2-zo1), 2)
  distance = round(pow(distance_squared, 0.5), 4)
  sum_of_radii = radius1+radius2
  if distance < sum_of_radii:
    print("The balls are colliding")

  else:
    print("The balls are not colliding")


main()
