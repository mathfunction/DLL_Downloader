"""
	
	

	- gdown 
	- patool
	https://drive.google.com/uc?id=<google_drive_id>
	torch_1.10.0_cpu 		id=	1MZ5b2tyoJgyq9_wUtTlsRsT3fYFQodoM
	torch_1.10.0_cu102 		id=	1Moyl1DJ2EKL5mV-0y72Y0k55t2il607G
	torch_1.10.0_cu113   	id=	1606Un9nwGuAgtd78pprOn8A9F23js2kz

"""



import os
import subprocess
import patoolib


CODE_VERSION = "1"
THIS_FILE_DIR = os.path.dirname(os.path.abspath(__file__))


#====================================================================================================
fileDict = {
	# 偏好定義名         :  google_drive_id , file_name                    
	"torch_1.10.0_win10_cpu"  :["1MZ5b2tyoJgyq9_wUtTlsRsT3fYFQodoM","libtorch_cpu_dlls"],
	"torch_1.10.0_win10_cu102":["1Moyl1DJ2EKL5mV-0y72Y0k55t2il607G","libtorch_cu102_dlls"],
	"torch_1.10.0_win10_cu113":["1606Un9nwGuAgtd78pprOn8A9F23js2kz","libtorch_cu113_dlls"],
	"opencv_454_win10":["1ysiZZOMT5Wn4aSHZPdm-VOgrpjqzMl0m","opecv_world_454_vc15"]
}
#=====================================================================================================

def GoogleDriveDownloader(fileKey):
	if fileKey in fileDict:
		google_drive_id = fileDict[fileKey][0]
		file_dir = f"{THIS_FILE_DIR}/{fileDict[fileKey][1]}"
		file_rar_name = f"{THIS_FILE_DIR}/{fileDict[fileKey][1]}.rar" 
		if os.path.isdir(file_dir):
			print(f"{file_dir} has already exists !!")
			return
		else:
			# download from google drive
			subprocess.run(["gdown",f"https://drive.google.com/uc?id={google_drive_id}"])
			patoolib.extract_archive(file_rar_name,outdir=f"{THIS_FILE_DIR}/")
			os.remove(file_rar_name)
	else:
		print(f"{fileKey} not found !!")


if __name__ == '__main__':
	GoogleDriveDownloader("opencv_454_win10")


