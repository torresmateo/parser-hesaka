import pandas as pd
import re
from parser import parse_file_municipalidad


def run(in_file, out_file, fmt):
    data = parse_file_municipalidad(in_file)
    df = pd.DataFrame(data)
    del data
    if fmt == "excel":
        df.to_excel(out_file, index=False)
    elif fmt == "csv":
        df.to_csv(out_file, index=False)
    else:
        df.to_csv(out_file, index=False, sep="\t")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Parser de Hesaka"
    )
    parser.add_argument("--input",
                        help="archivo a parsear",
                        required=True)
    parser.add_argument("--output",
                        help="archivo a escribir",
                        required=True)
    parser.add_argument("--fmt",
                        help="formato",
                        default="tsv",
                        required=False,
                        choices=["tsv", "csv", "excel"])
    args = parser.parse_args()
    run(args.input, args.output, args.fmt)


