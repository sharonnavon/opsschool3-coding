#!/usr/bin/env python3

import sys
import os
import json
import operator


def load_json_into_dict(json_file):
    try:
        with open(json_file) as infile:
            ppl_dict = json.load(infile)
            return ppl_dict

    except (FileNotFoundError, IndexError):
        print('Usage: python3', os.path.basename(sys.argv[0]), '<path to JSON>')
        sys.exit()


def prepare_data_into_lists_and_strings(a_dict):
    buckets = sorted(a_dict['buckets'])
    ppl_ages = a_dict['ppl_ages']
    oldest_age = max(ppl_ages.values())
    json_basename = os.path.basename(sys.argv[1])
    output_file = (os.path.splitext(json_basename)[0])+'.yml'

    return buckets, ppl_ages, oldest_age, output_file


def write_buckets_and_ppl_into_outfile(start_bucket, end_bucket, ppl_ages, outfile, oper=operator.lt):
    """
    Organizes people into age buckets and write the data into outfile.
    :param start_bucket:
    :param end_bucket:
    :param ppl_ages:
    :param outfile:
    :param oper: last operator
    """
    outfile.write(f"{start_bucket}-{end_bucket}:\n")

    for person in ppl_ages:
        if start_bucket <= ppl_ages[person] and oper(ppl_ages[person], end_bucket):
            outfile.write(f"- :{person}\n")


def main():
    ppl_dict = load_json_into_dict(sys.argv[1])
    buckets, ppl_ages, oldest_age, output_file = prepare_data_into_lists_and_strings(ppl_dict)

    # Write the data into outfile in YAML style
    with open(output_file, 'w') as outfile:
        outfile.write(f"---\n")
        write_buckets_and_ppl_into_outfile(buckets[0], buckets[1], ppl_ages, outfile)
        write_buckets_and_ppl_into_outfile(buckets[1], buckets[2], ppl_ages, outfile)
        write_buckets_and_ppl_into_outfile(buckets[2], buckets[3], ppl_ages, outfile)
        write_buckets_and_ppl_into_outfile(buckets[3], oldest_age, ppl_ages, outfile, oper=operator.le)


if __name__ == "__main__":
    main()
