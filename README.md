## Özellikler
- Python ve C/C++ destekli kod altyapısı
- Jatson Nano + Raspberry Pi uyumlu
- QGroundControl ve MAVLink (pymavlink) ile iletişim
- PID kontrol algoritması örneği
- OpenCV ile veri ön işleme altyapısı

## Klasör Yapısı
```plaintext
.
├── README.md
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── control
│   │   ├── pid.py            # Python PID algoritması
│   │   └── pid.cpp           # C++ PID algoritması
│   ├── vision
│   │   └── preprocessor.py   # OpenCV ile veri ön işleme
│   ├── communication
│   │   └── mavlink_comm.py   # pymavlink ile iletişim
│   └── main.py               # Proje ana dosyası
├── CMakeLists.txt            # C/C++ derleme ayarları
├── scripts
│   └── flash_pixhawk.sh      # QGroundControl/Pixhawk için yükleme scripti
└── tests
    └── test_pid.py
```

## Kurulum
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Kullanılan Kütüphaneler
- numpy
- opencv-python
- pymavlink
- pytest
