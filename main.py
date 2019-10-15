# -*- coding: utf-8 -*-
import os
import time
import shutil

apkFileName = "tangguo.apk"
apkFolderName = apkFileName.split(".")[0]

apkPackageOriginName = "com.qp168.tgqpxxxxx"
apkPackageAfterName = "com.qp168.tgqpxxxxxss"

# 解包
if not os.path.exists(apkFolderName):
    print("正在解包中..." + apkFileName)
    os.popen("apktool.bat d " + apkFileName)
    time.sleep(10)
    

# 修改manifest
print("正在修改包名..." + apkPackageOriginName + "=>" + apkPackageAfterName)
f = open("./" + apkFolderName + "/AndroidManifest.xml","r+")
content =  f.read()
content = content.replace(apkPackageOriginName,apkPackageAfterName)
f.close()
f = open("./" + apkFolderName + "/AndroidManifest.xml","w")
f.write(content)
f.close()

# 打包
print("正在打包中...")
result = os.popen("apktool.bat b " + apkFolderName)
time.sleep(20)

print("拷贝中...")
shutil.copyfile("./" + apkFolderName + "/dist/" + apkFileName , "./" +apkFolderName + "_"+ apkPackageAfterName + "_unSign.apk")
time.sleep(5)
print("正在签名中...")
result = os.popen("apksigner sign --ks tangguo11.keystore --ks-pass pass:123456 --key-pass pass:123456 --in "  + apkFolderName + "_"+ apkPackageAfterName + "_unSign.apk --out "  + apkFolderName + "_"+ apkPackageAfterName + "_sign.apk")

time.sleep(5)
print("清理资源中...")
os.remove( apkFolderName + "/dist/" + apkFileName )
os.remove( apkFolderName + "_"+ apkPackageAfterName + "_unSign.apk")
print("Success!")

