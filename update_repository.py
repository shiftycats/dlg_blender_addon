import json
import tomllib
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('repo', type=str)
parser.add_argument('--manifest', type=str, required=True)
parser.add_argument('--url', type=str, required=True)
parser.add_argument('--size', type=int, required=True)
parser.add_argument('--digest', type=str, required=True)

args = parser.parse_args()

with open(args.repo, 'r') as fp_repo, open(args.manifest, 'rb') as fp_manifest:
    repo = json.load(fp_repo)
    manifest = tomllib.load(fp_manifest)
    addon = repo['data'][0]

    # Tranfser
    for key, val in manifest.items():
        addon[key] = val

    addon['archive_url'] = args.url
    addon['archive_size'] = args.size
    addon['archive_hash'] = args.digest


with open(args.repo, 'w') as fp:
    json.dump(repo, fp, indent=2)
