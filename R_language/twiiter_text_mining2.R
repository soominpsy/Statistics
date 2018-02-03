library(twitteR)
library(rJava)
library(KoNLP)
library(plyr)
#library(ggplot2)

###########################settings##########################

KEY_WORD = 'wine'
#DIR = "wine/0_friday/wine"   #1_monday 2_tuesday 3_wednesday 4_thursday 5_friday 6_saturday 7_sunday
#8_weekend  9_weekdays
DIR = "/korea/"
NUMBER_OF_TWEETS = 1000
BEGGING_SEARCHING_DATE = '2018-01-25'
END_OF_SEARCHING_DATE = '2018-01-26'
NEW_YORK = '40.758896,-73.985130,200km'
SOUTH_KOREA = '35.549684,127.094529,300km'
#############################################################

getwd()
setwd("~/Desktop/R_self/")
getwd()

apple_tweets = searchTwitter(KEY_WORD, n=NUMBER_OF_TWEETS, lang="en", since=BEGGING_SEARCHING_DATE ,until=END_OF_SEARCHING_DATE, geocode=NEW_YORK)
#head(apple_tweets)
#tail(apple_tweets)
length(apple_tweets)

pos.word=scan("positive-words.txt", what = "character", comment.char = ";")
#pos.word = scan("positive-words-ko-v2.txt", what = "character", comment.char = ";")
neg.word=scan("negative-words.txt", what = "character", comment.char = ";")  
# comment.char = ";" means do not run the line which begin with ;

score.sentiment = function(sentences, pos.word, neg.word, .progress="none") #.progress??
{
  require(plyr)
  require(stringr)
  
  scores = laply(sentences, 
                 function(sentences, pos.word, neg.word)
  {
    sentences = gsub("[[:punct:]]", "", sentences) # replacing(removing) all kinds of symbols
    sentences = gsub("[[:cntrl:]]", "", sentences) # replacing(removing) the "\n"
    sentences = gsub("\\d+","", sentences)   # replacing(removing) number
    
#    sentences = gsub("[\\.\\,\\;]+","",sentences) # remove dots
    sentences = gsub("https:[^ $]+","",sentences) # remove links 
#    sentences = gsub("@\\w+","",sentences) # remove at people
    
    sentences = tolower(sentences) # ABD -> abc
    word.list = str_split(sentences,"\\s+")
    words = unlist(word.list)
    
    pos.match = match(words, pos.word)
    neg.match = match(words, neg.word)
    
   # print(pos.match)
  #  print(neg.match)
    pos.match = !is.na(pos.match)
    neg.match = !is.na(neg.match)
    
    print(pos.match)
    print(neg.match)
    
    score = sum(pos.match) - sum(neg.match)
    return(score)
  }, pos.word, neg.word, .progress = .progress)
  
  scores.df = data.frame(score = scores, text = sentences)
  return(scores.df)
}

apple_text = laply(apple_tweets, function(t) t$getText())
apple_text = apple_text[!Encoding((apple_text))=="UTF-8"] # don't encode if not UTF-8

apple_scores = score.sentiment(apple_text, pos.word, neg.word, .progress="text")
apple_words = apple_scores$text
head(apple_words,10) 
length(apple_words)

apple_words = gsub("https:[^ $]+","",apple_words)
apple_words = gsub("[[:cntrl:]]", "",apple_words)

Score_of = apple_scores$score

NUMBER_OF_POSITIVE <- 0
NUMBER_OF_NEGATIVE <- 0
NUMBER_OF_NEUTURAL <- 0

for(i in 1:length(Score_of))
{
  if(Score_of[i]< -3) Score_of[i]=-3 
  else if(Score_of[i]> 4) Score_of[i]= 4
  if(Score_of[i]< -0.5) NUMBER_OF_NEGATIVE <- NUMBER_OF_NEGATIVE + 1
  if(Score_of[i]> 0.5) NUMBER_OF_POSITIVE <- NUMBER_OF_POSITIVE + 1
  if((Score_of[i]> -0.5) && (Score_of[i]< 0.5)) NUMBER_OF_NEUTURAL <- NUMBER_OF_NEUTURAL + 1
}

NUMBER_OF_NEGATIVE
NUMBER_OF_POSITIVE
NUMBER_OF_NEUTURAL

PRO_POS = NUMBER_OF_POSITIVE/length(Score_of)
PRO_NEU = NUMBER_OF_NEUTURAL/length(Score_of)
PRO_NEG = NUMBER_OF_NEGATIVE/length(Score_of)
PRO_POS
PRO_NEU
PRO_NEG

#Score_of
xrange = seq(-4,6,1) 
rangex = c(-4,6)

hist_info <- hist(Score_of+0.001, main=KEY_WORD, xlab='emotion', border="blue", col="green", xlim=rangex, breaks=xrange, panel.first=grid(), xaxt="n") #,prob=TRUE)
axis(1, at=hist_info$mids, labels = seq(10)-5)

write.table(hist_info$density, sub("REPLACE",DIR,"~/Desktop/R_self/temp/REPLACE_density.txt"),sep="\t")
write.table(hist_info$counts, sub("REPLACE",DIR,"~/Desktop/R_self/temp/REPLACE_counts.txt"),sep="\t")
write.table(hist_info$breaks, sub("REPLACE",DIR,"~/Desktop/R_self/temp/REPLACE_bins.txt"),sep="\t")
write.table(PRO_POS, sub("REPLACE",DIR,"~/Desktop/R_self/temp/REPLACE_Positive_propotion.txt"),sep="\t")
write.table(PRO_NEG, sub("REPLACE",DIR,"~/Desktop/R_self/temp/REPLACE_Negative_propotion.txt"),sep="\t")
write.table(PRO_NEU, sub("REPLACE",DIR,"~/Desktop/R_self/temp/REPLACE_Neutural_propotion.txt"),sep="\t")
write.table(length(Score_of),sub("REPLACE",DIR,"~/Desktop/R_self/temp/REPLACE_total_counts.txt"),sep="\t")
png(filename = sub("REPLACE",DIR,"~/Desktop/R_self/temp/REPLACE_plot.png"))
plot(hist_info)
dev.off()
length(Score_of)