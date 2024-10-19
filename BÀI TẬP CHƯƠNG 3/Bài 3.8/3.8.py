import numpy as np
heights = np.loadtxt('Bài 3.8\heights.txt') 
with open('Bài 3.8\position.txt', 'r') as f:
    positions = f.read().splitlines() 
positions_set = ['GK', 'M', 'A', 'D']
height_by_position = {pos: [] for pos in positions_set}
for i, pos in enumerate(positions):
    height_by_position[pos].append(heights[i])
average_heights = {pos: np.mean(height_by_position[pos]) for pos in height_by_position}
for pos, avg_height in average_heights.items():
    print(f"Chiều cao trung bình của vị trí {pos}: {avg_height:.2f}")