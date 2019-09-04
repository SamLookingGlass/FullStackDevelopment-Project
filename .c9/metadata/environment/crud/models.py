{"filter":false,"title":"models.py","tooltip":"/crud/models.py","undoManager":{"mark":16,"position":16,"stack":[[{"start":{"row":9,"column":0},"end":{"row":11,"column":2},"action":"insert","lines":["class Category(models.Model):","    name = models.CharField(max_length=255, blank=False)","  "],"id":3}],[{"start":{"row":8,"column":24},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":9,"column":0},"end":{"row":9,"column":8},"action":"insert","lines":["        "]},{"start":{"row":9,"column":8},"end":{"row":10,"column":0},"action":"insert","lines":["",""]},{"start":{"row":10,"column":0},"end":{"row":10,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":3,"column":0},"end":{"row":8,"column":24},"action":"remove","lines":["class Item(models.Model):","    name = models.CharField(max_length=30, blank=False)","    done = models.BooleanField(blank=False, default=True)","","    def __str__(self):","        return self.name"],"id":5},{"start":{"row":3,"column":0},"end":{"row":9,"column":24},"action":"insert","lines":["class Item(models.Model):","    name = models.CharField(max_length=30, blank=False)","    done = models.BooleanField(blank=False, default=False)","    ongoing = models.BooleanField(blank=False, default=False)","    category = models.ForeignKey('Category', on_delete=models.CASCADE)","    def __str__(self):","        return self.name"]}],[{"start":{"row":14,"column":2},"end":{"row":14,"column":3},"action":"insert","lines":[" "],"id":7},{"start":{"row":14,"column":3},"end":{"row":14,"column":4},"action":"insert","lines":[" "]}],[{"start":{"row":14,"column":4},"end":{"row":15,"column":24},"action":"insert","lines":["def __str__(self):","        return self.name"],"id":8}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":70},"action":"remove","lines":["category = models.ForeignKey('Category', on_delete=models.CASCADE)"],"id":11}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":61},"action":"remove","lines":["    ongoing = models.BooleanField(blank=False, default=False)"],"id":12},{"start":{"row":5,"column":58},"end":{"row":6,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["c"],"id":13},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["a"]},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["t"]},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["e"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["g"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["o"]},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["r"]},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["y"]}],[{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":[" "],"id":14}],[{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"remove","lines":[" "],"id":15}],[{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":[" "],"id":16},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["="]}],[{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":[" "],"id":17},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["m"]},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["o"]},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["d"]},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":["e"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["l"]},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["s"]},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["."]},{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"insert","lines":["F"]}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":23},"action":"remove","lines":["category = models.F"],"id":18},{"start":{"row":6,"column":4},"end":{"row":6,"column":70},"action":"insert","lines":["category = models.ForeignKey('Category', on_delete=models.CASCADE)"]}],[{"start":{"row":14,"column":24},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":40},{"start":{"row":15,"column":0},"end":{"row":15,"column":8},"action":"insert","lines":["        "]},{"start":{"row":15,"column":8},"end":{"row":16,"column":0},"action":"insert","lines":["",""]},{"start":{"row":16,"column":0},"end":{"row":16,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":16,"column":0},"end":{"row":20,"column":24},"action":"insert","lines":["class Tag(models.Model):","    name = models.CharField(max_length=50, blank=False)","    ","    def __str__(self):","        return self.name"],"id":41}],[{"start":{"row":6,"column":70},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":42},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":40},"action":"insert","lines":["tags = models.ManyToManyField(\"Tag\")"],"id":43}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":7,"column":40},"end":{"row":7,"column":40},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1567572300499,"hash":"32c9ecc411ddbb13915c7f055da957e720c72cac"}