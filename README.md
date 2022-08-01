# 🔥📈🔥 Scrape Data From SSE and SZSE 🔥📈🔥


## Installation Guide 🏗️

Create the environment using
```bash
  conda env create -f environment.yml
```
Activate the environment 
```bash
  conda activate environmental
```

Or:
```bash
pip3 install requirements
```

## Usage/Examples 🧙
In terminal, we type   **crontab -e**   and copy code below in it (don't forget to replace **absolute_path** in the code below and in **Shanghai.py** and **Shenzhen.py**):

```bash
*/5 * * * * python3 /absolute_path/Shanghai.py
*/5 * * * * python3 /absolute_path/Shenzhen.py
```
In my computer, these are:
```bash
*/5 * * * * python3 /Users/jiahaozhang/Desktop/test_bash/Shanghai.py
*/5 * * * * python3 /Users/jiahaozhang/Desktop/test_bash/Shenzhen.py
```
Here, 5 means we scrath data every 5 mins. 


Run code below in terminal to stop this task:
```bash
crontab -r
```

## Authors
```bash
Yi-Yu Lin
Jiahao Zhang
```
