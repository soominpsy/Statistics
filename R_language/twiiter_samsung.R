library(twitteR)
#library(KoNLP)
library(plyr)
library(stringr)

setwd("~/Desktop/R_self/")

things_tweet = searchTwitter("#samsung", n = 1000)
head(things_tweet,3)

posi = scan("positive-words.txt", what = "character", comment.char = ";")
nega = scan("negative-words.txt", what = "character", comment.char = ";")

score.senti = function(tweet, posi, nega, .progress = "none")
{
  scores = laply(tweet, function(tweet, posi, nega )
  {
    tweet = gsub("[[:punct:]]","",tweet)
    tweet = gsub("[[:cntrl:]]","",tweet)
    tweet = gsub("\\d+","",tweet)
    tweet = gsub("https:[^ $]+","",tweet)
    
    tweet = tolower(tweet)
    word.list = str_split(tweet, "\\s+")
    words = unlist(word.list)
    
    pos_match = match(words, posi)
    neg_match = match(words, nega)
    pos_match = !is.na(pos_match)
    neg_match = !is.na(pos_match)
    score = sum(pos_match) - sum(neg_match)
    return(score)
  }, posi, nega, .progress = .progress)
  
  score.df = data.frame(score = scores, text = tweet)
  return(score.df)
}

things_text = laply(things_tweet, function(t) t$getText()) # remove who wrote it
#head(things_text,5)
#head(things_tweet,3)

things_text = things_text[!Encoding(things_text)=="UTF-8"] #removin all kinds of odds
#head(things_text,5)

things_score = score.senti(things_text, posi, nega, .progress = "text")
hist(things_score$score)
head(things_score$text,10)
