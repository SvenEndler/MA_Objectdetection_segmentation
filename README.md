# MA: Detection and Objectsegmentation in Maps
Dieses GitHub Repository enthält den Code und die Ergebnisse zur Masterarbeit mit dem Thema automatisierte Erkennung und Objektsegmentierung in Karten.  
Das System kombiniert etablierte Objekterkennungsverfahren mit einem Segmentierungsmodell.  
Das Ziel ist es Symbole und Piktogramme möglichst genau zu segmentieren und anschließend für die Weiterverarbeitung auszugeben.  

Das System zur Objekterkennung und anschließenden Segmentierung.
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ZWU8aGkynafYgWCbJ6BvnfV2RVm4XbOJ?usp=sharing)

Die Auswertung der Modelle.
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Wa5DQ-CiksjqLkfo302oSqIwvAB4cEIh?usp=sharing)

## Abstract:

Diese Masterarbeit beschäftigt sich mit der automatisierten Erkennung und 
Segmentierung von Symbolen und Piktogrammen in Karten. Dafür wurde ein System 
entwickelt, dass verschiedene Objekterkennungsverfahren nutzt und diese mit einem 
geeigneten Segmentierungsmodell kombiniert. Die Modelle YOLOv5, YOLOv8, Faster R
CNN, SSD und RetinaNet wurden vergleichend eingesetzt und auf zwei unterschiedlichen 
Datensätzen trainiert. Für die Segmentierung wird SAM verwendet. Der Datensatz für die 
einfachen Symbole erzielte insgesamt einen mAP50 Wert von 0,85 sowie eine mAP50-95 
von 0,51. Der zweite Datensatz für die Piktogramme konnte mit einer mAP50 von 0,56 und 
einer mAP50-95 von 0,30 eine schwächere Erkennungsleistung erzielen. Die Kombination 
aus automatischer Erkennung und Segmentierung bietet neue Möglichkeiten für die 
Kartografie in Hinblick auf die Analyse und Erstellung von Karten.  
