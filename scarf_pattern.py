#i need to create something basic so I do not go crazy
import math

def scarf(inch_sts, inch_rows, needle_size):
    print("Scarf Pattern Generator")
    #materials list
    print('Materials needed:')
    print('Yarn: (WEIGHT PROVIDED) weight yarn, (YARDAGE CALCULATED) yards') #make yardage calculator lol
    print('Needles: US Size (NEEDLES PROVIDED) circular needles, US Size (NEEDLES PROVIDED -1) circular needles for ribbing')
    print(' ')

    print('Pattern Notes:')
    print('This pattern follows the standard sizing for scarves')
    print('Width: 8.0 inches || Length: 60.0 inches')
    print(' ')

    #stitch options
    print('Stitch Options:')
    print('1. Garter Stitch')
    print('2. Stockinette Stitch')
    print('3. Moss Stitch')
    print(' ')
    stitch_selection = int(input("Select your stitch option: "))
    print(' ')

    if stitch_selection == 1:
        print('You have selected the garter stitch option.')
        print(f'Cast on {inch_sts * 8} stitches')
        print('Row 1: Knit all stitches')
        print('Row 2: Knit all stitches')
        print(f'Repeat rows 1 and 2 for a total of, {inch_rows * 60} rows')
        print('Cast off all stitches')
    elif stitch_selection == 2:
        print('You have selected the stockinette stitch option.')
        print(f'Cast on {inch_sts * 8}   stitches')
        print('Row 1: Knit all stitches')
        print('Row 2: Purl all stitches')
        print(f'Repeat rows 1 and 2 for a total of {inch_rows * 60} rows')
        print('Cast off all stitches')
    elif stitch_selection == 3:
        print('You have selected the moss stitch option.')
        print(f'Cast on {math.ceil((8.0 / 2) * inch_sts) * 2} stitches')
        print('Row 1: K1, P1 across')
        print('Row 2: K1, P1 across')
        print(f'Repeat rows 1 and 2 for a total of {inch_rows * 60} rows')
        print('Cast off all stitches')

