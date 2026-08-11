#goal: base pattern to use for (kinda) yoke sweater pattern, adjusts in pattern generator based off size

#pattern is worked from top-down using circular needles
#the needle size for the neckline ribbing are one US size smaller than main needle size

def weird_sweater():
    #materials list
    print('Materials needed:')
    print('Yarn: (WEIGHT PROVIDED) weight yarn, (YARDAGE CALCULATED) yards') #make yardage calculator lol
    print('Needles: US Size (NEEDLES PROVIDED) circular needles, US Size (NEEDLES PROVIDED -1) circular needles for ribbing')
    print('Stitch markers')
    print('Tapestry needle')
    print(' ')

    #pattern notes
    print('Pattern Notes:')
    print('This pattern is worked in the round from the top down, starting with the neckline')
    print('The pattern is worked in stockinette stitch, with increases at the yoke to shape the garment')
    print('This pattern was generated based on the size selected and the gauge provided')
    print('Stitch count was calculated based on the gauge provided, but please check your gauge before starting the pattern to ensure proper fit')
    print(' ')

    #mockneck
    print('Cast on (STS x INCH) stitches using the smaller needles')
    print('Join in the round, being careful not to twist stitches')
    print('Work in 1x1 (k1p1) rib for (ROWS x INCH, WHOLE NUMBER) rounds')
    print(' ')

    #yoke
    #increases at different points, dart-like structure
    #abbreviations: m1l and mir
    print('Switch to larger needles')
    print('Work one row in stockinette stitch')
    #adjust to allow for users to pick number of darts??
    #total sts/4 for distance between darts for 4pt increase, may need adjustment depending on yarn weight anyways
    #smaller yarn weight may mean 4pt increase is not enough, idk lowkey
    #im lowley going insane
    print(' ')
    #divide for body and sleeves
    print('Place (STS) on hold, CO (STS) foe right underarm, knit (STS) for body, place (STS) on hold, CO (STS) for left underarm, knit (STS) to BOR')
    print(' ')
    #body
    print('You should have (STS) on your needles for the body')
    print('Continue to work in stockinette stitch in the round until desired length from underarm')
    print('Switch to smaller needles')
    print('Work in 1x1 (k1p1) rib for (ROWS x 2.25 INCH, WHOLE NUMBER) rounds')
    print('Cast off all stitches')
    print(' ')
    #sleeves
    print('Place (STS) on the larger needles')
    print('Pick up and knit (STS) along the underarm and knit 1 stitch between underarm and sleeve')
    print('Continue work in the round using stockinette stitch')
    print('Decrease: k1, k2tog, work to last 3 sts, ssk, k1')
    print('Repeat decrease every (ROWS x SIZE SPECIFIC INCH, WHOLE NUMBER) rows for a total of (SIZE SPECIFIC NUMBER) times, ending with (SIZE SPEC STITCH COUNT) on your needles')
    print('Continue to work in stockinette stitch until sleeve measures (SIZE SPECIFIC INCH) from underarm')
    print('Switch to smaller needles')
    print('Work in 1x1 (k1p1) rib for (ROWS x 2.25 INCH, WHOLE NUMBER) rounds')
    print('Cast off all stitches')
    print(' ')
    #finishing
    print('Weave in ends')
    print('Block garment to desired measurements')
    print('yay sweater :)')