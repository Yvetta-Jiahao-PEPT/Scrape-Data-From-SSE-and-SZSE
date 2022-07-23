def get_url_data(page_num, date):
    url = 'http://query.sse.com.cn/commonQuery.do?jsonCallBack=jsonpCallback97417902&isPagination=true&pageHelp.pageSize=25&pageHelp.cacheSize=1&type=inParams&sqlId=COMMON_PL_SSGSXX_ZXGG_L&START_DATE=' + str(date) + '&END_DATE=' + str(date) +'&SECURITY_CODE=&TITLE=&BULLETIN_TYPE=&pageHelp.pageNo=' + str(page_num)  + '&pageHelp.beginPage=' + str(page_num) + '&pageHelp.endPage=' + str(page_num) + '&_=1631613647901'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36', 
               'referer' : 'http://www.sse.com.cn/'}
    response = requests.post(url, headers=headers)
    json_data = response.text[response.text.find('(')+1:].replace(')', '')
    format_data = json.loads(json_data)
    return format_data

def download_new_pdf(directory, files_we_had, date):

  page_num = 1
  format_data = get_url_data(page_num, date)

  while len(format_data['result']): 
    print('=' * 50, ' ', page_num, ' ', '=' * 50)
      
    for every_report in format_data['result']:
        source_pdf_url = every_report['URL']

        for report_index in range(len(source_pdf_url.split('<br>'))): 
          pdf_url = 'http://static.sse.com.cn' + source_pdf_url.split('<br>')[report_index]
          file_name = every_report['SECURITY_NAME'] + "："+ every_report['TITLE'].split('<br>')[report_index] + '.pdf'

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
  from requests.utils import default_headers

  tz = pytz.timezone('Asia/Shanghai') #get current time
  Beijing_now = datetime.now(tz)
  date = str(Beijing_now).split()[0]
#   date = '2022-5-11'

  # directory_shanghai = './上交所/' # absolute path (where we want to store data)
  directory_shanghai = '/Users/jiahaozhang/Desktop/上交所/' # absolute path (where we want to store data)

  
  if not os.path.isdir(directory_shanghai): # if we don't have this folder, we will create one to store data
    os.mkdir(directory_shanghai)

  files_we_had = os.listdir(directory_shanghai) # get pdf_names we have
  download_new_pdf(directory_shanghai, files_we_had, date)
