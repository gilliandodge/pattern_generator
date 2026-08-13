#goal: base pattern to use for (kinda) yoke sweater pattern, adjusts in pattern generator based off size

#pattern is worked from top-down using circular needles
#the needle size for the neckline ribbing are one US size smaller than main needle size


def weird_sweater(inch_sts, inch_rows, needle_size, chosen_size_dict):

    size_label = chosen_size_dict["size"]
    bust_inch = chosen_size_dict["bust"]
    total_length = chosen_size_dict["length"]
    arm_circ = chosen_size_dict["arm_circ"]
    sleeve_length = chosen_size_dict["sleeve_length"]

    smaller_needle = needle_size - 1


    if needle_size >= 10:
        increase_points = 4
    elif needle_size <= 6:
        increase_points = 8
    else:
        increase_points = 6


    # Neckline setup
    neck_inch = 16 if bust_inch < 42 else (18 if bust_inch < 50 else 20)
    cast_on_sts = int(neck_inch * inch_sts)
    if cast_on_sts % 2 != 0: 
        cast_on_sts += 1

    # Body Math 
    body_target_sts = int(bust_inch * inch_sts)
    if body_target_sts % 2 != 0: 
        body_target_sts += 1
    
    # Sleeve Math
    sleeve_target_sts = int(arm_circ * inch_sts)
    
    # Underarm setup
    underarm_sts = int(body_target_sts * 0.08)
    if underarm_sts % 2 != 0: 
        underarm_sts += 1

    # Active yoke target before split
    total_yoke_sts = (body_target_sts - (underarm_sts * 2)) + (sleeve_target_sts * 2)

    # Ribbing rounds
    body_rib_rounds = round(inch_rows * 2.25)
    neck_rib_rounds = round(inch_rows * 1.5)


    #materials list
    print('Materials needed:')
    print('Yarn: (WEIGHT PROVIDED) weight yarn, (YARDAGE CALCULATED) yards') #make yardage calculator lol
    print(f'Needles: US Size {needle_size} circular needles, US Size {smaller_needle} circular needles for ribbing')
    print('Tapestry needle')
    print(' ')

    #pattern notes
    print('Pattern Notes:')
    print('This pattern is worked in the round from the top down, starting with the neckline')
    print('The pattern is worked in stockinette stitch, with increases at the yoke to shape the garment')
    print(f'Generated for Size: {size_label} ({bust_inch}" Bust) based on a gauge of {inch_sts} sts / {inch_rows} rows per inch.')
    print('Stitch count was calculated based on the gauge provided, but please check your gauge before starting the pattern to ensure proper fit')
    print(' ')

    #mockneck
    print('Mockneck: 1x1 Ribbing')
    print(f'Cast on {neck_inch * inch_sts} stitches using the smaller needles')
    print('Join in the round, being careful not to twist stitches')
    print(f'Work in 1x1 (k1p1) rib for {neck_rib_rounds} rounds')
    print(f'Total Stitches on needles: {neck_inch * inch_sts}')
    print(' ')

    #yoke
    #increases at different points, dart-like structure
    #abbreviations: m1l and mir
    print('Yoke: Stockinette Stitch')

    base_section_sts = cast_on_sts // increase_points
    setup_knit_sts = base_section_sts - 1

    print(f'Switch to larger (US {needle_size}) needles')
    print(f'Setup Round: *Knit {setup_knit_sts}, place marker; repeat from * around to BOR.')
    print(f'(This divides your {cast_on_sts} stitches into {increase_points} sections. The first stitch after each marker is your triangle center.)')
    print(' ')
    print('Establish the shifting triangle darts by repeating these two rounds:')
    print('Round 1 (Increase): *M1L, k1, M1R, knit to next marker; repeat from * around.')
    print('Round 2 *Knit to 1 stitch before marker, remove marker, k1, replace marker; repeat from * around.')
    print('(Note: Moving the marker left by 1 stitch every plain round creates the triangle pattern)')
    print(' ')
    print(f'Repeat Rounds 1 and 2 until you have a total of {total_yoke_sts} stitches on your needles.')
    print(' ')
    print(' ')
    #im lowkey going insane
    print(f'Total Stitches on needles: {total_yoke_sts}')
    print(' ')

    #divide for body and sleeves
    print(f'Place {sleeve_target_sts / 2} on hold, CO {underarm_sts} for right underarm, knit {body_target_sts / 2} for body, place {(sleeve_target_sts / 2)} on hold, CO {underarm_sts} for left underarm, knit {body_target_sts / 2} to BOR')
    print(' ')
    #body
    print(f'You should have {body_target_sts + (underarm_sts * 2)} stitches on your needles for the body')
    print('Continue to work in stockinette stitch in the round until desired length from underarm')
    print(f'Switch to smaller needles (US {smaller_needle})')
    print(f'Work in 1x1 (k1p1) rib for {body_rib_rounds} rounds')
    print('Cast off all stitches')
    print(' ')
    #sleeves
    print(f'Place {sleeve_target_sts / 2} on the larger needles')
    print('Pick up and knit (STS) along the underarm and knit 1 stitch between underarm and sleeve')
    print('Continue work in the round using stockinette stitch')
    print('Decrease: k1, k2tog, work to last 3 sts, ssk, k1')
    print(f'Repeat decrease every {sleeve_decrease_interval} rows for a total of {sleeve_decrease_count} times, ending with {sleeve_final_sts} on your needles')
    print(f'Continue to work in stockinette stitch until sleeve measures {sleeve_length} inches from underarm')
    print('Switch to smaller needles')
    print(f'Work in 1x1 (k1p1) rib for {sleeve_rib_rounds} rounds')
    print('Cast off all stitches')
    print(' ')
    #finishing
    print('Weave in ends')
    print('Block garment to desired measurements')
    print('yay sweater :)')