{"filter":false,"title":"models.py","tooltip":"/crud/models.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":32,"column":0},"end":{"row":36,"column":41},"action":"remove","lines":["    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)","    items = models.ManyToManyField(OrderItem)","    start_date = models.DateTimeField(auto_now_add=True)","    ordered = models.BooleanField(default=False)","    ordered_date = models.DateTimeField()"],"id":209},{"start":{"row":31,"column":26},"end":{"row":32,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":31,"column":26},"end":{"row":32,"column":4},"action":"remove","lines":["","    "],"id":210}],[{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["d"],"id":211},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"insert","lines":["e"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"insert","lines":["f"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["a"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["u"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["l"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":["="],"id":212},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"insert","lines":["0"]}],[{"start":{"row":6,"column":30},"end":{"row":6,"column":39},"action":"remove","lines":["default=0"],"id":213},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["b"]},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"insert","lines":["u"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"insert","lines":["l"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["l"]}],[{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"remove","lines":["l"],"id":214},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"remove","lines":["l"]},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"remove","lines":["u"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"remove","lines":["b"]}],[{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["n"],"id":215},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"insert","lines":["u"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"insert","lines":["l"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["l"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["="]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["T"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["r"]},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":["u"]},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"insert","lines":["e"]}],[{"start":{"row":27,"column":0},"end":{"row":28,"column":0},"action":"remove","lines":["    item = models.ForeignKey(Item, on_delete=models.CASCADE)",""],"id":216}],[{"start":{"row":26,"column":0},"end":{"row":32,"column":26},"action":"remove","lines":["class OrderItem(models.Model):","    def __str__(self):","        return self.name        ","","class Order(models.Model):","    def __str__(self):","        return self.name  "],"id":217}],[{"start":{"row":26,"column":0},"end":{"row":26,"column":1},"action":"insert","lines":["c"],"id":218},{"start":{"row":26,"column":1},"end":{"row":26,"column":2},"action":"insert","lines":["l"]},{"start":{"row":26,"column":2},"end":{"row":26,"column":3},"action":"insert","lines":["a"]},{"start":{"row":26,"column":3},"end":{"row":26,"column":4},"action":"insert","lines":["s"]},{"start":{"row":26,"column":4},"end":{"row":26,"column":5},"action":"insert","lines":["s"]}],[{"start":{"row":26,"column":5},"end":{"row":26,"column":6},"action":"insert","lines":[" "],"id":219},{"start":{"row":26,"column":6},"end":{"row":26,"column":7},"action":"insert","lines":["O"]},{"start":{"row":26,"column":7},"end":{"row":26,"column":8},"action":"insert","lines":["r"]},{"start":{"row":26,"column":8},"end":{"row":26,"column":9},"action":"insert","lines":["d"]},{"start":{"row":26,"column":9},"end":{"row":26,"column":10},"action":"insert","lines":["e"]},{"start":{"row":26,"column":10},"end":{"row":26,"column":11},"action":"insert","lines":["r"]},{"start":{"row":26,"column":11},"end":{"row":26,"column":12},"action":"insert","lines":["I"]},{"start":{"row":26,"column":12},"end":{"row":26,"column":13},"action":"insert","lines":["t"]},{"start":{"row":26,"column":13},"end":{"row":26,"column":14},"action":"insert","lines":["e"]},{"start":{"row":26,"column":14},"end":{"row":26,"column":15},"action":"insert","lines":["m"]}],[{"start":{"row":26,"column":15},"end":{"row":26,"column":17},"action":"insert","lines":["()"],"id":220}],[{"start":{"row":26,"column":16},"end":{"row":26,"column":17},"action":"insert","lines":["m"],"id":221},{"start":{"row":26,"column":17},"end":{"row":26,"column":18},"action":"insert","lines":["o"]},{"start":{"row":26,"column":18},"end":{"row":26,"column":19},"action":"insert","lines":["d"]},{"start":{"row":26,"column":19},"end":{"row":26,"column":20},"action":"insert","lines":["e"]},{"start":{"row":26,"column":20},"end":{"row":26,"column":21},"action":"insert","lines":["l"]},{"start":{"row":26,"column":21},"end":{"row":26,"column":22},"action":"insert","lines":["s"]},{"start":{"row":26,"column":22},"end":{"row":26,"column":23},"action":"insert","lines":["."]},{"start":{"row":26,"column":23},"end":{"row":26,"column":24},"action":"insert","lines":["M"]},{"start":{"row":26,"column":24},"end":{"row":26,"column":25},"action":"insert","lines":["o"]}],[{"start":{"row":26,"column":25},"end":{"row":26,"column":26},"action":"insert","lines":["d"],"id":222},{"start":{"row":26,"column":26},"end":{"row":26,"column":27},"action":"insert","lines":["e"]},{"start":{"row":26,"column":27},"end":{"row":26,"column":28},"action":"insert","lines":["l"]}],[{"start":{"row":26,"column":29},"end":{"row":26,"column":30},"action":"insert","lines":[":"],"id":223}],[{"start":{"row":26,"column":30},"end":{"row":26,"column":36},"action":"remove","lines":["      "],"id":224},{"start":{"row":26,"column":30},"end":{"row":27,"column":0},"action":"insert","lines":["",""]},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":27,"column":4},"end":{"row":29,"column":0},"action":"insert","lines":["def __str__(self):","        return self.name        ",""],"id":225}],[{"start":{"row":30,"column":0},"end":{"row":33,"column":0},"action":"insert","lines":["class OrderItem(models.Model):","    def __str__(self):","        return self.name        ",""],"id":226}],[{"start":{"row":30,"column":11},"end":{"row":30,"column":15},"action":"remove","lines":["Item"],"id":227}],[{"start":{"row":30,"column":26},"end":{"row":31,"column":0},"action":"insert","lines":["",""],"id":228},{"start":{"row":31,"column":0},"end":{"row":31,"column":4},"action":"insert","lines":["    "]},{"start":{"row":31,"column":4},"end":{"row":31,"column":5},"action":"insert","lines":["u"]},{"start":{"row":31,"column":5},"end":{"row":31,"column":6},"action":"insert","lines":["s"]},{"start":{"row":31,"column":6},"end":{"row":31,"column":7},"action":"insert","lines":["e"]},{"start":{"row":31,"column":7},"end":{"row":31,"column":8},"action":"insert","lines":["r"]}],[{"start":{"row":31,"column":8},"end":{"row":31,"column":9},"action":"insert","lines":[" "],"id":229},{"start":{"row":31,"column":9},"end":{"row":31,"column":10},"action":"insert","lines":["="]}],[{"start":{"row":31,"column":10},"end":{"row":31,"column":11},"action":"insert","lines":[" "],"id":230},{"start":{"row":31,"column":11},"end":{"row":31,"column":12},"action":"insert","lines":["m"]},{"start":{"row":31,"column":12},"end":{"row":31,"column":13},"action":"insert","lines":["o"]},{"start":{"row":31,"column":13},"end":{"row":31,"column":14},"action":"insert","lines":["d"]},{"start":{"row":31,"column":14},"end":{"row":31,"column":15},"action":"insert","lines":["e"]},{"start":{"row":31,"column":15},"end":{"row":31,"column":16},"action":"insert","lines":["l"]},{"start":{"row":31,"column":16},"end":{"row":31,"column":17},"action":"insert","lines":["s"]}],[{"start":{"row":31,"column":17},"end":{"row":31,"column":18},"action":"insert","lines":["."],"id":231},{"start":{"row":31,"column":18},"end":{"row":31,"column":19},"action":"insert","lines":["F"]}],[{"start":{"row":31,"column":19},"end":{"row":31,"column":20},"action":"insert","lines":["o"],"id":232}],[{"start":{"row":31,"column":18},"end":{"row":31,"column":20},"action":"remove","lines":["Fo"],"id":233},{"start":{"row":31,"column":18},"end":{"row":31,"column":28},"action":"insert","lines":["ForeignKey"]}],[{"start":{"row":31,"column":28},"end":{"row":31,"column":30},"action":"insert","lines":["()"],"id":234}],[{"start":{"row":31,"column":30},"end":{"row":31,"column":31},"action":"insert","lines":["s"],"id":235},{"start":{"row":31,"column":31},"end":{"row":31,"column":32},"action":"insert","lines":["e"]},{"start":{"row":31,"column":32},"end":{"row":31,"column":33},"action":"insert","lines":["t"]}],[{"start":{"row":31,"column":32},"end":{"row":31,"column":33},"action":"remove","lines":["t"],"id":236},{"start":{"row":31,"column":31},"end":{"row":31,"column":32},"action":"remove","lines":["e"]},{"start":{"row":31,"column":30},"end":{"row":31,"column":31},"action":"remove","lines":["s"]}],[{"start":{"row":31,"column":29},"end":{"row":31,"column":30},"action":"insert","lines":["s"],"id":237},{"start":{"row":31,"column":30},"end":{"row":31,"column":31},"action":"insert","lines":["e"]},{"start":{"row":31,"column":31},"end":{"row":31,"column":32},"action":"insert","lines":["t"]},{"start":{"row":31,"column":32},"end":{"row":31,"column":33},"action":"insert","lines":["t"]},{"start":{"row":31,"column":33},"end":{"row":31,"column":34},"action":"insert","lines":["i"]},{"start":{"row":31,"column":34},"end":{"row":31,"column":35},"action":"insert","lines":["n"]},{"start":{"row":31,"column":35},"end":{"row":31,"column":36},"action":"insert","lines":["g"]},{"start":{"row":31,"column":36},"end":{"row":31,"column":37},"action":"insert","lines":["s"]},{"start":{"row":31,"column":37},"end":{"row":31,"column":38},"action":"insert","lines":["."]}],[{"start":{"row":31,"column":38},"end":{"row":31,"column":39},"action":"insert","lines":["A"],"id":238},{"start":{"row":31,"column":39},"end":{"row":31,"column":40},"action":"insert","lines":["Y"]}],[{"start":{"row":31,"column":39},"end":{"row":31,"column":40},"action":"remove","lines":["Y"],"id":239}],[{"start":{"row":31,"column":39},"end":{"row":31,"column":40},"action":"insert","lines":["U"],"id":240},{"start":{"row":31,"column":40},"end":{"row":31,"column":41},"action":"insert","lines":["T"]},{"start":{"row":31,"column":41},"end":{"row":31,"column":42},"action":"insert","lines":["H"]},{"start":{"row":31,"column":42},"end":{"row":31,"column":43},"action":"insert","lines":["_"]},{"start":{"row":31,"column":43},"end":{"row":31,"column":44},"action":"insert","lines":["U"]},{"start":{"row":31,"column":44},"end":{"row":31,"column":45},"action":"insert","lines":["S"]},{"start":{"row":31,"column":45},"end":{"row":31,"column":46},"action":"insert","lines":["E"]},{"start":{"row":31,"column":46},"end":{"row":31,"column":47},"action":"insert","lines":["R"]},{"start":{"row":31,"column":47},"end":{"row":31,"column":48},"action":"insert","lines":["_"]},{"start":{"row":31,"column":48},"end":{"row":31,"column":49},"action":"insert","lines":["M"]},{"start":{"row":31,"column":49},"end":{"row":31,"column":50},"action":"insert","lines":["O"]}],[{"start":{"row":31,"column":50},"end":{"row":31,"column":51},"action":"insert","lines":["D"],"id":241},{"start":{"row":31,"column":51},"end":{"row":31,"column":52},"action":"insert","lines":["E"]},{"start":{"row":31,"column":52},"end":{"row":31,"column":53},"action":"insert","lines":["L"]},{"start":{"row":31,"column":53},"end":{"row":31,"column":54},"action":"insert","lines":[","]}],[{"start":{"row":31,"column":54},"end":{"row":31,"column":55},"action":"insert","lines":[" "],"id":242}],[{"start":{"row":31,"column":55},"end":{"row":31,"column":79},"action":"insert","lines":["on_delete=models.CASCADE"],"id":243}],[{"start":{"row":31,"column":54},"end":{"row":31,"column":55},"action":"remove","lines":[" "],"id":244}],[{"start":{"row":31,"column":54},"end":{"row":31,"column":55},"action":"insert","lines":[" "],"id":245}],[{"start":{"row":31,"column":80},"end":{"row":32,"column":0},"action":"insert","lines":["",""],"id":246},{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":32,"column":4},"end":{"row":32,"column":5},"action":"insert","lines":["i"],"id":247},{"start":{"row":32,"column":5},"end":{"row":32,"column":6},"action":"insert","lines":["t"]},{"start":{"row":32,"column":6},"end":{"row":32,"column":7},"action":"insert","lines":["e"]},{"start":{"row":32,"column":7},"end":{"row":32,"column":8},"action":"insert","lines":["m"]},{"start":{"row":32,"column":8},"end":{"row":32,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":32,"column":9},"end":{"row":32,"column":10},"action":"insert","lines":[" "],"id":248},{"start":{"row":32,"column":10},"end":{"row":32,"column":11},"action":"insert","lines":["="]}],[{"start":{"row":32,"column":11},"end":{"row":32,"column":12},"action":"insert","lines":[" "],"id":249},{"start":{"row":32,"column":12},"end":{"row":32,"column":13},"action":"insert","lines":["m"]},{"start":{"row":32,"column":13},"end":{"row":32,"column":14},"action":"insert","lines":["o"]},{"start":{"row":32,"column":14},"end":{"row":32,"column":15},"action":"insert","lines":["d"]},{"start":{"row":32,"column":15},"end":{"row":32,"column":16},"action":"insert","lines":["e"]},{"start":{"row":32,"column":16},"end":{"row":32,"column":17},"action":"insert","lines":["l"]},{"start":{"row":32,"column":17},"end":{"row":32,"column":18},"action":"insert","lines":["s"]}],[{"start":{"row":32,"column":18},"end":{"row":32,"column":19},"action":"insert","lines":["."],"id":250},{"start":{"row":32,"column":19},"end":{"row":32,"column":20},"action":"insert","lines":["M"]},{"start":{"row":32,"column":20},"end":{"row":32,"column":21},"action":"insert","lines":["a"]},{"start":{"row":32,"column":21},"end":{"row":32,"column":22},"action":"insert","lines":["n"]},{"start":{"row":32,"column":22},"end":{"row":32,"column":23},"action":"insert","lines":["y"]}],[{"start":{"row":32,"column":19},"end":{"row":32,"column":23},"action":"remove","lines":["Many"],"id":251},{"start":{"row":32,"column":19},"end":{"row":32,"column":34},"action":"insert","lines":["ManyToManyField"]}],[{"start":{"row":32,"column":34},"end":{"row":32,"column":36},"action":"insert","lines":["()"],"id":252}],[{"start":{"row":32,"column":35},"end":{"row":32,"column":36},"action":"insert","lines":["O"],"id":253},{"start":{"row":32,"column":36},"end":{"row":32,"column":37},"action":"insert","lines":["r"]},{"start":{"row":32,"column":37},"end":{"row":32,"column":38},"action":"insert","lines":["d"]},{"start":{"row":32,"column":38},"end":{"row":32,"column":39},"action":"insert","lines":["e"]},{"start":{"row":32,"column":39},"end":{"row":32,"column":40},"action":"insert","lines":["r"]},{"start":{"row":32,"column":40},"end":{"row":32,"column":41},"action":"insert","lines":["I"]},{"start":{"row":32,"column":41},"end":{"row":32,"column":42},"action":"insert","lines":["t"]},{"start":{"row":32,"column":42},"end":{"row":32,"column":43},"action":"insert","lines":["e"]},{"start":{"row":32,"column":43},"end":{"row":32,"column":44},"action":"insert","lines":["m"]}],[{"start":{"row":32,"column":45},"end":{"row":33,"column":0},"action":"insert","lines":["",""],"id":254},{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"insert","lines":["    "]},{"start":{"row":33,"column":4},"end":{"row":33,"column":5},"action":"insert","lines":["s"]},{"start":{"row":33,"column":5},"end":{"row":33,"column":6},"action":"insert","lines":["t"]},{"start":{"row":33,"column":6},"end":{"row":33,"column":7},"action":"insert","lines":["a"]},{"start":{"row":33,"column":7},"end":{"row":33,"column":8},"action":"insert","lines":["r"]}],[{"start":{"row":33,"column":8},"end":{"row":33,"column":9},"action":"insert","lines":["t"],"id":255},{"start":{"row":33,"column":9},"end":{"row":33,"column":10},"action":"insert","lines":["-"]},{"start":{"row":33,"column":10},"end":{"row":33,"column":11},"action":"insert","lines":["d"]},{"start":{"row":33,"column":11},"end":{"row":33,"column":12},"action":"insert","lines":["a"]},{"start":{"row":33,"column":12},"end":{"row":33,"column":13},"action":"insert","lines":["t"]},{"start":{"row":33,"column":13},"end":{"row":33,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":33,"column":13},"end":{"row":33,"column":14},"action":"remove","lines":["e"],"id":256},{"start":{"row":33,"column":12},"end":{"row":33,"column":13},"action":"remove","lines":["t"]},{"start":{"row":33,"column":11},"end":{"row":33,"column":12},"action":"remove","lines":["a"]},{"start":{"row":33,"column":10},"end":{"row":33,"column":11},"action":"remove","lines":["d"]},{"start":{"row":33,"column":9},"end":{"row":33,"column":10},"action":"remove","lines":["-"]}],[{"start":{"row":33,"column":9},"end":{"row":33,"column":10},"action":"insert","lines":["_"],"id":257},{"start":{"row":33,"column":10},"end":{"row":33,"column":11},"action":"insert","lines":["d"]},{"start":{"row":33,"column":11},"end":{"row":33,"column":12},"action":"insert","lines":["a"]},{"start":{"row":33,"column":12},"end":{"row":33,"column":13},"action":"insert","lines":["t"]},{"start":{"row":33,"column":13},"end":{"row":33,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":33,"column":14},"end":{"row":33,"column":15},"action":"insert","lines":[" "],"id":258},{"start":{"row":33,"column":15},"end":{"row":33,"column":16},"action":"insert","lines":["="]}],[{"start":{"row":33,"column":16},"end":{"row":33,"column":17},"action":"insert","lines":[" "],"id":259},{"start":{"row":33,"column":17},"end":{"row":33,"column":18},"action":"insert","lines":["m"]},{"start":{"row":33,"column":18},"end":{"row":33,"column":19},"action":"insert","lines":["o"]},{"start":{"row":33,"column":19},"end":{"row":33,"column":20},"action":"insert","lines":["d"]},{"start":{"row":33,"column":20},"end":{"row":33,"column":21},"action":"insert","lines":["e"]},{"start":{"row":33,"column":21},"end":{"row":33,"column":22},"action":"insert","lines":["l"]},{"start":{"row":33,"column":22},"end":{"row":33,"column":23},"action":"insert","lines":["s"]},{"start":{"row":33,"column":23},"end":{"row":33,"column":24},"action":"insert","lines":["."]},{"start":{"row":33,"column":24},"end":{"row":33,"column":25},"action":"insert","lines":["D"]},{"start":{"row":33,"column":25},"end":{"row":33,"column":26},"action":"insert","lines":["a"]},{"start":{"row":33,"column":26},"end":{"row":33,"column":27},"action":"insert","lines":["t"]},{"start":{"row":33,"column":27},"end":{"row":33,"column":28},"action":"insert","lines":["e"]}],[{"start":{"row":33,"column":24},"end":{"row":33,"column":28},"action":"remove","lines":["Date"],"id":260},{"start":{"row":33,"column":24},"end":{"row":33,"column":37},"action":"insert","lines":["DateTimeField"]}],[{"start":{"row":33,"column":37},"end":{"row":33,"column":39},"action":"insert","lines":["()"],"id":261}],[{"start":{"row":33,"column":38},"end":{"row":33,"column":39},"action":"insert","lines":["a"],"id":262},{"start":{"row":33,"column":39},"end":{"row":33,"column":40},"action":"insert","lines":["u"]},{"start":{"row":33,"column":40},"end":{"row":33,"column":41},"action":"insert","lines":["t"]},{"start":{"row":33,"column":41},"end":{"row":33,"column":42},"action":"insert","lines":["o"]}],[{"start":{"row":33,"column":38},"end":{"row":33,"column":42},"action":"remove","lines":["auto"],"id":263},{"start":{"row":33,"column":38},"end":{"row":33,"column":50},"action":"insert","lines":["auto_now_add"]}],[{"start":{"row":33,"column":50},"end":{"row":33,"column":51},"action":"insert","lines":["="],"id":264},{"start":{"row":33,"column":51},"end":{"row":33,"column":52},"action":"insert","lines":["T"]},{"start":{"row":33,"column":52},"end":{"row":33,"column":53},"action":"insert","lines":["r"]},{"start":{"row":33,"column":53},"end":{"row":33,"column":54},"action":"insert","lines":["u"]},{"start":{"row":33,"column":54},"end":{"row":33,"column":55},"action":"insert","lines":["e"]}],[{"start":{"row":33,"column":56},"end":{"row":34,"column":0},"action":"insert","lines":["",""],"id":265},{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":34,"column":4},"end":{"row":34,"column":5},"action":"insert","lines":["o"],"id":266},{"start":{"row":34,"column":5},"end":{"row":34,"column":6},"action":"insert","lines":["r"]},{"start":{"row":34,"column":6},"end":{"row":34,"column":7},"action":"insert","lines":["e"]}],[{"start":{"row":34,"column":6},"end":{"row":34,"column":7},"action":"remove","lines":["e"],"id":267}],[{"start":{"row":34,"column":6},"end":{"row":34,"column":7},"action":"insert","lines":["d"],"id":268},{"start":{"row":34,"column":7},"end":{"row":34,"column":8},"action":"insert","lines":["e"]},{"start":{"row":34,"column":8},"end":{"row":34,"column":9},"action":"insert","lines":["r"]},{"start":{"row":34,"column":9},"end":{"row":34,"column":10},"action":"insert","lines":["e"]},{"start":{"row":34,"column":10},"end":{"row":34,"column":11},"action":"insert","lines":["d"]},{"start":{"row":34,"column":11},"end":{"row":34,"column":12},"action":"insert","lines":["_"]},{"start":{"row":34,"column":12},"end":{"row":34,"column":13},"action":"insert","lines":["d"]},{"start":{"row":34,"column":13},"end":{"row":34,"column":14},"action":"insert","lines":["a"]},{"start":{"row":34,"column":14},"end":{"row":34,"column":15},"action":"insert","lines":["t"]},{"start":{"row":34,"column":15},"end":{"row":34,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":34,"column":16},"end":{"row":34,"column":17},"action":"insert","lines":[" "],"id":269},{"start":{"row":34,"column":17},"end":{"row":34,"column":18},"action":"insert","lines":["="]}],[{"start":{"row":34,"column":18},"end":{"row":34,"column":19},"action":"insert","lines":[" "],"id":270},{"start":{"row":34,"column":19},"end":{"row":34,"column":20},"action":"insert","lines":["m"]}],[{"start":{"row":34,"column":20},"end":{"row":34,"column":21},"action":"insert","lines":["o"],"id":271},{"start":{"row":34,"column":21},"end":{"row":34,"column":22},"action":"insert","lines":["d"]},{"start":{"row":34,"column":22},"end":{"row":34,"column":23},"action":"insert","lines":["e"]},{"start":{"row":34,"column":23},"end":{"row":34,"column":24},"action":"insert","lines":["l"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"insert","lines":["s"]},{"start":{"row":34,"column":25},"end":{"row":34,"column":26},"action":"insert","lines":["."]},{"start":{"row":34,"column":26},"end":{"row":34,"column":27},"action":"insert","lines":["D"]},{"start":{"row":34,"column":27},"end":{"row":34,"column":28},"action":"insert","lines":["a"]},{"start":{"row":34,"column":28},"end":{"row":34,"column":29},"action":"insert","lines":["t"]},{"start":{"row":34,"column":29},"end":{"row":34,"column":30},"action":"insert","lines":["e"]},{"start":{"row":34,"column":30},"end":{"row":34,"column":31},"action":"insert","lines":["I"]}],[{"start":{"row":34,"column":31},"end":{"row":34,"column":32},"action":"insert","lines":["m"],"id":272},{"start":{"row":34,"column":32},"end":{"row":34,"column":33},"action":"insert","lines":["e"]}],[{"start":{"row":34,"column":32},"end":{"row":34,"column":33},"action":"remove","lines":["e"],"id":273},{"start":{"row":34,"column":31},"end":{"row":34,"column":32},"action":"remove","lines":["m"]},{"start":{"row":34,"column":30},"end":{"row":34,"column":31},"action":"remove","lines":["I"]},{"start":{"row":34,"column":29},"end":{"row":34,"column":30},"action":"remove","lines":["e"]},{"start":{"row":34,"column":28},"end":{"row":34,"column":29},"action":"remove","lines":["t"]},{"start":{"row":34,"column":27},"end":{"row":34,"column":28},"action":"remove","lines":["a"]},{"start":{"row":34,"column":26},"end":{"row":34,"column":27},"action":"remove","lines":["D"]}],[{"start":{"row":34,"column":26},"end":{"row":34,"column":27},"action":"insert","lines":["D"],"id":274},{"start":{"row":34,"column":27},"end":{"row":34,"column":28},"action":"insert","lines":["a"]}],[{"start":{"row":34,"column":26},"end":{"row":34,"column":28},"action":"remove","lines":["Da"],"id":275},{"start":{"row":34,"column":26},"end":{"row":34,"column":39},"action":"insert","lines":["DateTimeField"]}],[{"start":{"row":34,"column":39},"end":{"row":34,"column":41},"action":"insert","lines":["()"],"id":276}],[{"start":{"row":34,"column":41},"end":{"row":35,"column":0},"action":"insert","lines":["",""],"id":277},{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"insert","lines":["    "]},{"start":{"row":35,"column":4},"end":{"row":35,"column":5},"action":"insert","lines":["o"]},{"start":{"row":35,"column":5},"end":{"row":35,"column":6},"action":"insert","lines":["r"]}],[{"start":{"row":35,"column":6},"end":{"row":35,"column":7},"action":"insert","lines":["d"],"id":278},{"start":{"row":35,"column":7},"end":{"row":35,"column":8},"action":"insert","lines":["e"]},{"start":{"row":35,"column":8},"end":{"row":35,"column":9},"action":"insert","lines":["r"]},{"start":{"row":35,"column":9},"end":{"row":35,"column":10},"action":"insert","lines":["e"]},{"start":{"row":35,"column":10},"end":{"row":35,"column":11},"action":"insert","lines":["d"]}],[{"start":{"row":35,"column":11},"end":{"row":35,"column":12},"action":"insert","lines":[" "],"id":279},{"start":{"row":35,"column":12},"end":{"row":35,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":35,"column":13},"end":{"row":35,"column":14},"action":"insert","lines":[" "],"id":280},{"start":{"row":35,"column":14},"end":{"row":35,"column":15},"action":"insert","lines":["m"]},{"start":{"row":35,"column":15},"end":{"row":35,"column":16},"action":"insert","lines":["o"]},{"start":{"row":35,"column":16},"end":{"row":35,"column":17},"action":"insert","lines":["o"]}],[{"start":{"row":35,"column":16},"end":{"row":35,"column":17},"action":"remove","lines":["o"],"id":281}],[{"start":{"row":35,"column":16},"end":{"row":35,"column":17},"action":"insert","lines":["d"],"id":282},{"start":{"row":35,"column":17},"end":{"row":35,"column":18},"action":"insert","lines":["e"]},{"start":{"row":35,"column":18},"end":{"row":35,"column":19},"action":"insert","lines":["l"]},{"start":{"row":35,"column":19},"end":{"row":35,"column":20},"action":"insert","lines":["s"]},{"start":{"row":35,"column":20},"end":{"row":35,"column":21},"action":"insert","lines":["."]},{"start":{"row":35,"column":21},"end":{"row":35,"column":22},"action":"insert","lines":["b"]}],[{"start":{"row":35,"column":21},"end":{"row":35,"column":22},"action":"remove","lines":["b"],"id":283}],[{"start":{"row":35,"column":21},"end":{"row":35,"column":22},"action":"insert","lines":["B"],"id":284},{"start":{"row":35,"column":22},"end":{"row":35,"column":23},"action":"insert","lines":["o"]}],[{"start":{"row":35,"column":21},"end":{"row":35,"column":23},"action":"remove","lines":["Bo"],"id":285},{"start":{"row":35,"column":21},"end":{"row":35,"column":33},"action":"insert","lines":["BooleanField"]}],[{"start":{"row":35,"column":33},"end":{"row":35,"column":35},"action":"insert","lines":["()"],"id":286}],[{"start":{"row":35,"column":34},"end":{"row":35,"column":35},"action":"insert","lines":["d"],"id":287},{"start":{"row":35,"column":35},"end":{"row":35,"column":36},"action":"insert","lines":["e"]},{"start":{"row":35,"column":36},"end":{"row":35,"column":37},"action":"insert","lines":["f"]},{"start":{"row":35,"column":37},"end":{"row":35,"column":38},"action":"insert","lines":["a"]},{"start":{"row":35,"column":38},"end":{"row":35,"column":39},"action":"insert","lines":["i"]}],[{"start":{"row":35,"column":38},"end":{"row":35,"column":39},"action":"remove","lines":["i"],"id":288}],[{"start":{"row":35,"column":38},"end":{"row":35,"column":39},"action":"insert","lines":["u"],"id":289},{"start":{"row":35,"column":39},"end":{"row":35,"column":40},"action":"insert","lines":["l"]},{"start":{"row":35,"column":40},"end":{"row":35,"column":41},"action":"insert","lines":["t"]},{"start":{"row":35,"column":41},"end":{"row":35,"column":42},"action":"insert","lines":["-"]}],[{"start":{"row":35,"column":41},"end":{"row":35,"column":42},"action":"remove","lines":["-"],"id":290}],[{"start":{"row":35,"column":41},"end":{"row":35,"column":42},"action":"insert","lines":["="],"id":291},{"start":{"row":35,"column":42},"end":{"row":35,"column":43},"action":"insert","lines":["F"]},{"start":{"row":35,"column":43},"end":{"row":35,"column":44},"action":"insert","lines":["l"]}],[{"start":{"row":35,"column":43},"end":{"row":35,"column":44},"action":"remove","lines":["l"],"id":292}],[{"start":{"row":35,"column":43},"end":{"row":35,"column":44},"action":"insert","lines":["a"],"id":293},{"start":{"row":35,"column":44},"end":{"row":35,"column":45},"action":"insert","lines":["l"]},{"start":{"row":35,"column":45},"end":{"row":35,"column":46},"action":"insert","lines":["s"]},{"start":{"row":35,"column":46},"end":{"row":35,"column":47},"action":"insert","lines":["e"]}],[{"start":{"row":26,"column":30},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":294},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":5},"action":"insert","lines":["i"],"id":295},{"start":{"row":27,"column":5},"end":{"row":27,"column":6},"action":"insert","lines":["t"]},{"start":{"row":27,"column":6},"end":{"row":27,"column":7},"action":"insert","lines":["e"]},{"start":{"row":27,"column":7},"end":{"row":27,"column":8},"action":"insert","lines":["m"]}],[{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":[" "],"id":296},{"start":{"row":27,"column":9},"end":{"row":27,"column":10},"action":"insert","lines":["="]}],[{"start":{"row":27,"column":10},"end":{"row":27,"column":11},"action":"insert","lines":[" "],"id":297},{"start":{"row":27,"column":11},"end":{"row":27,"column":12},"action":"insert","lines":["m"]},{"start":{"row":27,"column":12},"end":{"row":27,"column":13},"action":"insert","lines":["o"]},{"start":{"row":27,"column":13},"end":{"row":27,"column":14},"action":"insert","lines":["d"]},{"start":{"row":27,"column":14},"end":{"row":27,"column":15},"action":"insert","lines":["e"]},{"start":{"row":27,"column":15},"end":{"row":27,"column":16},"action":"insert","lines":["l"]},{"start":{"row":27,"column":16},"end":{"row":27,"column":17},"action":"insert","lines":["."]},{"start":{"row":27,"column":17},"end":{"row":27,"column":18},"action":"insert","lines":["F"]}],[{"start":{"row":27,"column":17},"end":{"row":27,"column":18},"action":"remove","lines":["F"],"id":298},{"start":{"row":27,"column":17},"end":{"row":27,"column":27},"action":"insert","lines":["ForeignKey"]}],[{"start":{"row":27,"column":27},"end":{"row":27,"column":29},"action":"insert","lines":["()"],"id":299}],[{"start":{"row":27,"column":28},"end":{"row":27,"column":29},"action":"insert","lines":["I"],"id":300},{"start":{"row":27,"column":29},"end":{"row":27,"column":30},"action":"insert","lines":["t"]},{"start":{"row":27,"column":30},"end":{"row":27,"column":31},"action":"insert","lines":["e"]},{"start":{"row":27,"column":31},"end":{"row":27,"column":32},"action":"insert","lines":["m"]},{"start":{"row":27,"column":32},"end":{"row":27,"column":33},"action":"insert","lines":[","]}],[{"start":{"row":27,"column":33},"end":{"row":27,"column":34},"action":"insert","lines":[" "],"id":301},{"start":{"row":27,"column":34},"end":{"row":27,"column":35},"action":"insert","lines":["o"]},{"start":{"row":27,"column":35},"end":{"row":27,"column":36},"action":"insert","lines":["n"]}],[{"start":{"row":27,"column":34},"end":{"row":27,"column":36},"action":"remove","lines":["on"],"id":302},{"start":{"row":27,"column":34},"end":{"row":27,"column":43},"action":"insert","lines":["on_delete"]}],[{"start":{"row":27,"column":43},"end":{"row":27,"column":44},"action":"insert","lines":["="],"id":303},{"start":{"row":27,"column":44},"end":{"row":27,"column":45},"action":"insert","lines":["m"]},{"start":{"row":27,"column":45},"end":{"row":27,"column":46},"action":"insert","lines":["o"]},{"start":{"row":27,"column":46},"end":{"row":27,"column":47},"action":"insert","lines":["d"]},{"start":{"row":27,"column":47},"end":{"row":27,"column":48},"action":"insert","lines":["e"]},{"start":{"row":27,"column":48},"end":{"row":27,"column":49},"action":"insert","lines":["l"]},{"start":{"row":27,"column":49},"end":{"row":27,"column":50},"action":"insert","lines":["s"]}],[{"start":{"row":27,"column":50},"end":{"row":27,"column":51},"action":"insert","lines":[","],"id":304}],[{"start":{"row":27,"column":50},"end":{"row":27,"column":51},"action":"remove","lines":[","],"id":305}],[{"start":{"row":27,"column":34},"end":{"row":27,"column":50},"action":"remove","lines":["on_delete=models"],"id":306},{"start":{"row":27,"column":34},"end":{"row":27,"column":58},"action":"insert","lines":["on_delete=models.CASCADE"]}],[{"start":{"row":27,"column":16},"end":{"row":27,"column":17},"action":"insert","lines":["s"],"id":307}],[{"start":{"row":27,"column":34},"end":{"row":27,"column":35},"action":"insert","lines":[" "],"id":308},{"start":{"row":27,"column":35},"end":{"row":27,"column":36},"action":"insert","lines":["n"]},{"start":{"row":27,"column":36},"end":{"row":27,"column":37},"action":"insert","lines":["u"]},{"start":{"row":27,"column":37},"end":{"row":27,"column":38},"action":"insert","lines":["l"]},{"start":{"row":27,"column":38},"end":{"row":27,"column":39},"action":"insert","lines":["l"]},{"start":{"row":27,"column":39},"end":{"row":27,"column":40},"action":"insert","lines":["="]},{"start":{"row":27,"column":40},"end":{"row":27,"column":41},"action":"insert","lines":["T"]},{"start":{"row":27,"column":41},"end":{"row":27,"column":42},"action":"insert","lines":["r"]},{"start":{"row":27,"column":42},"end":{"row":27,"column":43},"action":"insert","lines":["u"]},{"start":{"row":27,"column":43},"end":{"row":27,"column":44},"action":"insert","lines":["e"]}],[{"start":{"row":27,"column":44},"end":{"row":27,"column":45},"action":"insert","lines":[","],"id":309}]]},"ace":{"folds":[],"scrolltop":129.5,"scrollleft":0,"selection":{"start":{"row":27,"column":45},"end":{"row":27,"column":45},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":24,"state":"start","mode":"ace/mode/python"}},"timestamp":1567588867344,"hash":"bf22da0f1ffeda3394120368aba5269f47aa89db"}