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

###Auftragssteuerung
Die Auftragssteuerung geht über die Webseite. Im Moment hat es 4 Knöpfe: Toggle Modell, +, -, Start.
Darüber kann man den Typ und die Anzahl der Felgen verändern. Um den Auftrag tatsächlich abzusenden, klicke auf Start.

Der Auftrag wird dann als Liste [Anzahl, Typ] in eine Warteschlange geschoben. Falls kein Auftrag mehr läuft, wird der vorderste Auftrag aus der Schlange gestartet. Die Anzeige wird dann für den nächsten Auftrag wieder auf 1 Felge vom Typ 0 zurückgesetzt.

Wenn das Projekt gestartet wird, ist die Auftragswarteschlange erst mal leer. Der gewünschte Auftrag kann über die Webseite zusammengeklickt werden.

###Ablauf von einem Auftrag:
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


###Die Felgen
...werden in initScene erstellt. Wenn später die (seeeehr) simple Geomtrie ersetzt wird, sollte `VR.felge0` und `VR.felge1` weiterhin vom Typ Geometry sein, damit die Transportsimulation die Geometrie in Produkte umwandeln und transportieren kann.


