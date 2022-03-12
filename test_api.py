import requests

url = "http://127.0.0.1:8000/detect/"

payload={'name_cam': ''}
files=[
  ('image',('multi_face.jpeg',open('/home/dtnguyen/python/face_ver/face_detection/mask_detect_yolov5/test_data/img/multi_face.jpeg','rb'),'image/jpeg'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
