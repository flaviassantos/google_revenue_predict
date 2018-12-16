
# Import the necessary modules and libraries

from DataPreparation import load_flatten_df


if __name__ == '__main__':
	PATH = r"C:\Users\ssant\GoogleDrive\github\google_revenue_predict\data"
    # load data
    train = load_flatten_df(PATH+r'\raw\train.csv')
    test = load_flatten_df(PATH+r'\raw\test.csv')
    # output data
    train.to_csv(PATH+r"/processed/train_flattened.csv", index=False)
    train.to_csv(PATH+r"/processed/test_flattened.csv", index=False)


    #logger = get_google_logger()
    #logger.log("google.data_flattened", "true")
