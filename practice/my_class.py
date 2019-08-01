class Planet:
    shape='round'  #定義在這裡的叫做class attribute
                   #也就是所有planet的class都有共同這個特性  (因為星球都是圓的阿)

    def __init__(self,name,radius,gravity):
        self.name=name
        self.radius=radius
        self.gravity=gravity


    def show_gravity(self):
        print('This planet has gravity', gravity)
