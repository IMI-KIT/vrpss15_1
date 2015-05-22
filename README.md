# vrpss15_1
Virtual reality practical course summer 2015 group 1

Achtet darauf, immer die aktuelle polyVR-Version zu haben, der Code in unserer Fabrik benutzt Funktionen, die dafür erst hinzugefügt wurden.


container.get() ruft intern  self->obj->pop() auf, dh. das Objekt ist danach nicht mehr im Container. Der Container ist intern als vector organisiert, bei dem Objekte am Ende hinzugefügt und weggenommen werden (push_back und pop_back) 
--> Stack, keine Queue!!

FProduct* FContainer::pop() {
    FProduct* p = products.back();
    //p->getTransformation()->setMatrix(getTransformation()->getMatrix());
    products.pop_back();
    p->getTransformation()->show();
    setMetaData("Nb: " + toString(products.size()));
    //p->setMetaData("ID: " + toString(p->getID()));
    return p;
}

