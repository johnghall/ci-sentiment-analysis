# import nltk
import sys
import getopt
import csv
import pandas
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


def parse_cli(argv):

    # Define default options
    options = {'replace': False, 'long': False, 'input_file': None,
               'output_file': None, 'column_name': None}

    # Parse submitted options
    try:
        opts, args = getopt.getopt(argv, "rli:o:c:")
    except getopt.GetoptError as e:
        print(e.msg)
        print("how to use")  # FIXME
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-r":
            options['replace'] = True
        elif opt == "-l":
            options['long'] = True
        elif opt == "-i":
            options['input_file'] = arg
        elif opt == "-o":
            options['output_file'] = arg
        elif opt == "-c":
            options['column_name'] = arg

    # Report issues to user
    error = False

    if not options['input_file']:
        print("User must specify input file (-i <file_name>)")
        error = True

    if not options['column_name']:
        print("User must specify column name (-c <column_name>)")
        error = True

    if error:
        sys.exit(2)

    return options


consent_column = "Consent to Participate in a Research Study"
consent_response = "I agree (i.e., I give my consent)"


def get_dataframe(options):
    # TODO add error checking before pandas scan here
    df = pandas.read_csv(options['input_file'])
    df = df.loc[df[consent_column] == consent_response]

    return df


def get_column(dataframe, column_name):
    column = dataframe[column_name]
    column = column.dropna()

    return column


def get_sentiment(response: str) -> bool:
    score = sia.polarity_scores(response)["compound"]
    if score <= -.2:
        return "Negative", score
    elif score < .2:
        return "Neutral", score
    else:
        return "Positive", score


def print_long(arr):
    for [value, score] in arr:
        print(value + " (Score: " + str(score) + ") \n")


def main(argv):
    options = parse_cli(argv)
    df = get_dataframe(options)
    input_column = get_column(df, options["column_name"])
    output_column = options["column_name"] if options["replace"] else options["column_name"] + \
        " (CATEGORIZED)"

    count = {"Negative": 0, "Neutral": 0, "Positive": 0}
    sorted_sentiments = {"Negative": [], "Neutral": [], "Positive": []}

    for index, value in input_column.items():
        analysis, score = get_sentiment(value)
        count[analysis] += 1
        sorted_sentiments[analysis].append([value, score])
        df[output_column[index]] = analysis

    total = sum(count.values())
    neg_per = '{:.2f}'.format(count["Negative"]/total*100)
    neut_per = '{:.2f}'.format(count["Neutral"]/total*100)
    pos_per = '{:.2f}'.format(count["Positive"]/total*100)
    print("Total: " + str(total))
    print("Negative: " + str(count["Negative"]) + " (" + neg_per + "%)")
    if options["long"]:
        print_long(sorted_sentiments["Negative"])
    print("Neutral: " + str(count["Neutral"]) + " (" + neut_per + "%)")
    if options["long"]:
        print_long(sorted_sentiments["Neutral"])
    print("Positive: " + str(count["Positive"]) + " (" + pos_per + "%)")
    if options["long"]:
        print_long(sorted_sentiments["Positive"])


if __name__ == "__main__":
    main(sys.argv[1:])
