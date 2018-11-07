#!/usr/bin/env python3

import sys
import os
import json
import operator


# Load the JSON into a dict
try:
    with open(sys.argv[1]) as infile:
        my_dict = json.load(infile)

# The script aborts if the path to JSON is not passed as a second arg
except (FileNotFoundError, IndexError):
    print('USAGE: python3', os.path.basename(sys.argv[0]), '<path to JSON>')
    sys.exit()

# Preparing the data into lists and strings
buckets = sorted(my_dict['buckets'])
ppl_ages = my_dict['ppl_ages']
oldest_age = max(ppl_ages.values())
output_file = 'my_list.yml'


def write_buckets_and_ppl(start_bucket, end_bucket, outfile, operator=operator.lt):
    """
    Organizes people into age buckets and write the data into outfile.
    :param start_bucket:
    :param end_bucket:
    :param outfile:
    :param operator:
    """
    outfile.write(f"{start_bucket}-{end_bucket}:\n")

    for person in ppl_ages:
        if start_bucket <= ppl_ages[person] and operator(ppl_ages[person], end_bucket):
            outfile.write(f"- :{person}\n")


# Write the data into outfile in YAML style
with open(output_file, 'w') as outfile:
    outfile.write(f"---\n")
    write_buckets_and_ppl(buckets[0], buckets[1], outfile)
    write_buckets_and_ppl(buckets[1], buckets[2], outfile)
    write_buckets_and_ppl(buckets[2], buckets[3], outfile)
    write_buckets_and_ppl(buckets[3], oldest_age, outfile, operator=operator.le)
