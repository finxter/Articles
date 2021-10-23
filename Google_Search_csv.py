


''' Scrip for filling query in the search field''' 


# import necessary libraries
from selenium import webdriver
from time import sleep
import csv

# specify path of Chrome Driver
driver = webdriver.Chrome('/Users/mohamedthoufeeq/Desktop/chromedriver')


# use driver.get()method to navigate the web page by giving URL address
driver.get('https://www.google.com/')

# locate "English" Language by _Xpath / to change language to English
English = driver.find_element_by_xpath('//*[@id="SIvCob"]/a[2]')
English.click()
       
# locate search query form in html script by _name
search_query=driver.find_element_by_name("q")

# use send_keys() to simulate key strokes/ type the search term "python"
search_query.send_keys("python")

#locate Google Search button by _xpath
google_search_btn =driver.find_element_by_xpath('//*[@type="submit"]')

# use submit() to mimic enter key
google_search_btn.submit()

i = 1

sleep(1)

for i in range(7):
       Next_page = driver.find_element_by_xpath('//*[@id="pnnext"]')
       
       ''' Script for extracting Search result from "Organic Result" google element'''

       # locate url for organic results element from html script by _xpath
       organic_result = driver.find_elements_by_xpath('//*[@class="yuRUbf"]/a[@href]')


       # get all url and store it in variable "url_list1" list using for loop
       url_list1 = []
       for organic_url in organic_result:
               if not 'google' in organic_url.get_attribute("href"):
                   url_list1.append(organic_url.get_attribute("href"))
           
       # locate title of url for organic results element from html script by _xpath
       url1_title = driver.find_elements_by_xpath('//*[@class="LC20lb DKV0Md"]')

       # get all title of the url and store it in variable "title_url_list1" list using for loop
       title_url_list1 =[]
       for title_url1 in url1_title :
              text = title_url1.text
              title_url_list1.append(text)

       while i == 0:

              ''' Script for extracting Search result from "People also ask" google element'''
              # locate url in "People also ask" element from html script by _xpath

              People_quest = driver.find_elements_by_xpath('//*[@class="AuVD cUnQKe"]//a[@href]')
            
              # get all url and store it in variable "url_list2" list using for loop
              url_list2 = []
              for People_url in People_quest :
                     if not 'google' in People_url.get_attribute("href"):
                            if not 'search' in People_url.get_attribute("href"): 
                                   url_list2.append(People_url.get_attribute("href"))
              

              # locate title of url in "People also ask" element from html script by _xpath
              url2_title = driver.find_elements_by_xpath('//*[@class="iDjcJe IX9Lgd wwB5gf"]')

              # get all title of the url and store it in variable "title_url_list2" list using for loop
              title_url_list2 =[]
              for title_url2 in url2_title :
                     text = title_url2.text
                     title_url_list2.append(text)
                     sleep(1)                            
              
              ''' Script for extracting Search result from "Related Search" google element'''

              # locate url for Related Searches element from html script by _xpath
              related_search = driver.find_elements_by_xpath('//a[@class ="k8XOCe R0xfCb VCOFK s8bAkb"][@href]')

              # get all url and store it in variable "url_list5" list using for loop
              url_list5 = []
              for related_url in related_search :
                  url_list5.append(related_url.get_attribute("href"))           

              # locate title of url for organic results element from html script by _xpath
              url5_title = driver.find_elements_by_xpath('//*[@class="s75CSd OhScic AB4Wff"]')
              # get all title of the url and store it in variable "title_url_list5" list using for loop
              title_url_list5 = []
              for title_url5 in url5_title:  
                          text = title_url5.text
                          title_url_list5.append(text)
                          sleep(1)
                 
              ''' Script for extracting Search result from "Knowledge Graph" google element'''

              # locate the main title for Knowledge Graph element from html script by _xpath
              Know_Main_head = driverr.find_elements_by_xpath('//*[@class="K20DDe R9GLFb JXFbbc LtKgIf a1vOw BY2RHc"]')

              # get the main title  and store it in variable "text_url3" using for loop

              for title_url3 in Know_Main_head :
                   text_url3 = title_url3.text

              # locate description of Knowledge Graph element from html script by _xpath
              Know_desc = driver.find_elements_by_xpath('//*[@class="PZPZlf hb8SAc"]')

              # get description and store it in variable "text_desc" using for loop
              for desc in Know_desc:
                    text_desc = desc.text

              # locate title of sub head for Knowledge Graph element from html script by _xpath

              Know_subhead = driver.find_elements_by_xpath('//*[@class="rVusze"]')

              # get all title of the url and store it in variable "title_url_list1" list using for loop
              title_subhead = []
              for subhead in Know_subhead:
                   text = subhead.text
                   title_subhead.append(text)
                
              # locate title of url for Knowledge Graph  element from html script by _xpath
              Know_links_name = driver.find_elements_by_xpath('//*[@class="OS8yje oJc6P QTsT3e"]')

              # get all title of the url and store it in variable "title_url_list3" list using for loop
              title_url_list3 = []
              for title_url3 in Know_links_name: 
                   text = title_url3.text
                   title_url_list3.append(text)

              # locate url for Knowledge Graph element from html script by _xpath
              Know_graph = driver.find_elements_by_xpath('//*[@class ="mFVw3b"]//a[@href]')

              # get all url and store it in variable "url_list6" list using for loop
              url_list6 = []
              for graph_url in Know_graph :
                          url_list6.append(graph_url.get_attribute("href"))
                          sleep(1)
              ''' Script for extracting Search result from "Videos" google element'''

              # locate url for Videos element from html script by _xpath

              Video = driver.find_elements_by_xpath('//a[@class ="X5OiLe"][@href]')

              # get all url and store it in variable "vid_url" list using for loop
              vid_url = []
              for vid in Video :
                   vid_url.append(vid .get_attribute("href"))

                  
              # locate title of url for Videos element from html script by _xpath

              Video_title = driver.find_elements_by_xpath('//*[@class="fc9yUc oz3cqf p5AXld"]')

              # get all title of the url and store it in variable "title_url_list1" list using for loop
              vid_title = [] 
              for Vid_text in Video_title :
                        text = Vid_text.text
                        vid_title.append(text)
                        sleep(1)  
              # presenting the details in proper form
              o =  len(url_list2) + 1
              del url_list1[1 : o]
              i = i + 1              
       Next_page.click()
       sleep(10)      
