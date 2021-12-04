import pandas as pd

# Day 1 AoC part 1

def get_depth(df):
    depth_increase = []
    for i in range(0, len(df)-1):
        if (df['depth'][i+1] > df['depth'][i]):
            depth_increase.append(df['depth'][i+1])

    return len(depth_increase)

if __name__ == "__main__":
    df = pd.read_csv('data_sea_floor_day1.csv', delimiter=" ")
    print(f'---> Depth: {get_depth(df)}')