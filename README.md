In terminal, we type   crontab -e   and copy code below in it (don't forget to replace absolute_path in the code below and in Shanghai.py and Shenzhen.py):


*/5 * * * * python3 /absolute_path/Shanghai.py
*/5 * * * * python3 /absolute_path/Shenzhen.py


In my computer, these are:
*/5 * * * * python3 /Users/jiahaozhang/Desktop/test_bash/Shanghai.py
*/5 * * * * python3 /Users/jiahaozhang/Desktop/test_bash/Shenzhen.py
