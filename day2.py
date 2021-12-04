import pandas as pd

# Day 2 AoC part 1

def get_position(df):
    x_position = 0
    y_position = 0
    aim = 0
    for i in range(len(df)):
        if df['direction'][i] == "forward":
            x_position += int(df['distance'][i])
            y_position += (aim * int(df['distance'][i]))
        if df['direction'][i] == "down":
            aim += int(df['distance'][i])
        if df['direction'][i] == "up":
            aim -= int(df['distance'][i])
    return x_position*y_position

# Day 2 AoC part 2

if __name__ == "__main__":
    df = pd.read_csv('data_course_day2.csv', delimiter=" ")
    print(f'---> Position: {get_position(df)}')