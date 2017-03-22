#!/usr/bin/python
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("target", type=str,
                    help="path to dir or file")
parser.add_argument("adress_to_copy", type=str,
                    help="remote adress which will store copy")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()
if args.verbose:
    print("Copy local {} to remote machine with adress {}".format(args.target, args.adress_to_copy))
else:
    print(args.target, args.adress)
os.system("rsync {0} {1}".format(args.target, args.adress_to_copy))
