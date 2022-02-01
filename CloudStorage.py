pip3 install dropbox
import dropbox

class A:
    def __init__(self,accesstoken):
        self.accesstoken=accesstoken
        
    def uploadfile(self,filefrom,filetwo):
        dbx=dropbox.Dropbox(self.accesstoken)
        f=open(filefrom,'rb')
        dbx.files_upload(f.read(),filetwo)

#main code
#access token
accesstoken="123"
#creating class object
o=A(accesstoken)
filefrom=input("enter the file path which want to transfer")
file2=input("enter the name to upload the dropbox")
o.uploadfile(filefrom,file2)
print("file has moved")