with open('Google_Search.csv','w', newline = "") as Google:
                     Main_header1 = ["People also ask"]
                     People_header_writer = csv.DictWriter(Google, fieldnames = Main_header1)
                     People_header_writer.writeheader()
                     header1 = ['Question','URL']
                     People_writer = csv.DictWriter(Google, fieldnames = header1)
                     People_writer.writeheader()
                     for a,b in zip(title_url_list2,url_list2):
                            People_writer.writerow({'Question' : a , 'URL' : b })

                     Main_header2 = ["Related Search"]
                     Related_header_writer = csv.DictWriter(Google, fieldnames = Main_header2)
                     Related_header_writer.writeheader()
                     header2 = ['Search Terms','URL']
                     Related_writer = csv.DictWriter(Google, fieldnames = header2)
                     Related_writer.writeheader()
                     for c,d in zip(title_url_list5,url_list5):
                            Related_writer.writerow({'Search Terms' : c , 'URL' : d })

                     Main_header3 = ["Knowledge Graph"]
                     Knowledge_header_writer1 = csv.DictWriter(Google, fieldnames = Main_header3)
                     Knowledge_header_writer1.writeheader()

                     Know_Main_header = [text_url3] 
                     Know_Main_header_writer = csv.DictWriter(Google, fieldnames = Know_Main_header)
                     Know_Main_header_writer.writeheader()

                     Know_descp = [text_desc] 
                     Know_descp_writer = csv.DictWriter(Google, fieldnames = Know_descp)
                     Know_descp_writer.writeheader()

                     Know_subhead_header = ["subhead"] 
                     Know_subhead_writer = csv.DictWriter(Google, fieldnames = Know_subhead_header)
                     Know_subhead_writer.writeheader()
                     for i in zip(title_subhead):
                            Know_subhead_writer.writerow({'subhead' : i})

                     header3 = ['Title','URL']
                     Know_writer = csv.DictWriter(Google, fieldnames = header3)
                     Know_writer.writeheader()
                     for e,f in zip(title_url_list3,url_list6):
                            Know_writer.writerow({'Title' : e , 'URL' : f })

                     Main_header4 = ["Videos"]
                     Video_header_writer1 = csv.DictWriter(Google, fieldnames = Main_header4)
                     Video_header_writer1.writeheader()
                 
                     header4 = ['Title','URL']
                     Video_writer = csv.DictWriter(Google, fieldnames = header4)
                     Video_writer.writeheader()
                     for g,h in zip(vid_title,vid_url):
                            Video_writer.writerow({'Title' : g , 'URL' : h })

                     Main_header5 = ["Organic Results"]
                     Organic_header_writer1 = csv.DictWriter(Google, fieldnames = Main_header5)
                     Organic_header_writer1.writeheader()
                 
                     header5 = ['Web Site Name','URL']
                     Organic_writer = csv.DictWriter(Google, fieldnames = header5)
                     Organic_writer.writeheader()
                     for j,k in zip(title_url_list1,url_list1):
                            Organic_writer.writerow({'Web Site Name' : j , 'URL' : k })

