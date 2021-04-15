#
# Author: Shawn Jin
# Purpose: random sampling a 2,500,000 dataset into 5 subsets and make sure the 
#           predict var, 'success' or 'fail' in this case, is about half and half.


# setwd('H:')

# read file 
kick_starter <- read.csv('Kickstarter-full-raw.csv', na.strings = 'NA')
str(kick_starter)
# list part of data 
head(kick_starter, 12)
class(kick_starter)

# count success and fail cases 
count <- ifelse(kick_starter$goal > kick_starter$pledged, 'success', 'fail')
class(count)
sum(count == "success")
sum(count == "fail")

# 400000 for each sample, because there are only about 1000k success cases, and 
# need to the dataset contains half and half about success and fail.
SAMPLE_DATASET_SIZE = 400000

# split kick starter data into two groups: success or fail
kick_starter_split <- split(kick_starter, kick_starter$goal >= kick_starter$pledged)
str(kick_starter_split)
kick_starter_success <- kick_starter_split$"TRUE"
kick_starter_fail <- kick_starter_split$"FALSE"

# random sampling 5 datasets
FILE_NAME = "kickstarter_random_sampling"
PART_SAMPLE_SIZE = SAMPLE_DATASET_SIZE / 2 

random_sampling_dataset_success <- split(kick_starter_success,
                                         sample(rep(1:5, times=c(PART_SAMPLE_SIZE,
                                                                 PART_SAMPLE_SIZE,
                                                                 PART_SAMPLE_SIZE,
                                                                 PART_SAMPLE_SIZE,
                                                                 PART_SAMPLE_SIZE)),
                                                replace = FALSE))
random_sampling_dataset_fail <- split(kick_starter_fail,
                                         sample(rep(1:5, times=c(PART_SAMPLE_SIZE,
                                                                 PART_SAMPLE_SIZE,
                                                                 PART_SAMPLE_SIZE,
                                                                 PART_SAMPLE_SIZE,
                                                                 PART_SAMPLE_SIZE)),
                                                replace = FALSE))
str(random_sampling_dataset_success)
random_sampleing_dataset <- rbind(random_sampling_dataset_success$'1',
                                  random_sampling_dataset_fail$'1')
str(random_sampleing_dataset)

# write into 5 files 
for (i in 1:5) {
    index <- toString(i)
    print(index)
    random_sampleing_dataset <- rbind(random_sampling_dataset_success[[index]],
                                      random_sampling_dataset_fail[[index]])

    # write.csv(random_sampleing_dataset, paste(FILE_NAME, toString(i)))
}


















