{"filter":false,"title":"models.py","tooltip":"/crud/models.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":41,"column":8},"end":{"row":41,"column":9},"action":"insert","lines":[" "],"id":578},{"start":{"row":41,"column":9},"end":{"row":41,"column":10},"action":"insert","lines":["="]}],[{"start":{"row":41,"column":10},"end":{"row":41,"column":11},"action":"insert","lines":[" "],"id":579}],[{"start":{"row":41,"column":11},"end":{"row":41,"column":71},"action":"insert","lines":["models.ForeignKey(Item, null=True, on_delete=models.CASCADE)"],"id":580}],[{"start":{"row":41,"column":71},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":581},{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":41,"column":33},"end":{"row":41,"column":34},"action":"insert","lines":["'"],"id":583}],[{"start":{"row":41,"column":29},"end":{"row":41,"column":30},"action":"insert","lines":["'"],"id":584}],[{"start":{"row":38,"column":8},"end":{"row":44,"column":25},"action":"remove","lines":["","class Inventory(models.Model):","    name = models.CharField(max_length=30, blank=False)","    item = models.ForeignKey('Item', null=True, on_delete=models.CASCADE)","    ","    def __str__(self):","        return self.name "],"id":586},{"start":{"row":38,"column":4},"end":{"row":38,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":50,"column":41},"end":{"row":50,"column":42},"action":"insert","lines":["g"],"id":587}],[{"start":{"row":50,"column":41},"end":{"row":50,"column":42},"action":"remove","lines":["g"],"id":588}],[{"start":{"row":38,"column":0},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":589}],[{"start":{"row":39,"column":0},"end":{"row":39,"column":1},"action":"insert","lines":["c"],"id":591},{"start":{"row":39,"column":1},"end":{"row":39,"column":2},"action":"insert","lines":["l"]},{"start":{"row":39,"column":2},"end":{"row":39,"column":3},"action":"insert","lines":["a"]},{"start":{"row":39,"column":3},"end":{"row":39,"column":4},"action":"insert","lines":["s"]},{"start":{"row":39,"column":4},"end":{"row":39,"column":5},"action":"insert","lines":["s"]}],[{"start":{"row":39,"column":5},"end":{"row":39,"column":6},"action":"insert","lines":[" "],"id":592},{"start":{"row":39,"column":6},"end":{"row":39,"column":7},"action":"insert","lines":["I"]},{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"insert","lines":["n"]},{"start":{"row":39,"column":8},"end":{"row":39,"column":9},"action":"insert","lines":["v"]},{"start":{"row":39,"column":9},"end":{"row":39,"column":10},"action":"insert","lines":["e"]},{"start":{"row":39,"column":10},"end":{"row":39,"column":11},"action":"insert","lines":["n"]},{"start":{"row":39,"column":11},"end":{"row":39,"column":12},"action":"insert","lines":["t"]},{"start":{"row":39,"column":12},"end":{"row":39,"column":13},"action":"insert","lines":["o"]},{"start":{"row":39,"column":13},"end":{"row":39,"column":14},"action":"insert","lines":["r"]},{"start":{"row":39,"column":14},"end":{"row":39,"column":15},"action":"insert","lines":["y"]}],[{"start":{"row":39,"column":15},"end":{"row":39,"column":17},"action":"insert","lines":["()"],"id":593}],[{"start":{"row":39,"column":16},"end":{"row":39,"column":17},"action":"insert","lines":["m"],"id":594},{"start":{"row":39,"column":17},"end":{"row":39,"column":18},"action":"insert","lines":["o"]},{"start":{"row":39,"column":18},"end":{"row":39,"column":19},"action":"insert","lines":["d"]},{"start":{"row":39,"column":19},"end":{"row":39,"column":20},"action":"insert","lines":["e"]},{"start":{"row":39,"column":20},"end":{"row":39,"column":21},"action":"insert","lines":["l"]},{"start":{"row":39,"column":21},"end":{"row":39,"column":22},"action":"insert","lines":["s"]},{"start":{"row":39,"column":22},"end":{"row":39,"column":23},"action":"insert","lines":["."]},{"start":{"row":39,"column":23},"end":{"row":39,"column":24},"action":"insert","lines":["M"]},{"start":{"row":39,"column":24},"end":{"row":39,"column":25},"action":"insert","lines":["o"]},{"start":{"row":39,"column":25},"end":{"row":39,"column":26},"action":"insert","lines":["d"]},{"start":{"row":39,"column":26},"end":{"row":39,"column":27},"action":"insert","lines":["e"]}],[{"start":{"row":39,"column":27},"end":{"row":39,"column":28},"action":"insert","lines":["l"],"id":595}],[{"start":{"row":39,"column":29},"end":{"row":39,"column":30},"action":"insert","lines":[":"],"id":596}],[{"start":{"row":39,"column":30},"end":{"row":39,"column":41},"action":"remove","lines":["           "],"id":597},{"start":{"row":39,"column":30},"end":{"row":40,"column":0},"action":"insert","lines":["",""]},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":40,"column":4},"end":{"row":42,"column":32},"action":"insert","lines":[" name = models.CharField(max_length=50, blank=False)","    def __str__(self):","        return self.name        "],"id":598}],[{"start":{"row":40,"column":4},"end":{"row":40,"column":5},"action":"remove","lines":[" "],"id":599}],[{"start":{"row":40,"column":0},"end":{"row":42,"column":26},"action":"remove","lines":["    name = models.CharField(max_length=50, blank=False)","    def __str__(self):","        return self.name  "],"id":600},{"start":{"row":39,"column":30},"end":{"row":40,"column":6},"action":"remove","lines":["","      "]},{"start":{"row":39,"column":29},"end":{"row":39,"column":30},"action":"remove","lines":[":"]},{"start":{"row":39,"column":28},"end":{"row":39,"column":29},"action":"remove","lines":[")"]},{"start":{"row":39,"column":27},"end":{"row":39,"column":28},"action":"remove","lines":["l"]},{"start":{"row":39,"column":26},"end":{"row":39,"column":27},"action":"remove","lines":["e"]},{"start":{"row":39,"column":25},"end":{"row":39,"column":26},"action":"remove","lines":["d"]},{"start":{"row":39,"column":24},"end":{"row":39,"column":25},"action":"remove","lines":["o"]},{"start":{"row":39,"column":23},"end":{"row":39,"column":24},"action":"remove","lines":["M"]},{"start":{"row":39,"column":22},"end":{"row":39,"column":23},"action":"remove","lines":["."]},{"start":{"row":39,"column":21},"end":{"row":39,"column":22},"action":"remove","lines":["s"]},{"start":{"row":39,"column":20},"end":{"row":39,"column":21},"action":"remove","lines":["l"]},{"start":{"row":39,"column":19},"end":{"row":39,"column":20},"action":"remove","lines":["e"]},{"start":{"row":39,"column":18},"end":{"row":39,"column":19},"action":"remove","lines":["d"]},{"start":{"row":39,"column":17},"end":{"row":39,"column":18},"action":"remove","lines":["o"]},{"start":{"row":39,"column":16},"end":{"row":39,"column":17},"action":"remove","lines":["m"]},{"start":{"row":39,"column":15},"end":{"row":39,"column":16},"action":"remove","lines":["("]},{"start":{"row":39,"column":14},"end":{"row":39,"column":15},"action":"remove","lines":["y"]},{"start":{"row":39,"column":13},"end":{"row":39,"column":14},"action":"remove","lines":["r"]},{"start":{"row":39,"column":12},"end":{"row":39,"column":13},"action":"remove","lines":["o"]},{"start":{"row":39,"column":11},"end":{"row":39,"column":12},"action":"remove","lines":["t"]},{"start":{"row":39,"column":10},"end":{"row":39,"column":11},"action":"remove","lines":["n"]},{"start":{"row":39,"column":9},"end":{"row":39,"column":10},"action":"remove","lines":["e"]},{"start":{"row":39,"column":8},"end":{"row":39,"column":9},"action":"remove","lines":["v"]},{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"remove","lines":["n"]},{"start":{"row":39,"column":6},"end":{"row":39,"column":7},"action":"remove","lines":["I"]},{"start":{"row":39,"column":5},"end":{"row":39,"column":6},"action":"remove","lines":[" "]},{"start":{"row":39,"column":4},"end":{"row":39,"column":5},"action":"remove","lines":["s"]},{"start":{"row":39,"column":3},"end":{"row":39,"column":4},"action":"remove","lines":["s"]},{"start":{"row":39,"column":2},"end":{"row":39,"column":3},"action":"remove","lines":["a"]},{"start":{"row":39,"column":1},"end":{"row":39,"column":2},"action":"remove","lines":["l"]},{"start":{"row":39,"column":0},"end":{"row":39,"column":1},"action":"remove","lines":["c"]},{"start":{"row":38,"column":0},"end":{"row":39,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":37,"column":24},"end":{"row":38,"column":0},"action":"remove","lines":["",""],"id":601}],[{"start":{"row":38,"column":0},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":602},{"start":{"row":39,"column":0},"end":{"row":39,"column":1},"action":"insert","lines":["c"]},{"start":{"row":39,"column":1},"end":{"row":39,"column":2},"action":"insert","lines":["l"]},{"start":{"row":39,"column":2},"end":{"row":39,"column":3},"action":"insert","lines":["a"]},{"start":{"row":39,"column":3},"end":{"row":39,"column":4},"action":"insert","lines":["s"]},{"start":{"row":39,"column":4},"end":{"row":39,"column":5},"action":"insert","lines":["s"]}],[{"start":{"row":39,"column":5},"end":{"row":39,"column":6},"action":"insert","lines":[" "],"id":603},{"start":{"row":39,"column":6},"end":{"row":39,"column":7},"action":"insert","lines":["I"]},{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"insert","lines":["n"]},{"start":{"row":39,"column":8},"end":{"row":39,"column":9},"action":"insert","lines":["v"]},{"start":{"row":39,"column":9},"end":{"row":39,"column":10},"action":"insert","lines":["e"]},{"start":{"row":39,"column":10},"end":{"row":39,"column":11},"action":"insert","lines":["n"]},{"start":{"row":39,"column":11},"end":{"row":39,"column":12},"action":"insert","lines":["t"]},{"start":{"row":39,"column":12},"end":{"row":39,"column":13},"action":"insert","lines":["o"]},{"start":{"row":39,"column":13},"end":{"row":39,"column":14},"action":"insert","lines":["r"]},{"start":{"row":39,"column":14},"end":{"row":39,"column":15},"action":"insert","lines":["y"]}],[{"start":{"row":39,"column":15},"end":{"row":39,"column":16},"action":"insert","lines":[" "],"id":604}],[{"start":{"row":39,"column":15},"end":{"row":39,"column":17},"action":"insert","lines":["()"],"id":605}],[{"start":{"row":39,"column":16},"end":{"row":39,"column":28},"action":"insert","lines":["models.Model"],"id":606}],[{"start":{"row":39,"column":29},"end":{"row":39,"column":30},"action":"insert","lines":[":"],"id":607}],[{"start":{"row":39,"column":30},"end":{"row":39,"column":31},"action":"remove","lines":[" "],"id":608},{"start":{"row":39,"column":30},"end":{"row":40,"column":0},"action":"insert","lines":["",""]},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":40,"column":4},"end":{"row":40,"column":62},"action":"insert","lines":["size = models.ForeignKey('Size', on_delete=models.CASCADE)"],"id":609}],[{"start":{"row":39,"column":30},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":610},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"insert","lines":["    "]},{"start":{"row":40,"column":4},"end":{"row":40,"column":5},"action":"insert","lines":["i"]},{"start":{"row":40,"column":5},"end":{"row":40,"column":6},"action":"insert","lines":["t"]},{"start":{"row":40,"column":6},"end":{"row":40,"column":7},"action":"insert","lines":["e"]},{"start":{"row":40,"column":7},"end":{"row":40,"column":8},"action":"insert","lines":["m"]}],[{"start":{"row":40,"column":8},"end":{"row":40,"column":9},"action":"insert","lines":[" "],"id":611},{"start":{"row":40,"column":9},"end":{"row":40,"column":10},"action":"insert","lines":["-"]}],[{"start":{"row":40,"column":10},"end":{"row":40,"column":11},"action":"insert","lines":[" "],"id":612}],[{"start":{"row":40,"column":9},"end":{"row":40,"column":10},"action":"remove","lines":["-"],"id":613}],[{"start":{"row":40,"column":9},"end":{"row":40,"column":10},"action":"insert","lines":["-"],"id":614}],[{"start":{"row":40,"column":9},"end":{"row":40,"column":10},"action":"remove","lines":["-"],"id":615}],[{"start":{"row":40,"column":9},"end":{"row":40,"column":10},"action":"insert","lines":["="],"id":616}],[{"start":{"row":40,"column":10},"end":{"row":40,"column":11},"action":"insert","lines":[" "],"id":617}],[{"start":{"row":40,"column":11},"end":{"row":40,"column":62},"action":"insert","lines":["models.ForeignKey('Size', on_delete=models.CASCADE)"],"id":618}],[{"start":{"row":41,"column":62},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":619},{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":42,"column":4},"end":{"row":44,"column":0},"action":"insert","lines":["def __str__(self):","        return self.name",""],"id":620}],[{"start":{"row":42,"column":0},"end":{"row":43,"column":0},"action":"insert","lines":["",""],"id":621}],[{"start":{"row":41,"column":62},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":622},{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":42,"column":4},"end":{"row":43,"column":0},"action":"remove","lines":["",""],"id":623}],[{"start":{"row":42,"column":4},"end":{"row":42,"column":5},"action":"insert","lines":["s"],"id":624},{"start":{"row":42,"column":5},"end":{"row":42,"column":6},"action":"insert","lines":["t"]},{"start":{"row":42,"column":6},"end":{"row":42,"column":7},"action":"insert","lines":["o"]},{"start":{"row":42,"column":7},"end":{"row":42,"column":8},"action":"insert","lines":["c"]},{"start":{"row":42,"column":8},"end":{"row":42,"column":9},"action":"insert","lines":["k"]}],[{"start":{"row":42,"column":9},"end":{"row":42,"column":10},"action":"insert","lines":[" "],"id":625},{"start":{"row":42,"column":10},"end":{"row":42,"column":11},"action":"insert","lines":["="]}],[{"start":{"row":42,"column":11},"end":{"row":42,"column":12},"action":"insert","lines":[" "],"id":626}],[{"start":{"row":42,"column":12},"end":{"row":42,"column":40},"action":"insert","lines":["models.FloatField(null=True)"],"id":627}],[{"start":{"row":42,"column":4},"end":{"row":42,"column":9},"action":"remove","lines":["stock"],"id":628},{"start":{"row":42,"column":4},"end":{"row":42,"column":5},"action":"insert","lines":["n"]},{"start":{"row":42,"column":5},"end":{"row":42,"column":6},"action":"insert","lines":["a"]},{"start":{"row":42,"column":6},"end":{"row":42,"column":7},"action":"insert","lines":["m"]},{"start":{"row":42,"column":7},"end":{"row":42,"column":8},"action":"insert","lines":["e"]}],[{"start":{"row":40,"column":30},"end":{"row":40,"column":34},"action":"remove","lines":["Size"],"id":629},{"start":{"row":40,"column":30},"end":{"row":40,"column":31},"action":"insert","lines":["I"]},{"start":{"row":40,"column":31},"end":{"row":40,"column":32},"action":"insert","lines":["t"]},{"start":{"row":40,"column":32},"end":{"row":40,"column":33},"action":"insert","lines":["e"]},{"start":{"row":40,"column":33},"end":{"row":40,"column":34},"action":"insert","lines":["m"]}],[{"start":{"row":40,"column":4},"end":{"row":40,"column":8},"action":"remove","lines":["item"],"id":630},{"start":{"row":40,"column":4},"end":{"row":40,"column":5},"action":"insert","lines":["p"]},{"start":{"row":40,"column":5},"end":{"row":40,"column":6},"action":"insert","lines":["r"]},{"start":{"row":40,"column":6},"end":{"row":40,"column":7},"action":"insert","lines":["o"]},{"start":{"row":40,"column":7},"end":{"row":40,"column":8},"action":"insert","lines":["d"]},{"start":{"row":40,"column":8},"end":{"row":40,"column":9},"action":"insert","lines":["u"]},{"start":{"row":40,"column":9},"end":{"row":40,"column":10},"action":"insert","lines":["c"]},{"start":{"row":40,"column":10},"end":{"row":40,"column":11},"action":"insert","lines":["t"]}],[{"start":{"row":42,"column":4},"end":{"row":42,"column":8},"action":"remove","lines":["name"],"id":631},{"start":{"row":42,"column":4},"end":{"row":42,"column":5},"action":"insert","lines":["s"]},{"start":{"row":42,"column":5},"end":{"row":42,"column":6},"action":"insert","lines":["t"]},{"start":{"row":42,"column":6},"end":{"row":42,"column":7},"action":"insert","lines":["i"]},{"start":{"row":42,"column":7},"end":{"row":42,"column":8},"action":"insert","lines":["c"]}],[{"start":{"row":42,"column":7},"end":{"row":42,"column":8},"action":"remove","lines":["c"],"id":632},{"start":{"row":42,"column":6},"end":{"row":42,"column":7},"action":"remove","lines":["i"]}],[{"start":{"row":42,"column":6},"end":{"row":42,"column":7},"action":"insert","lines":["o"],"id":633},{"start":{"row":42,"column":7},"end":{"row":42,"column":8},"action":"insert","lines":["c"]},{"start":{"row":42,"column":8},"end":{"row":42,"column":9},"action":"insert","lines":["k"]}],[{"start":{"row":39,"column":30},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":634},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"insert","lines":["    "]},{"start":{"row":40,"column":4},"end":{"row":40,"column":5},"action":"insert","lines":["n"]},{"start":{"row":40,"column":5},"end":{"row":40,"column":6},"action":"insert","lines":["a"]},{"start":{"row":40,"column":6},"end":{"row":40,"column":7},"action":"insert","lines":["m"]},{"start":{"row":40,"column":7},"end":{"row":40,"column":8},"action":"insert","lines":["e"]}],[{"start":{"row":40,"column":8},"end":{"row":40,"column":9},"action":"insert","lines":[" "],"id":635},{"start":{"row":40,"column":9},"end":{"row":40,"column":10},"action":"insert","lines":["="]}],[{"start":{"row":40,"column":10},"end":{"row":40,"column":11},"action":"insert","lines":[" "],"id":636}],[{"start":{"row":40,"column":11},"end":{"row":41,"column":13},"action":"remove","lines":["","    product ="],"id":637}],[{"start":{"row":40,"column":11},"end":{"row":40,"column":12},"action":"remove","lines":[" "],"id":638}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":62},"action":"remove","lines":["    size = models.ForeignKey('Size', on_delete=models.CASCADE)"],"id":639},{"start":{"row":19,"column":40},"end":{"row":20,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":41,"column":0},"end":{"row":41,"column":40},"action":"remove","lines":["    stock = models.FloatField(null=True)"],"id":640},{"start":{"row":40,"column":62},"end":{"row":41,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":41,"column":4},"end":{"row":41,"column":5},"action":"insert","lines":["#"],"id":642}],[{"start":{"row":42,"column":8},"end":{"row":42,"column":9},"action":"insert","lines":["#"],"id":643}],[{"start":{"row":40,"column":4},"end":{"row":40,"column":6},"action":"insert","lines":["# "],"id":644}],[{"start":{"row":40,"column":4},"end":{"row":40,"column":6},"action":"remove","lines":["# "],"id":645}],[{"start":{"row":41,"column":4},"end":{"row":41,"column":5},"action":"remove","lines":["#"],"id":647}],[{"start":{"row":42,"column":8},"end":{"row":42,"column":9},"action":"remove","lines":["#"],"id":648}],[{"start":{"row":42,"column":24},"end":{"row":42,"column":25},"action":"insert","lines":["."],"id":649},{"start":{"row":42,"column":25},"end":{"row":42,"column":26},"action":"insert","lines":["n"]},{"start":{"row":42,"column":26},"end":{"row":42,"column":27},"action":"insert","lines":["a"]},{"start":{"row":42,"column":27},"end":{"row":42,"column":28},"action":"insert","lines":["m"]},{"start":{"row":42,"column":28},"end":{"row":42,"column":29},"action":"insert","lines":["e"]}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":8},"action":"remove","lines":["name"],"id":650},{"start":{"row":39,"column":4},"end":{"row":39,"column":5},"action":"insert","lines":["i"]},{"start":{"row":39,"column":5},"end":{"row":39,"column":6},"action":"insert","lines":["t"]},{"start":{"row":39,"column":6},"end":{"row":39,"column":7},"action":"insert","lines":["e"]},{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"insert","lines":["m"]}],[{"start":{"row":42,"column":23},"end":{"row":42,"column":24},"action":"remove","lines":["e"],"id":651},{"start":{"row":42,"column":22},"end":{"row":42,"column":23},"action":"remove","lines":["m"]},{"start":{"row":42,"column":21},"end":{"row":42,"column":22},"action":"remove","lines":["a"]},{"start":{"row":42,"column":20},"end":{"row":42,"column":21},"action":"remove","lines":["n"]}],[{"start":{"row":42,"column":20},"end":{"row":42,"column":21},"action":"insert","lines":["i"],"id":652},{"start":{"row":42,"column":21},"end":{"row":42,"column":22},"action":"insert","lines":["t"]},{"start":{"row":42,"column":22},"end":{"row":42,"column":23},"action":"insert","lines":["e"]},{"start":{"row":42,"column":23},"end":{"row":42,"column":24},"action":"insert","lines":["m"]}],[{"start":{"row":42,"column":29},"end":{"row":42,"column":30},"action":"insert","lines":[" "],"id":653}],[{"start":{"row":42,"column":30},"end":{"row":42,"column":31},"action":"insert","lines":["+"],"id":654}],[{"start":{"row":42,"column":31},"end":{"row":42,"column":32},"action":"insert","lines":[" "],"id":655}],[{"start":{"row":42,"column":32},"end":{"row":42,"column":34},"action":"insert","lines":["\"\""],"id":656}],[{"start":{"row":42,"column":33},"end":{"row":42,"column":34},"action":"insert","lines":[" "],"id":657}],[{"start":{"row":42,"column":35},"end":{"row":42,"column":36},"action":"insert","lines":[" "],"id":658},{"start":{"row":42,"column":36},"end":{"row":42,"column":37},"action":"insert","lines":["+"]}],[{"start":{"row":42,"column":37},"end":{"row":42,"column":38},"action":"insert","lines":[" "],"id":659}],[{"start":{"row":42,"column":37},"end":{"row":42,"column":38},"action":"insert","lines":[" "],"id":660}],[{"start":{"row":42,"column":38},"end":{"row":42,"column":52},"action":"insert","lines":["self.item.name"],"id":661}],[{"start":{"row":42,"column":43},"end":{"row":42,"column":47},"action":"remove","lines":["item"],"id":662},{"start":{"row":42,"column":43},"end":{"row":42,"column":44},"action":"insert","lines":["s"]},{"start":{"row":42,"column":44},"end":{"row":42,"column":45},"action":"insert","lines":["i"]},{"start":{"row":42,"column":45},"end":{"row":42,"column":46},"action":"insert","lines":["z"]},{"start":{"row":42,"column":46},"end":{"row":42,"column":47},"action":"insert","lines":["e"]}],[{"start":{"row":40,"column":62},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":663},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"insert","lines":["    "]},{"start":{"row":41,"column":4},"end":{"row":41,"column":5},"action":"insert","lines":["s"]},{"start":{"row":41,"column":5},"end":{"row":41,"column":6},"action":"insert","lines":["t"]},{"start":{"row":41,"column":6},"end":{"row":41,"column":7},"action":"insert","lines":["o"]},{"start":{"row":41,"column":7},"end":{"row":41,"column":8},"action":"insert","lines":["c"]},{"start":{"row":41,"column":8},"end":{"row":41,"column":9},"action":"insert","lines":["k"]}],[{"start":{"row":41,"column":9},"end":{"row":41,"column":10},"action":"insert","lines":[" "],"id":664},{"start":{"row":41,"column":10},"end":{"row":41,"column":11},"action":"insert","lines":["="]}],[{"start":{"row":41,"column":11},"end":{"row":41,"column":12},"action":"insert","lines":[" "],"id":665}],[{"start":{"row":41,"column":12},"end":{"row":41,"column":40},"action":"insert","lines":["models.FloatField(null=True)"],"id":666}],[{"start":{"row":14,"column":40},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":667},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["p"]},{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"insert","lines":["r"]},{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"insert","lines":["o"]},{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"insert","lines":["d"]},{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"insert","lines":["u"]},{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"insert","lines":["c"]},{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":["_"],"id":668},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["d"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":["e"]},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["s"]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["c"]}],[{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"remove","lines":["c"],"id":669},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"remove","lines":["s"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"remove","lines":["e"]},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"remove","lines":["d"]},{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"remove","lines":["_"]},{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"remove","lines":["t"]},{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"remove","lines":["c"]},{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"remove","lines":["u"]},{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"remove","lines":["d"]},{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"remove","lines":["o"]},{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"remove","lines":["r"]},{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"remove","lines":["p"]}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["d"],"id":670},{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"insert","lines":["e"]},{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"insert","lines":["s"]},{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"insert","lines":["c"]},{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"insert","lines":["r"]},{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"insert","lines":["i"]},{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"insert","lines":["p"]},{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":["t"]},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["i"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":["o"]},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["n"]}],[{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":[" "],"id":671},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["="]}],[{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":[" "],"id":672}],[{"start":{"row":15,"column":18},"end":{"row":15,"column":63},"action":"insert","lines":["models.CharField(max_length=255, blank=False)"],"id":673}],[{"start":{"row":15,"column":51},"end":{"row":15,"column":62},"action":"remove","lines":["blank=False"],"id":674},{"start":{"row":15,"column":51},"end":{"row":15,"column":60},"action":"insert","lines":["null=True"]}],[{"start":{"row":15,"column":60},"end":{"row":15,"column":61},"action":"insert","lines":[","],"id":675}],[{"start":{"row":15,"column":61},"end":{"row":15,"column":62},"action":"insert","lines":[" "],"id":676},{"start":{"row":15,"column":62},"end":{"row":15,"column":63},"action":"insert","lines":["b"]},{"start":{"row":15,"column":63},"end":{"row":15,"column":64},"action":"insert","lines":["l"]},{"start":{"row":15,"column":64},"end":{"row":15,"column":65},"action":"insert","lines":["a"]},{"start":{"row":15,"column":65},"end":{"row":15,"column":66},"action":"insert","lines":["n"]},{"start":{"row":15,"column":66},"end":{"row":15,"column":67},"action":"insert","lines":["k"]},{"start":{"row":15,"column":67},"end":{"row":15,"column":68},"action":"insert","lines":["="]},{"start":{"row":15,"column":68},"end":{"row":15,"column":69},"action":"insert","lines":["T"]},{"start":{"row":15,"column":69},"end":{"row":15,"column":70},"action":"insert","lines":["r"]}],[{"start":{"row":15,"column":70},"end":{"row":15,"column":71},"action":"insert","lines":["u"],"id":677},{"start":{"row":15,"column":71},"end":{"row":15,"column":72},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":49},"end":{"row":15,"column":72},"action":"remove","lines":[", null=True, blank=True"],"id":681}],[{"start":{"row":15,"column":49},"end":{"row":15,"column":50},"action":"insert","lines":[","],"id":682}],[{"start":{"row":15,"column":50},"end":{"row":15,"column":51},"action":"insert","lines":[" "],"id":683},{"start":{"row":15,"column":51},"end":{"row":15,"column":52},"action":"insert","lines":["n"]},{"start":{"row":15,"column":52},"end":{"row":15,"column":53},"action":"insert","lines":["i"]}],[{"start":{"row":15,"column":52},"end":{"row":15,"column":53},"action":"remove","lines":["i"],"id":684}],[{"start":{"row":15,"column":52},"end":{"row":15,"column":53},"action":"insert","lines":["u"],"id":685},{"start":{"row":15,"column":53},"end":{"row":15,"column":54},"action":"insert","lines":["l"]},{"start":{"row":15,"column":54},"end":{"row":15,"column":55},"action":"insert","lines":["l"]},{"start":{"row":15,"column":55},"end":{"row":15,"column":56},"action":"insert","lines":["="]},{"start":{"row":15,"column":56},"end":{"row":15,"column":57},"action":"insert","lines":["T"]},{"start":{"row":15,"column":57},"end":{"row":15,"column":58},"action":"insert","lines":["r"]},{"start":{"row":15,"column":58},"end":{"row":15,"column":59},"action":"insert","lines":["u"]},{"start":{"row":15,"column":59},"end":{"row":15,"column":60},"action":"insert","lines":["e"]}],[{"start":{"row":46,"column":0},"end":{"row":60,"column":0},"action":"remove","lines":["# Link between 2 models","class OrderItem(models.Model):","    item = models.ForeignKey(Item, null=True, on_delete=models.CASCADE)","    def __str__(self):","        return self.name        ","","class Order(models.Model):","    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)","    items = models.ManyToManyField(OrderItem)","    start_date = models.DateTimeField(auto_now_add=True)","    ordered_date = models.DateTimeField()","    ordered = models.BooleanField(default=False)","    def __str__(self):","        return self.name        ",""],"id":686}]]},"ace":{"folds":[],"scrolltop":402,"scrollleft":0,"selection":{"start":{"row":47,"column":0},"end":{"row":47,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":27,"state":"start","mode":"ace/mode/python"}},"timestamp":1567737338576,"hash":"459369628536b4b5931701d093a01e0d6aed2990"}