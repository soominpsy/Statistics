library(twitteR)
library(RColorBrewer)
library(dplyr)
library(Rserve)
library(plyr)
#Rserve()
#.jinit()
library(rJava)
library(KoNLP)

SOUTH_KOREA = '35.549684,127.094529,300km'
setwd("~/Desktop/R_self/")
#korea_t = searchTwitter("카톡", n =10000, geocode=SOUTH_KOREA)

pos.word=scan("positive-words-ko-v2.txt", what = "character", comment.char = ";")
neg.word=scan("negative-words-ko-v2.txt", what = "character", comment.char = ";") 
#korea_t = gsub('[[:punct:]]','',korea_t)
#korea_t = gsub("[[:cntrl:]]","",korea_t)
#korea_t = gsub("http:[^ $]+","",korea_t)
korea_text = laply(korea_t, function(t) t$getText())
korea_text = korea_text[!Encoding((korea_text))=="UTF-8"]

korea_scores = score.sentiment(korea_text, pos.word, neg.word, .progress="text")
korea_words = korea_scores$text
korea_words = gsub("https:[^ $]+","",korea_words)
korea_words = gsub("[[:cntrl:]]", "",korea_words)
korea_words = gsub("[[:punct:]]", "",korea_words)
korea_words = gsub("\\d+","",korea_words)
korea_words = gsub("@\\w+","",korea_words)
korea_words = gsub("[\\.\\,\\;]+","",korea_words)

Score_of = korea_scores$score

#print(Score_of)
head(korea_t)
length(korea_t)