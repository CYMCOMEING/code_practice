# pip install googletrans-temp

from googletrans import Translator


translator = Translator(service_urls=['translate.google.cn'])
print("翻译中文:"+translator.translate('星期日').text)

print("翻译英文:"+translator.translate('Sunday', dest='zh-CN').text)

print("检测源文本的语言:",translator.detect('일요일'))
