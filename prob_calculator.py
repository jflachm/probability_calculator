import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for color, value in kwargs.items():
            self.contents += [color] * int(value)

  def draw(self, num_draws):
    num_balls = len(self.contents)
    if num_draws >= num_balls:
      return self.contents
    result = []
    for i in range(0, num_draws):
      bid = random.randint(0, num_balls - 1)
      result.append(self.contents.pop(bid))
      num_balls -= 1

    return result


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for exp in range(num_experiments):
    hat_exp = copy.deepcopy(hat)
    balls_drawn = hat_exp.draw(num_balls_drawn)
    balls_req = 0
    for color, value in expected_balls.items():
      if balls_drawn.count(color) >= value:  
        balls_req += 1
    if balls_req == len(expected_balls):
      count += 1  
    else:
      count += 0

  return count / num_experiments
