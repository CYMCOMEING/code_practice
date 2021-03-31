
#https://www.cnblogs.com/68xi/p/9294309.html
#https://blog.csdn.net/sky04/article/details/5769517?utm_source=blogxgwz5
#https://www.jianshu.com/p/f1659aba5aed


#pip install py3-bencode
import time
from bencode import bdecode

# TODO 补完整getStruct获取key的所有信息

class Parser(object):

    def __init__(self, filePath):
        self.path = filePath
        metainfo_file = open(str(self.path), 'rb')
        self.metainfo = bdecode(metainfo_file.read())

        metainfo_file.close()

    def getStruct(self):
        print(self.metainfo.keys())

    def getAnnounce(self):
        return str(self.metainfo[b'announce'], encoding = "utf-8")
    
    def getAnnounceList(self):
        return self.metainfo[b'announce-list']

    # 如果是单文件就返回：0
    # 如果是多文件就返回:1
    def checkType(self):
        if b'files' in self.metainfo[b'info']:
            return 1
        else:
            return 0

    def getCreationDate(self):
        if b'creation date' in self.metainfo:
            return self.metainfo[b'creation date']
        else:
            return ''

    def getInfo(self):
        return self.metainfo[b'info'].keys()

     # 获得文件名
    def getName(self):

        info = self.metainfo[b'info']

        if b'name.utf-8' in info:
            filename = info[b'name.utf-8']
        else:
            filename = info[b'name']

        for c in filename:
            if c == b"b'":
                filename = filename.replace(c, b"\\\'")
        return str(filename, encoding = "utf-8")

    # 多文件的情况下，获得所有文件，返回为:dic

    def getInfoFiles(self):
        return self.metainfo[b'info'][b'files']

    def getPieceLength(self):
        return self.metainfo[b'info'][b'piece length']

    def getPieces(self):
        return self.metainfo[b'info'][b'pieces']

    # 返回创建时间
    def getCreatedBy(self):
        if b'created by' in self.metainfo:
            return str(self.metainfo[b'created by'], encoding = "utf-8")
        else:
            return ''

    # 获得编码方式
    def getEncoding(self):
        if b'encoding' in self.metainfo:
            return str(self.metainfo[b'encoding'], encoding = "utf-8")
        return ""

    def getComments(self):
        # info = self.metainfo[b'info']

        if b'comment.utf-8' in self.metainfo:
            comment = self.metainfo[b'comment.utf-8']
            return comment
        else:
            return ''


if __name__ == "__main__":
    parser = Parser('a.torrent')

    # print(parser.getStruct())
    # print(parser.getAnnounce())
    announceList = parser.getAnnounceList()
    for al in announceList:
        print(str(al[0], encoding = "utf-8"))
    # print(parser.getCreationDate())
    # print('creation date:'+time.strftime('%Y-%m-%d', time.localtime(parser.getCreationDate())))
    # print('comments:'+parser.getComments())
    # print('name:'+parser.getName())
    # print('encoding:'+parser.getEncoding())
    # print('created by:'+parser.getCreatedBy())
    # print(parser.getInfo())
    # print(parser.getPieceLength())
    with open('a.txt', 'w') as f:
        f.write(parser.getPieces().hex())
    # print(parser.checkType())
    # for file in parser.getInfoFiles():
    #     print("length:"+ str(file[b'length']))
    #     for path in file[b'path']:
    #         print(str(path, encoding = "utf-8"))
    #     print("######")
