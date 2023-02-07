from fit2gpx import StravaConverter
import argparse

parser = argparse.ArgumentParser(
    prog='fit2gpx',
    description='Command line utility to parse strava data downloads'
)
parser.add_argument('input_dir',help="input folder with the unzipped strava library",)
parser.add_argument('output_dir',help='path to output folder')


def main(input_dir,output_dir):
    # Step 1: Create StravaConverter object 
    # - Note: the dir_in must be the path to the central unzipped Strava bulk export folder 
    # - Note: You can specify the dir_out if you wish. By default it is set to 'activities_gpx', which will be created in main Strava folder specified.

    strava_conv = StravaConverter(
        dir_in=input_dir,
        dir_out=output_dir
    )

    # Step 2: Unzip the zipped files
    strava_conv.unzip_activities()

    # Step 3: Add metadata to existing GPX files
    strava_conv.add_metadata_to_gpx()

    # Step 4: Convert FIT to GPX
    strava_conv.strava_fit_to_gpx()


if __name__ == "__main__":
    args = parser.parse_args()
    main(input_dir=args.input_dir,
    output_dir = args.output_dir)
    print('nice')