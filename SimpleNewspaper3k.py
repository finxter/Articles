from newspaper import Article

# create an article object
article = Article('https://www.cnbc.com/2021/02/02/5-freelance-jobs-where-you-can-earn-100000-or-more-during-pandemic.html')
article.download()
article.parse()
article.nlp()

title = article.title
link = article.url
authors = article.authors
date = article.publish_date
image = article.top_image
summary = article.summary
text = article.text

print('**********************************')
print(f'Title: {title}')
print(f'Link: {link}')
print(f'Authors: {authors}')
print(f'Publish Date: {date}')
print(f'Top Image: {image}')
print(f'Summary: ')
print(summary)
print('**********************************')
