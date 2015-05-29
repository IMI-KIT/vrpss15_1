# vrpss15_1
Virtual reality practical course summer 2015 group 1

Achtet darauf, immer die aktuelle polyVR-Version zu haben, der Code in unserer Fabrik benutzt Funktionen, die dafür erst hinzugefügt wurden.


###Container

Der Container ist insgesamt als Stack organisiert, nicht als Queue!
`container.get()` ruft intern  `self->obj->pop()` auf, dh. das Objekt ist danach nicht mehr im Container. Der Container ist intern als vector organisiert, bei dem Objekte am Ende hinzugefügt und weggenommen werden (`push_back` und `pop_back`) 

```
FProduct* FContainer::pop() {
    FProduct* p = products.back();
    //p->getTransformation()->setMatrix(getTransformation()->getMatrix());
    products.pop_back();
    p->getTransformation()->show();
    setMetaData("Nb: " + toString(products.size()));
    //p->setMetaData("ID: " + toString(p->getID()));
    return p;
}
```

###Ablauf:
Zu Beginn eines Auftrags werden Anfangs- und Endlager-Kapazität auf Auftragsgröße gesetzt, und die Logistiktransportsimulation läuft an

Dann wird durchgeloopt:
* Sobald ein Rohling in erstem Container `VR.containers[1]` vorhanden und grade kein Rohling in Bearbeitung:
  LogisticControl nimmt Rohling aus Container und ruft `move` beim VR.robotController auf und übergibt Rohling und Positionen
* Roboter bewegt Rohling in Fräse, ruft Callback `moveDone` auf
* LogisticsControl ruft `VR.fraeseController.startFraese` auf. Übergeben werden der Rohling und ein int (im Moment 0 oder 1) für das Felgenmodell.
* Die Fräse tut Dinge und erstellt am Ende das fertige Felgen-Objekt.
* Die Fräse ruft `VR.logicsticController.fraeseDone` auf und übergibt die fertige Felge
* Analog zu vorhin bewegt der Roboter die Felge aufs Band
* Roboter fertig --> LogisticControl kümmert sich darum, dass die Felge abtransportiert wird.
