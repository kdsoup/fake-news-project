import pandas as pd

# helper function to extract sample of large dataset
def extract_sample(filename: str, dst: str, start_row: int, end_row: int) -> None:
    df = pd.read_csv(filename)

    data = df.iloc[start_row:end_row]

    data.to_csv(dst)

input = input("Enter '[filename] [distination] [start_row] [end_row]': ")
inp_lst = list(input.split(" "))

extract_sample(inp_lst[0], int(inp_lst[1]), int(inp_lst[2]))