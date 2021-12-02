# You have to gauge whether or not father is already
# twice as old or how many years it would take to be twice as old
# or lastly how many years it has been that he was twice as old

# How to go about it?
# Step 1. I'll would say subtract the son's age from the dad's age.

# Step 2. 
# An approach I take is to multiply the son's age by 2. That's
# a benchmark that looks appropriate for me.

# Step 3.
# With these 2 benchmarks under our belt we can start to compare 
# them to each other and actually echo out the following listing:

# 1 --> Father could be at this exact moment twice as old
# 2 --> Father already has been twice as old
# 3 --> Father still has to become twice as old

dad_years_old=$1
son_years_old=$2

# step 1
benchmark_1=$(($1 - $2))
# step 2
benchmark_2=$(($2 * 2))

# step 3

# scenario 1 and 2. Father is at this very moment twice as old
# or father has already been twice as old
if (($1 >= $benchmark_2)); then
    echo $(( $1 - $benchmark_2 ))
fi

# scenario 3. Father still has to become twice as old
if (($1 < $benchmark_2)); then
    echo $(($benchmark_2 - $1))
fi
exit
