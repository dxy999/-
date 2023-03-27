from aip import AipSpeech 
def get_file_content(file_name): 
    with open(file_name, 'rb') as fp:
        return fp.read()
APP_ID = '29358383'
API_KEY = 'I2L3nEW79kIqrWbLdZ8ZgRoE'
SECRET_KEY = '4IrgQ0qgkuo5mdXOY11nG7dbbTQ28oDH'
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
file_name= r'D:\研一\数据科学\data\test.wav' #使用语音：打开记事本
result = aipSpeech.asr(get_file_content(file_name), 'wav', 16000, {'dev_ip': '1536'})
#使用百度语音开放平台识别将其转换成文字命令，并执行该命令
print (result['result'][0])