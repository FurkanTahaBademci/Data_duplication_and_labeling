
# Data duplication and labeling

Yapay zeka algoritmalarında kullanılacak verilerin sentetik olarak çoğaltılması ve çoğaltma işlemi yaparken aynı zamanda da yolo etiket formatında etiketlemesi yapılmaktadır. Ekleme yapılacak nesnelerin .png formatında arka plansız görüntülerine ihtiyac duyulmaktadır.


In artificial intelligence , usage data is synthetically stored and replicated, while at the same time, yolo label format is saved. to be added needs backgroundless images in .png format.


## İnput

<img src="https://raw.githubusercontent.com/furkantahabademci/Data_duplication_and_labeling/main/examples/input.jpeg" width="700"/>


## Output

<img src="https://raw.githubusercontent.com/furkantahabademci/Data_duplication_and_labeling/main/examples/output.jpeg" width="700"/>


## Labeling

<img src="https://raw.githubusercontent.com/furkantahabademci/Data_duplication_and_labeling/main/examples/labelimg.jpg" width="700"/>

<br>


## Özellikler

- Birden fazla nesneyi ekleme ve farklı tuş kombinasyonlarına atama
- Çoğaltma işlemi yaparken eş zamanlı etiket de yapılması
- Kolay kullanım

<br>

  
## Bilgisayarınızda Çalıştırın

Projeyi klonlayın

```bash
  git clone https://github.com/furkantahabademci/Data_duplication_and_labeling.git
```

Proje dizinine gidin

```bash
  cd Data_duplication_and_labeling
```

Gerekli paketleri yükleyin


Görüntüleri ve txt belgelerini ./input klasorüne ekleyin 
<br>
<br>
Txt belgelerini ./output klasorüne ekleyin 
<br>


```bash
  pip install requirements.txt
```

Kodu çalıştırın

```bash
  python main.py
```

  

    