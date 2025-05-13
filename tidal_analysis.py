#!/usr/bin/env python3

# import the modules you need here
import argparse
import pandas as pd
import os
import glob


def read_tidal_data(filename):
    tide_data=pd.read_csv(r"w2k\user\nkj513\(H:)\SEpwC_tidal_assessment\data\Aberdeen,sep='\t'")
    all_files = glob.glob(
        f"{r'w2k\user\nkj513\(H:)\SEpwC_tidal_assessment\data\Aberdeen'}/*.csv"
        )
    list_of_dataframes = []
    
    for filename in all_files:
        try: 
            df=pd.read_txt(filename,sep='\t')
            list_of_dataframes.append(df)
            print(f"Successfully read: {filename}")
        except Exception as e:
            print (f"Error reading {filename}: {e}")
            
            return list_of_dataframes
        
    
def extract_single_year_remove_mean(year, data):
    
    return 


def extract_section_remove_mean(start, end, data):


    return 


def join_data(data1, data2):

    return 



def sea_level_rise(data):

                                                     
    return 

def tidal_analysis(data, constituents, start_datetime):


    return 

def get_longest_contiguous_data(data):


    return 

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
                     prog="UK Tidal analysis",
                     description="Calculate tidal constiuents and RSL from tide gauge data",
                     epilog="Copyright 2024, Jon Hill"
                     )

    parser.add_argument("directory",
                    help="the directory containing txt files with data")
    parser.add_argument('-v', '--verbose',
                    action='store_true',
                    default=False,
                    help="Print progress")

    args = parser.parse_args()
    dirname = args.directory
    verbose = args.verbose
    


