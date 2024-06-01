from database import LINKS_COLLECTION, SOURCES_COLLECTION

news_urls = [
  ('https://vnexpress.net/kinh-doanh/chung-khoan', 'https://vnexpress.net', 'title-news', 'title-news', 'description'),
  ('https://vnexpress.net/thoi-su', 'https://vnexpress.net', 'title-news', 'title-news', 'description'),
  ('https://vnexpress.net/thoi-su/chinh-tri', 'https://vnexpress.net', 'title-news', 'title-news', 'description'),
  ('https://kinhtedothi.vn/tai-chinh-chung-khoan.html', 'https://kinhtedothi.vn', 'story__title', 'story__title', 'story__summary'),
  ('https://kinhtedothi.vn/thoi-su.html', 'https://kinhtedothi.vn', 'story__title', 'story__title', 'story__summary'),
  ('https://kinhtedothi.vn/do-thi.html', 'https://kinhtedothi.vn', 'story__title', 'story__title', 'story__summary'),
  ('https://www.nytimes.com/section/politics', 'https://www.nytimes.com', 'css-1l4spti', 'css-8hzhxf', 'css-1l4spti'),
  ('https://www.nytimes.com/section/business', 'https://www.nytimes.com', 'css-1l4spti', 'css-8hzhxf', 'css-1l4spti'),
  ('https://www.nytimes.com/section/world/asia', 'https://www.nytimes.com', 'css-1l4spti', 'css-8hzhxf', 'css-1l4spti'),
  ('https://www.nytimes.com/section/world/africa', 'https://www.nytimes.com', 'css-1l4spti', 'css-8hzhxf', 'css-1l4spti'),
  ('https://www.nytimes.com/section/world/americas', 'https://www.nytimes.com', 'css-1l4spti', 'css-8hzhxf', 'css-1l4spti'),
  ('https://www.nytimes.com/section/world/australia', 'https://www.nytimes.com', 'css-1l4spti', 'css-8hzhxf', 'css-1l4spti'),
  ('https://www.nytimes.com/section/world/europe', 'https://www.nytimes.com', 'css-1l4spti', 'css-8hzhxf', 'css-1l4spti'),
  ('https://www.nytimes.com/section/world/middleeast', 'https://www.nytimes.com', 'css-1l4spti', 'css-8hzhxf', 'css-1l4spti'),
  ('https://www.nytimes.com/section/world/middleeast', 'https://www.nytimes.com', 'css-1l4spti', 'css-8hzhxf', 'css-1l4spti'),
  ('https://www.fox9.com/news', 'https://www.fox9.com', 'info-header', 'info-header', 'no-summary'),
  ('https://www.fox9.com/money', 'https://www.fox9.com', 'info-header', 'info-header', 'no-summary'),
  ('https://www.indiatimes.com', 'https://www.indiatimes.com', 'card-heading', 'card-heading', 'no-summary'),
  ('https://www.indiatimes.com/news/india', 'https://www.indiatimes.com', 'card-title', 'card-title', 'no-summary'),
  ('https://www.indiatimes.com/news/world', 'https://www.indiatimes.com', 'card-title', 'card-title', 'no-summary'),
  ('https://www.indiatimes.com/news/sports', 'https://www.indiatimes.com', 'card-title', 'card-title', 'no-summary'),
  ('https://www.news18.com/', 'https://www.news18.com', 'sub_headstory_title', 'sub_headstory_title', 'no-summary'),
  ('https://www.news18.com/india/', 'https://www.news18.com', 'blog_list_row', 'blog_list_row', 'no-summary'),
  ('https://news.google.com', 'https://news.google.com', 'gPFEn', 'gPFEn', 'no-summary'),
  ('https://finance.yahoo.com', 'https://finance.yahoo.com', 'subtle-link', 'subtle-link', 'no-summary'),
  ('https://finance.yahoo.com', 'https://finance.yahoo.com', 'subtle-link', 'subtle-link', 'no-summary'),
  ('https://www.forbes.com/', 'https://www.forbes.com', 'happening__title', 'happening__title', 'no-summary'),
  ('https://www.forbes.com/', 'https://www.forbes.com', 'happening__title', 'happening__title', 'no-summary'),
  ('https://www.forbes.com/worlds-billionaires', 'https://www.forbes.com', '_1-FLFW4R', '_1-FLFW4R', 'no-summary'),
  ('https://www.forbes.com/ai', 'https://www.forbes.com', '_1-FLFW4R', '_1-FLFW4R', 'no-summary'),
  ('https://www.forbes.com/big-data', 'https://www.forbes.com', '_1-FLFW4R', '_1-FLFW4R', 'no-summary'),
  ('https://www.forbes.com/careers', 'https://www.forbes.com', '_1-FLFW4R', '_1-FLFW4R', 'no-summary'),
  ('https://www.theguardian.com/international', 'https://www.theguardian.com', 'dcr-16c50tn', 'dcr-16c50tn', 'no-summary'),
  ('https://www.theguardian.com/uk/commentisfree', 'https://www.theguardian.com', 'dcr-16c50tn', 'dcr-16c50tn', 'no-summary'),
  ('https://www.cgtn.com', 'https://www.cgtn.com', 'news-item-content-title', 'news-item-content-title', 'no-summary'),
  ('https://www.cgtn.com/china', 'https://www.cgtn.com', 'news-headline', 'news-headline', 'no-summary'),
  ('https://www.cgtn.com/world', 'https://www.cgtn.com', 'news-headline', 'news-headline', 'no-summary'),
  ('https://www.globaltimes.cn', 'https://www.globaltimes.cn', 'new_title_s', 'new_title_s', 'new_form02'),
  ('https://www.globaltimes.cn/china/index.html', 'https://www.globaltimes.cn', 'new_title_ms', 'new_title_ms', 'no-summary'),
  ('https://www.globaltimes.cn/opinion/index.html', 'https://www.globaltimes.cn', 'new_title_ms', 'new_title_ms', 'no-summary'),
]

# Insert the news sources into the database
for source in range(0, len(news_urls)):
  SOURCES_COLLECTION.insert_one({
    "id": source,
    "source": news_urls[source][0],
    "site": news_urls[source][1],
    "urlTag": news_urls[source][2],
    "titleTag": news_urls[source][3],
    "summaryTag": news_urls[source][4]
  })

# for source in range(0, len(news_urls)):
#   source_id = source,
#   source = news_urls[source][0]
#   print(source_id, source)