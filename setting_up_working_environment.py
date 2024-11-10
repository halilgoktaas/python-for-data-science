#sanal ortalmların listelenmes:
#conda env list
#sanal ortam oluşturma:
#conda create -n myenv
#sanal ortamı aktif etme:
#conda activate myenv
#yüklü paketlerin listelenmesi:
#conda list
#paket yükleme:
#conda install numpy
#aynı anda birden fazla paket yükleme
#conda install numpy scipy pandas
#paket silme:
#conda remove package_name
#belirli bir versiyona göre paket yükleme:
#conda install numpy= 1.20.1
#paket yükseltme:
#conda upgrade conda
#tüm paketlerin yükseltilmesi:
#conda upgrade -all

#pip ile nasıl yapılır:
#pip install paket_Adi
#paket yükleme versiyona göre:
#pip install pandas==1.2.1

#oluşturduğun paketleri dosyalama:
#conda env export > dosya_adi
#oluşturduğun sanal ortamı silme:
#conda env remove -n myenv

#oluşturduğun sanal ortamdaki paketleri başkasına aktarma hemen:
#conda env create -f olustdurdugun_yml_dosyası