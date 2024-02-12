from helper import *

def main():
    # input information here
    item = 'motherboard'

    url = build_url(item)

    df = get_data(url)

    sorted = sort_df(df)

    print(sorted)

main()
