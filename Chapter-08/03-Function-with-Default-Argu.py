# Function with one default parament "dB"
def adjust_vol(level, unit="dB"):
    print(f"Volume set to {level}{unit}")

# Function calling with one argument
adjust_vol(10)

# Function calling with two arguments
adjust_vol(30, "%")