def test_rgb_to_html():
    import my_colours
    import matplotlib
    # define a colour that will enter enough if statements to give 100% coverage overall (i.e. it contains enough special characters)
    rgb_colour = [234, 12, 189]
    # use matplotlib to check what the value should be
    mpl_colour = matplotlib.colors.to_hex([rgb/255 for rgb in rgb_colour])
    my_colour = my_colours.rgb_to_hex(rgb_colour)
    assert mpl_colour == my_colour

def test_rainbow_palette():
    import my_colours
    # define a minimal palette which enters all if statements
    n = 6
    expected_palette = ['#ff0000', '#ffff00', '#00ff00', '#00ffff', '#0000ff', '#ff00ff']
    palette = my_colours.find_rainbow_palette(n)
    assert palette == expected_palette
