import numpy as citybois

names = ["Me", "Lia", "Jake"]
steps = citybois.array([
  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
])

for x in range(len(names)):
    total_steps = citybois.sum(steps[x])
    average_steps = citybois.mean(steps[x])
    min_steps = citybois.min(steps[x])
    max_steps = citybois.max(steps[x])
    print(
        f"{names[x]} - Total Steps: {total_steps} | "
        f"Average: {average_steps:.1f} | "
        f"Min: {min_steps} | Max: {max_steps}"
    )
