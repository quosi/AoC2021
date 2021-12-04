import pandas as pd

# Day 3 AoC part 1

def df_preProc(df):
    assert len(df['DATA'][1]) == len(df['DATA'][2]), 'Input data elements should have same length.'
    for i in range(len(df['DATA'][1])):
        df["bin"+str(i)] = 2
    for e in range(len(df)):
        for i in range(len(df['DATA'][1])):
            df["bin"+str(i)][e] = df['DATA'][e][i]
    return df

def get_mostCommonBite(df):
    result = []
    columns = df.columns
    cols = df[columns[1:]]
    for i in cols:
        x = df[i].value_counts()
        result.append(int(str(x.keys)[29:30]))
    return "".join(map(str, result))

def get_leastCommonBite(df):
    columns = df.columns
    cols = df[columns[1:]]
    result = []
    for i in cols:
        x = df[i].value_counts()
        result.append(int(str(x.keys)[38:39]))
    return "".join(map(str, result))

def get_powerConsumption(gamma_rate=0, epsilon_rate=0):
    '''Returns power consumption of submarine, 
    by multiplying the gamma and epsilon rate, 
    derived from diagnostic report.'''
    return gamma_rate * epsilon_rate

if __name__ == "__main__":
    df = pd.read_csv('data_diagnostics_day3.csv', dtype=str)
    bin_gamma = get_leastCommonBite(df_preProc(df))
    bin_epsilon = get_mostCommonBite(df_preProc(df))
    pC = get_powerConsumption(int(bin_gamma, 2), int(bin_epsilon, 2))
    print(f'---> Power consumption: {pC}')