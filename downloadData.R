dl_data<-function(url = "https://assets.datacamp.com/production/course_1639/datasets/messy_stock_data.tsv"){
  download.file(url, destfile = "yahooStockMessy.tsv", mode = "wb")
}
