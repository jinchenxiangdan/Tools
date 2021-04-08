#
# Author: Shawn Jin
# Purpose: random generate user data
#



#
# install packages if the package is not installed.
#

packages = c("randomNames")

# load or install if not installed & load all
package.check <- lapply(
    packages,
    FUN = function(x) {
        # if not installed, install it and its dependencies 
        if (!require(x, character.only = TRUE)) {
            install.packages(x, dependencies = TRUE)
            library(x, character.only = TRUE)
        }
    }
)

# show current working directory and set working directory
getwd()
setwd('D:/Projects/Tools')

# set the attributes and types of it

attributes <- c("user_id", "gomoku_total_hours", "current_gomoku_rank_score")

set.seed(1)
id_pools <- (sample.int(1000, 1000))
id_pools




