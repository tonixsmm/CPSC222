import utils

def main():
    data = utils.data_loading("patient_data_to_clean.csv")
    print(data.isna().sum())
    data = utils.data_cleaning(data)
    data_agg = utils.data_aggregation(data)
    print(data_agg)
    utils.draw_histogram(data, "ReplLE")
    # utils.draw_scatter(data, "Stroke")
    # utils.check_instances(data)

main()