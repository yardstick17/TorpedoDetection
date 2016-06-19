from main import *
import argparse
parser = argparse.ArgumentParser(description='enabling debugging mode')

parser.add_argument("cut_off",
                     help="percentage cut off for target detection",
                     type=int)
args = parser.parse_args()

if __name__ == '__main__':
    detector_image = FileRead('DetectorOutput.blf')
    space_ship_image = FileRead('Ravager.blf')
    torpedo_image = FileRead('ProtonTorpedo.blf')
    targets = [(space_ship_image, 'Ravager'), (torpedo_image, 'ProtonTorpedo')]
    for target in targets:
        Y = target[0]
        target_name = target[1]
        col_pre = PreColoumn(Y, len(Y[0]))
        PreMatrix = PreProcessing(detector_image, len(Y[0]))
        Matching(PreMatrix, col_pre, len(col_pre), len(Y), len(Y[0]),
                 target_name , args.cut_off)
