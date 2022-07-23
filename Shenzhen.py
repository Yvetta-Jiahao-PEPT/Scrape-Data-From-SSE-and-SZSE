from requests.utils import default_headers

def get_url_data(page_num, date = ''):
    url = 'http://www.szse.cn/api/disc/announcement/annList?random={rdm}'.format(rdm = random.random())
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    formdata = {"seDate":[date,date],"channelCode":["listedNotice_disc"],"pageSize":50,"pageNum":page_num}
    response = requests.post(url, headers=headers, json=formdata)
    format_data = json.loads(response.text)
    return format_data

def download_new_pdf(directory, files_we_had, date):

  page_num = 1
  format_data = get_url_data(page_num, )


  while len(format_data['data']): 
    print('=' * 50, ' ', page_num, ' ', '=' * 50)
    if page_num == 3: 
      break
      
    for every_report in format_data['data']:
        pdf_url = 'http://disc.static.szse.cn/download' + every_report['attachPath']
        file_name = every_report['title'] + '.pdf'

        if file_name in files_we_had:
          continue
        else:
          files_we_had.append(file_name) # store this new file and then download it

          file_path = os.path.join(directory, file_name)

          pdf_file = requests.get(pdf_url, stream=True)
          with open(file_path, 'wb') as f:
              for chunk in pdf_file.iter_content(1024):
                  f.write(chunk)
              print('上市公司报告：%s' % file_name + "已经完成下载")

    page_num += 1
    format_data = get_url_data(page_num, default_headers)


if __name__ == "__main__":
  import json
  import os
  import pytz
  import requests
  import os.path
  from bs4 import BeautifulSoup
  from datetime import datetime

  tz = pytz.timezone('Asia/Shanghai') #get current time
  Beijing_now = datetime.now(tz)
  date = str(Beijing_now).split()[0]
  # date = '2022-5-11'

  # directory_shenzhen = './深交所/' # absolute path (where we want to store data
  directory_shenzhen = '/Users/jiahaozhang/Desktop/深交所/' # absolute path (where we want to store data)
  
  
  if not os.path.isdir(directory_shenzhen): # if we don't have this folder, we will create one to store data
    os.mkdir(directory_shenzhen)

  files_we_had = os.listdir(directory_shenzhen) # get pdf_names we have
  download_new_pdf(directory_shenzhen, files_we_had, date)
