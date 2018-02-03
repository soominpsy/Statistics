library(twitteR)
library(RColorBrewer)
library(dplyr)
library(Rserve)
#Rserve()
#.jinit()
library(rJava)
library(KoNLP)

SOUTH_KOREA = '35.549684,127.094529,300km'

iphone_t = searchTwitter("커피", n =50, geocode=SOUTH_KOREA)
head(iphone_t)
#tail(iphone_t)
#iphone_t = gsub('[[:punct:]]','',iphone_t)
#iphone_t = gsub("[[:cntrl:]]","",iphone_t)
#iphone_t = gsub("http:[^ $]+","",iphone_t)
head(iphone_t)

length(iphone_t)