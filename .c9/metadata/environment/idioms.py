{"filter":false,"title":"idioms.py","tooltip":"/idioms.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":21,"column":12},"end":{"row":21,"column":13},"action":"insert","lines":["/"],"id":1414},{"start":{"row":21,"column":13},"end":{"row":21,"column":14},"action":"insert","lines":["p"]},{"start":{"row":21,"column":14},"end":{"row":21,"column":15},"action":"insert","lines":["a"]}],[{"start":{"row":21,"column":15},"end":{"row":21,"column":16},"action":"insert","lines":["g"],"id":1415},{"start":{"row":21,"column":16},"end":{"row":21,"column":17},"action":"insert","lines":["e"]},{"start":{"row":21,"column":17},"end":{"row":21,"column":18},"action":"insert","lines":["t"]}],[{"start":{"row":21,"column":17},"end":{"row":21,"column":18},"action":"remove","lines":["t"],"id":1416}],[{"start":{"row":21,"column":17},"end":{"row":21,"column":18},"action":"insert","lines":["_"],"id":1417},{"start":{"row":21,"column":18},"end":{"row":21,"column":19},"action":"insert","lines":["t"]},{"start":{"row":21,"column":19},"end":{"row":21,"column":20},"action":"insert","lines":["w"]},{"start":{"row":21,"column":20},"end":{"row":21,"column":21},"action":"insert","lines":["o"]}],[{"start":{"row":22,"column":0},"end":{"row":27,"column":115},"action":"insert","lines":["def get_idioms():","    ","    pageSize = 2","    pageNum = 1","    ","    return render_template(\"idioms.html\", idioms=mongo.db.idioms.find().skip(pageSize*(pageNum-1)).limit(pageSize))"],"id":1418}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":14},"action":"remove","lines":["get_idioms"],"id":1419},{"start":{"row":22,"column":4},"end":{"row":22,"column":5},"action":"insert","lines":["p"]}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":5},"action":"remove","lines":["p"],"id":1420},{"start":{"row":22,"column":4},"end":{"row":22,"column":12},"action":"insert","lines":["page_two"]}],[{"start":{"row":25,"column":14},"end":{"row":25,"column":15},"action":"remove","lines":["1"],"id":1421}],[{"start":{"row":25,"column":14},"end":{"row":25,"column":15},"action":"insert","lines":["2"],"id":1422}],[{"start":{"row":27,"column":115},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":1423},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "]},{"start":{"row":28,"column":4},"end":{"row":29,"column":0},"action":"insert","lines":["",""]},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"remove","lines":["    "],"id":1424}],[{"start":{"row":29,"column":0},"end":{"row":35,"column":115},"action":"insert","lines":["@app.route(\"/page_two\")","def page_two():","    ","    pageSize = 2","    pageNum = 2","    ","    return render_template(\"idioms.html\", idioms=mongo.db.idioms.find().skip(pageSize*(pageNum-1)).limit(pageSize))"],"id":1425}],[{"start":{"row":29,"column":20},"end":{"row":29,"column":21},"action":"remove","lines":["o"],"id":1426},{"start":{"row":29,"column":19},"end":{"row":29,"column":20},"action":"remove","lines":["w"]},{"start":{"row":29,"column":18},"end":{"row":29,"column":19},"action":"remove","lines":["t"]}],[{"start":{"row":29,"column":18},"end":{"row":29,"column":19},"action":"insert","lines":["t"],"id":1427},{"start":{"row":29,"column":19},"end":{"row":29,"column":20},"action":"insert","lines":["h"]},{"start":{"row":29,"column":20},"end":{"row":29,"column":21},"action":"insert","lines":["r"]},{"start":{"row":29,"column":21},"end":{"row":29,"column":22},"action":"insert","lines":["e"]},{"start":{"row":29,"column":22},"end":{"row":29,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":30,"column":11},"end":{"row":30,"column":12},"action":"remove","lines":["o"],"id":1428},{"start":{"row":30,"column":10},"end":{"row":30,"column":11},"action":"remove","lines":["w"]}],[{"start":{"row":30,"column":10},"end":{"row":30,"column":11},"action":"insert","lines":["h"],"id":1429},{"start":{"row":30,"column":11},"end":{"row":30,"column":12},"action":"insert","lines":["t"]}],[{"start":{"row":30,"column":11},"end":{"row":30,"column":12},"action":"remove","lines":["t"],"id":1430}],[{"start":{"row":30,"column":11},"end":{"row":30,"column":12},"action":"insert","lines":["r"],"id":1431},{"start":{"row":30,"column":12},"end":{"row":30,"column":13},"action":"insert","lines":["e"]},{"start":{"row":30,"column":13},"end":{"row":30,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":33,"column":14},"end":{"row":33,"column":15},"action":"remove","lines":["2"],"id":1432}],[{"start":{"row":33,"column":14},"end":{"row":33,"column":15},"action":"insert","lines":["3"],"id":1433}],[{"start":{"row":16,"column":15},"end":{"row":16,"column":16},"action":"remove","lines":["2"],"id":1434}],[{"start":{"row":16,"column":15},"end":{"row":16,"column":16},"action":"insert","lines":["1"],"id":1435},{"start":{"row":16,"column":16},"end":{"row":16,"column":17},"action":"insert","lines":["0"]}],[{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"remove","lines":["2"],"id":1436}],[{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"insert","lines":["1"],"id":1437},{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"insert","lines":["0"]}],[{"start":{"row":32,"column":15},"end":{"row":32,"column":16},"action":"remove","lines":["2"],"id":1438}],[{"start":{"row":32,"column":15},"end":{"row":32,"column":16},"action":"insert","lines":["1"],"id":1439},{"start":{"row":32,"column":16},"end":{"row":32,"column":17},"action":"insert","lines":["0"]}],[{"start":{"row":35,"column":115},"end":{"row":36,"column":0},"action":"insert","lines":["",""],"id":1440},{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"insert","lines":["    "]},{"start":{"row":36,"column":4},"end":{"row":37,"column":0},"action":"insert","lines":["",""]},{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"remove","lines":["    "],"id":1441}],[{"start":{"row":37,"column":0},"end":{"row":44,"column":0},"action":"insert","lines":["@app.route(\"/page_three\")","def page_three():","    ","    pageSize = 10","    pageNum = 3","    ","    return render_template(\"idioms.html\", idioms=mongo.db.idioms.find().skip(pageSize*(pageNum-1)).limit(pageSize))",""],"id":1442}],[{"start":{"row":37,"column":22},"end":{"row":37,"column":23},"action":"remove","lines":["e"],"id":1443},{"start":{"row":37,"column":21},"end":{"row":37,"column":22},"action":"remove","lines":["e"]},{"start":{"row":37,"column":20},"end":{"row":37,"column":21},"action":"remove","lines":["r"]},{"start":{"row":37,"column":19},"end":{"row":37,"column":20},"action":"remove","lines":["h"]},{"start":{"row":37,"column":18},"end":{"row":37,"column":19},"action":"remove","lines":["t"]}],[{"start":{"row":37,"column":18},"end":{"row":37,"column":19},"action":"insert","lines":["f"],"id":1444},{"start":{"row":37,"column":19},"end":{"row":37,"column":20},"action":"insert","lines":["o"]},{"start":{"row":37,"column":20},"end":{"row":37,"column":21},"action":"insert","lines":["u"]},{"start":{"row":37,"column":21},"end":{"row":37,"column":22},"action":"insert","lines":["r"]}],[{"start":{"row":38,"column":13},"end":{"row":38,"column":14},"action":"remove","lines":["e"],"id":1445},{"start":{"row":38,"column":12},"end":{"row":38,"column":13},"action":"remove","lines":["e"]},{"start":{"row":38,"column":11},"end":{"row":38,"column":12},"action":"remove","lines":["r"]},{"start":{"row":38,"column":10},"end":{"row":38,"column":11},"action":"remove","lines":["h"]},{"start":{"row":38,"column":9},"end":{"row":38,"column":10},"action":"remove","lines":["t"]}],[{"start":{"row":38,"column":9},"end":{"row":38,"column":10},"action":"insert","lines":["f"],"id":1446},{"start":{"row":38,"column":10},"end":{"row":38,"column":11},"action":"insert","lines":["o"]},{"start":{"row":38,"column":11},"end":{"row":38,"column":12},"action":"insert","lines":["u"]},{"start":{"row":38,"column":12},"end":{"row":38,"column":13},"action":"insert","lines":["r"]}],[{"start":{"row":41,"column":14},"end":{"row":41,"column":15},"action":"remove","lines":["3"],"id":1447}],[{"start":{"row":41,"column":14},"end":{"row":41,"column":15},"action":"insert","lines":["4"],"id":1448}],[{"start":{"row":43,"column":115},"end":{"row":44,"column":0},"action":"insert","lines":["",""],"id":1449},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]},{"start":{"row":44,"column":4},"end":{"row":45,"column":0},"action":"insert","lines":["",""]},{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"remove","lines":["    "],"id":1450}],[{"start":{"row":45,"column":0},"end":{"row":52,"column":0},"action":"insert","lines":["@app.route(\"/page_three\")","def page_three():","    ","    pageSize = 10","    pageNum = 3","    ","    return render_template(\"idioms.html\", idioms=mongo.db.idioms.find().skip(pageSize*(pageNum-1)).limit(pageSize))",""],"id":1451}],[{"start":{"row":45,"column":22},"end":{"row":45,"column":23},"action":"remove","lines":["e"],"id":1452},{"start":{"row":45,"column":21},"end":{"row":45,"column":22},"action":"remove","lines":["e"]},{"start":{"row":45,"column":20},"end":{"row":45,"column":21},"action":"remove","lines":["r"]},{"start":{"row":45,"column":19},"end":{"row":45,"column":20},"action":"remove","lines":["h"]},{"start":{"row":45,"column":18},"end":{"row":45,"column":19},"action":"remove","lines":["t"]}],[{"start":{"row":45,"column":18},"end":{"row":45,"column":19},"action":"insert","lines":["f"],"id":1453},{"start":{"row":45,"column":19},"end":{"row":45,"column":20},"action":"insert","lines":["i"]},{"start":{"row":45,"column":20},"end":{"row":45,"column":21},"action":"insert","lines":["v"]},{"start":{"row":45,"column":21},"end":{"row":45,"column":22},"action":"insert","lines":["e"]}],[{"start":{"row":46,"column":13},"end":{"row":46,"column":14},"action":"remove","lines":["e"],"id":1454},{"start":{"row":46,"column":12},"end":{"row":46,"column":13},"action":"remove","lines":["e"]},{"start":{"row":46,"column":11},"end":{"row":46,"column":12},"action":"remove","lines":["r"]},{"start":{"row":46,"column":10},"end":{"row":46,"column":11},"action":"remove","lines":["h"]},{"start":{"row":46,"column":9},"end":{"row":46,"column":10},"action":"remove","lines":["t"]}],[{"start":{"row":46,"column":9},"end":{"row":46,"column":10},"action":"insert","lines":["f"],"id":1455},{"start":{"row":46,"column":10},"end":{"row":46,"column":11},"action":"insert","lines":["i"]},{"start":{"row":46,"column":11},"end":{"row":46,"column":12},"action":"insert","lines":["v"]},{"start":{"row":46,"column":12},"end":{"row":46,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":49,"column":14},"end":{"row":49,"column":15},"action":"remove","lines":["3"],"id":1456}],[{"start":{"row":49,"column":14},"end":{"row":49,"column":15},"action":"insert","lines":["5"],"id":1457}],[{"start":{"row":51,"column":115},"end":{"row":52,"column":0},"action":"insert","lines":["",""],"id":1458},{"start":{"row":52,"column":0},"end":{"row":52,"column":4},"action":"insert","lines":["    "]},{"start":{"row":52,"column":4},"end":{"row":53,"column":0},"action":"insert","lines":["",""]},{"start":{"row":53,"column":0},"end":{"row":53,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":53,"column":0},"end":{"row":53,"column":4},"action":"remove","lines":["    "],"id":1459}],[{"start":{"row":53,"column":0},"end":{"row":60,"column":0},"action":"insert","lines":["@app.route(\"/page_three\")","def page_three():","    ","    pageSize = 10","    pageNum = 3","    ","    return render_template(\"idioms.html\", idioms=mongo.db.idioms.find().skip(pageSize*(pageNum-1)).limit(pageSize))",""],"id":1460}],[{"start":{"row":53,"column":22},"end":{"row":53,"column":23},"action":"remove","lines":["e"],"id":1461},{"start":{"row":53,"column":21},"end":{"row":53,"column":22},"action":"remove","lines":["e"]},{"start":{"row":53,"column":20},"end":{"row":53,"column":21},"action":"remove","lines":["r"]},{"start":{"row":53,"column":19},"end":{"row":53,"column":20},"action":"remove","lines":["h"]},{"start":{"row":53,"column":18},"end":{"row":53,"column":19},"action":"remove","lines":["t"]}],[{"start":{"row":53,"column":18},"end":{"row":53,"column":19},"action":"insert","lines":["s"],"id":1462},{"start":{"row":53,"column":19},"end":{"row":53,"column":20},"action":"insert","lines":["i"]},{"start":{"row":53,"column":20},"end":{"row":53,"column":21},"action":"insert","lines":["x"]}],[{"start":{"row":54,"column":13},"end":{"row":54,"column":14},"action":"remove","lines":["e"],"id":1463},{"start":{"row":54,"column":12},"end":{"row":54,"column":13},"action":"remove","lines":["e"]},{"start":{"row":54,"column":11},"end":{"row":54,"column":12},"action":"remove","lines":["r"]},{"start":{"row":54,"column":10},"end":{"row":54,"column":11},"action":"remove","lines":["h"]},{"start":{"row":54,"column":9},"end":{"row":54,"column":10},"action":"remove","lines":["t"]}],[{"start":{"row":54,"column":9},"end":{"row":54,"column":10},"action":"insert","lines":["s"],"id":1464},{"start":{"row":54,"column":10},"end":{"row":54,"column":11},"action":"insert","lines":["i"]},{"start":{"row":54,"column":11},"end":{"row":54,"column":12},"action":"insert","lines":["x"]}],[{"start":{"row":57,"column":14},"end":{"row":57,"column":15},"action":"remove","lines":["3"],"id":1465}],[{"start":{"row":57,"column":14},"end":{"row":57,"column":15},"action":"insert","lines":["6"],"id":1466}],[{"start":{"row":56,"column":16},"end":{"row":56,"column":17},"action":"remove","lines":["0"],"id":1467}],[{"start":{"row":56,"column":16},"end":{"row":56,"column":17},"action":"insert","lines":["5"],"id":1468}],[{"start":{"row":56,"column":16},"end":{"row":56,"column":17},"action":"remove","lines":["5"],"id":1469}],[{"start":{"row":56,"column":16},"end":{"row":56,"column":17},"action":"insert","lines":["0"],"id":1470}],[{"start":{"row":59,"column":98},"end":{"row":59,"column":114},"action":"remove","lines":[".limit(pageSize)"],"id":1471}],[{"start":{"row":98,"column":26},"end":{"row":98,"column":27},"action":"insert","lines":["_"],"id":1472},{"start":{"row":98,"column":27},"end":{"row":98,"column":28},"action":"insert","lines":["o"]},{"start":{"row":98,"column":28},"end":{"row":98,"column":29},"action":"insert","lines":["n"]},{"start":{"row":98,"column":29},"end":{"row":98,"column":30},"action":"insert","lines":["e"]}],[{"start":{"row":98,"column":29},"end":{"row":98,"column":30},"action":"remove","lines":["e"],"id":1473},{"start":{"row":98,"column":28},"end":{"row":98,"column":29},"action":"remove","lines":["n"]},{"start":{"row":98,"column":27},"end":{"row":98,"column":28},"action":"remove","lines":["o"]},{"start":{"row":98,"column":26},"end":{"row":98,"column":27},"action":"remove","lines":["_"]}],[{"start":{"row":98,"column":26},"end":{"row":98,"column":27},"action":"insert","lines":["_"],"id":1474},{"start":{"row":98,"column":27},"end":{"row":98,"column":28},"action":"insert","lines":["o"]},{"start":{"row":98,"column":28},"end":{"row":98,"column":29},"action":"insert","lines":["n"]},{"start":{"row":98,"column":29},"end":{"row":98,"column":30},"action":"insert","lines":["e"]}],[{"start":{"row":98,"column":29},"end":{"row":98,"column":30},"action":"remove","lines":["e"],"id":1475},{"start":{"row":98,"column":28},"end":{"row":98,"column":29},"action":"remove","lines":["n"]},{"start":{"row":98,"column":27},"end":{"row":98,"column":28},"action":"remove","lines":["o"]},{"start":{"row":98,"column":26},"end":{"row":98,"column":27},"action":"remove","lines":["_"]}],[{"start":{"row":59,"column":97},"end":{"row":59,"column":113},"action":"insert","lines":[".limit(pageSize)"],"id":1476}],[{"start":{"row":59,"column":113},"end":{"row":59,"column":114},"action":"remove","lines":[")"],"id":1477}],[{"start":{"row":59,"column":97},"end":{"row":59,"column":98},"action":"insert","lines":[")"],"id":1478}],[{"start":{"row":19,"column":115},"end":{"row":19,"column":116},"action":"insert","lines":["."],"id":1479}],[{"start":{"row":19,"column":116},"end":{"row":19,"column":117},"action":"insert","lines":["s"],"id":1480},{"start":{"row":19,"column":117},"end":{"row":19,"column":118},"action":"insert","lines":["o"]},{"start":{"row":19,"column":118},"end":{"row":19,"column":119},"action":"insert","lines":["r"]},{"start":{"row":19,"column":119},"end":{"row":19,"column":120},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":120},"end":{"row":19,"column":122},"action":"insert","lines":["()"],"id":1481}],[{"start":{"row":19,"column":120},"end":{"row":19,"column":121},"action":"insert","lines":["e"],"id":1482},{"start":{"row":19,"column":121},"end":{"row":19,"column":122},"action":"insert","lines":["d"]}],[{"start":{"row":19,"column":123},"end":{"row":19,"column":124},"action":"insert","lines":["_"],"id":1483},{"start":{"row":19,"column":124},"end":{"row":19,"column":125},"action":"insert","lines":["i"]},{"start":{"row":19,"column":125},"end":{"row":19,"column":126},"action":"insert","lines":["d"]}],[{"start":{"row":19,"column":126},"end":{"row":19,"column":127},"action":"insert","lines":["="],"id":1484}],[{"start":{"row":19,"column":127},"end":{"row":19,"column":128},"action":"insert","lines":["d"],"id":1485},{"start":{"row":19,"column":128},"end":{"row":19,"column":129},"action":"insert","lines":["e"]},{"start":{"row":19,"column":129},"end":{"row":19,"column":130},"action":"insert","lines":["s"]}],[{"start":{"row":19,"column":130},"end":{"row":19,"column":131},"action":"insert","lines":["c"],"id":1486},{"start":{"row":19,"column":131},"end":{"row":19,"column":132},"action":"insert","lines":["e"]},{"start":{"row":19,"column":132},"end":{"row":19,"column":133},"action":"insert","lines":["n"]},{"start":{"row":19,"column":133},"end":{"row":19,"column":134},"action":"insert","lines":["d"]},{"start":{"row":19,"column":134},"end":{"row":19,"column":135},"action":"insert","lines":["i"]},{"start":{"row":19,"column":135},"end":{"row":19,"column":136},"action":"insert","lines":["n"]},{"start":{"row":19,"column":136},"end":{"row":19,"column":137},"action":"insert","lines":["g"]}],[{"start":{"row":19,"column":121},"end":{"row":19,"column":122},"action":"remove","lines":["d"],"id":1487},{"start":{"row":19,"column":120},"end":{"row":19,"column":121},"action":"remove","lines":["e"]}],[{"start":{"row":19,"column":134},"end":{"row":19,"column":135},"action":"remove","lines":["g"],"id":1488},{"start":{"row":19,"column":133},"end":{"row":19,"column":134},"action":"remove","lines":["n"]},{"start":{"row":19,"column":132},"end":{"row":19,"column":133},"action":"remove","lines":["i"]},{"start":{"row":19,"column":131},"end":{"row":19,"column":132},"action":"remove","lines":["d"]},{"start":{"row":19,"column":130},"end":{"row":19,"column":131},"action":"remove","lines":["n"]},{"start":{"row":19,"column":129},"end":{"row":19,"column":130},"action":"remove","lines":["e"]},{"start":{"row":19,"column":128},"end":{"row":19,"column":129},"action":"remove","lines":["c"]},{"start":{"row":19,"column":127},"end":{"row":19,"column":128},"action":"remove","lines":["s"]},{"start":{"row":19,"column":126},"end":{"row":19,"column":127},"action":"remove","lines":["e"]},{"start":{"row":19,"column":125},"end":{"row":19,"column":126},"action":"remove","lines":["d"]},{"start":{"row":19,"column":124},"end":{"row":19,"column":125},"action":"remove","lines":["="]},{"start":{"row":19,"column":123},"end":{"row":19,"column":124},"action":"remove","lines":["d"]},{"start":{"row":19,"column":122},"end":{"row":19,"column":123},"action":"remove","lines":["i"]},{"start":{"row":19,"column":121},"end":{"row":19,"column":122},"action":"remove","lines":["_"]}],[{"start":{"row":19,"column":121},"end":{"row":19,"column":123},"action":"insert","lines":["\"\""],"id":1489}],[{"start":{"row":19,"column":122},"end":{"row":19,"column":123},"action":"insert","lines":["_"],"id":1490},{"start":{"row":19,"column":123},"end":{"row":19,"column":124},"action":"insert","lines":["i"]},{"start":{"row":19,"column":124},"end":{"row":19,"column":125},"action":"insert","lines":["d"]}],[{"start":{"row":19,"column":126},"end":{"row":19,"column":127},"action":"insert","lines":[","],"id":1491}],[{"start":{"row":19,"column":127},"end":{"row":19,"column":128},"action":"insert","lines":[" "],"id":1492},{"start":{"row":19,"column":128},"end":{"row":19,"column":129},"action":"insert","lines":["-"]},{"start":{"row":19,"column":129},"end":{"row":19,"column":130},"action":"insert","lines":["1"]}],[{"start":{"row":19,"column":130},"end":{"row":19,"column":131},"action":"remove","lines":[")"],"id":1493},{"start":{"row":19,"column":129},"end":{"row":19,"column":130},"action":"remove","lines":["1"]},{"start":{"row":19,"column":128},"end":{"row":19,"column":129},"action":"remove","lines":["-"]},{"start":{"row":19,"column":127},"end":{"row":19,"column":128},"action":"remove","lines":[" "]},{"start":{"row":19,"column":126},"end":{"row":19,"column":127},"action":"remove","lines":[","]},{"start":{"row":19,"column":125},"end":{"row":19,"column":126},"action":"remove","lines":["\""]},{"start":{"row":19,"column":124},"end":{"row":19,"column":125},"action":"remove","lines":["d"]},{"start":{"row":19,"column":123},"end":{"row":19,"column":124},"action":"remove","lines":["i"]},{"start":{"row":19,"column":122},"end":{"row":19,"column":123},"action":"remove","lines":["_"]},{"start":{"row":19,"column":121},"end":{"row":19,"column":122},"action":"remove","lines":["\""]},{"start":{"row":19,"column":120},"end":{"row":19,"column":121},"action":"remove","lines":["("]},{"start":{"row":19,"column":119},"end":{"row":19,"column":120},"action":"remove","lines":["t"]},{"start":{"row":19,"column":118},"end":{"row":19,"column":119},"action":"remove","lines":["r"]},{"start":{"row":19,"column":117},"end":{"row":19,"column":118},"action":"remove","lines":["o"]},{"start":{"row":19,"column":116},"end":{"row":19,"column":117},"action":"remove","lines":["s"]}],[{"start":{"row":19,"column":115},"end":{"row":19,"column":116},"action":"remove","lines":["."],"id":1494}],[{"start":{"row":19,"column":114},"end":{"row":19,"column":115},"action":"insert","lines":["."],"id":1495},{"start":{"row":19,"column":115},"end":{"row":19,"column":116},"action":"insert","lines":["s"]},{"start":{"row":19,"column":116},"end":{"row":19,"column":117},"action":"insert","lines":["o"]},{"start":{"row":19,"column":117},"end":{"row":19,"column":118},"action":"insert","lines":["r"]},{"start":{"row":19,"column":118},"end":{"row":19,"column":119},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":119},"end":{"row":19,"column":121},"action":"insert","lines":["()"],"id":1496}],[{"start":{"row":19,"column":120},"end":{"row":19,"column":122},"action":"insert","lines":["\"\""],"id":1497}],[{"start":{"row":19,"column":121},"end":{"row":19,"column":122},"action":"insert","lines":["_"],"id":1498},{"start":{"row":19,"column":122},"end":{"row":19,"column":123},"action":"insert","lines":["i"]},{"start":{"row":19,"column":123},"end":{"row":19,"column":124},"action":"insert","lines":["d"]}],[{"start":{"row":19,"column":125},"end":{"row":19,"column":126},"action":"insert","lines":[","],"id":1499}],[{"start":{"row":19,"column":126},"end":{"row":19,"column":127},"action":"insert","lines":[" "],"id":1500},{"start":{"row":19,"column":127},"end":{"row":19,"column":128},"action":"insert","lines":["-"]},{"start":{"row":19,"column":128},"end":{"row":19,"column":129},"action":"insert","lines":["1"]}],[{"start":{"row":27,"column":114},"end":{"row":27,"column":130},"action":"insert","lines":[".sort(\"_id\", -1)"],"id":1501}],[{"start":{"row":35,"column":114},"end":{"row":35,"column":130},"action":"insert","lines":[".sort(\"_id\", -1)"],"id":1502}],[{"start":{"row":43,"column":114},"end":{"row":43,"column":130},"action":"insert","lines":[".sort(\"_id\", -1)"],"id":1503}],[{"start":{"row":51,"column":114},"end":{"row":51,"column":130},"action":"insert","lines":[".sort(\"_id\", -1)"],"id":1504}],[{"start":{"row":59,"column":114},"end":{"row":59,"column":130},"action":"insert","lines":[".sort(\"_id\", -1)"],"id":1505}],[{"start":{"row":2,"column":41},"end":{"row":2,"column":42},"action":"remove","lines":["o"],"id":1506},{"start":{"row":2,"column":40},"end":{"row":2,"column":41},"action":"remove","lines":["g"]},{"start":{"row":2,"column":39},"end":{"row":2,"column":40},"action":"remove","lines":["n"]},{"start":{"row":2,"column":38},"end":{"row":2,"column":39},"action":"remove","lines":["o"]},{"start":{"row":2,"column":37},"end":{"row":2,"column":38},"action":"remove","lines":["m"]},{"start":{"row":2,"column":36},"end":{"row":2,"column":37},"action":"remove","lines":["y"]},{"start":{"row":2,"column":35},"end":{"row":2,"column":36},"action":"remove","lines":["p"]},{"start":{"row":2,"column":34},"end":{"row":2,"column":35},"action":"remove","lines":[" "]},{"start":{"row":2,"column":33},"end":{"row":2,"column":34},"action":"remove","lines":[","]}],[{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"remove","lines":["_"],"id":1507}],[{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["-"],"id":1508}],[{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"remove","lines":["-"],"id":1509}],[{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["-"],"id":1510}],[{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"remove","lines":["-"],"id":1511}],[{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["_"],"id":1512}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":2},"action":"insert","lines":["# "],"id":1513},{"start":{"row":22,"column":0},"end":{"row":22,"column":2},"action":"insert","lines":["# "]},{"start":{"row":24,"column":0},"end":{"row":24,"column":2},"action":"insert","lines":["# "]},{"start":{"row":25,"column":0},"end":{"row":25,"column":2},"action":"insert","lines":["# "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":2},"action":"insert","lines":["# "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":2},"action":"insert","lines":["# "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":2},"action":"insert","lines":["# "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":2},"action":"insert","lines":["# "]},{"start":{"row":33,"column":0},"end":{"row":33,"column":2},"action":"insert","lines":["# "]},{"start":{"row":35,"column":0},"end":{"row":35,"column":2},"action":"insert","lines":["# "]},{"start":{"row":37,"column":0},"end":{"row":37,"column":2},"action":"insert","lines":["# "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":2},"action":"insert","lines":["# "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":2},"action":"insert","lines":["# "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":2},"action":"insert","lines":["# "]},{"start":{"row":43,"column":0},"end":{"row":43,"column":2},"action":"insert","lines":["# "]},{"start":{"row":45,"column":0},"end":{"row":45,"column":2},"action":"insert","lines":["# "]},{"start":{"row":46,"column":0},"end":{"row":46,"column":2},"action":"insert","lines":["# "]},{"start":{"row":48,"column":0},"end":{"row":48,"column":2},"action":"insert","lines":["# "]},{"start":{"row":49,"column":0},"end":{"row":49,"column":2},"action":"insert","lines":["# "]},{"start":{"row":51,"column":0},"end":{"row":51,"column":2},"action":"insert","lines":["# "]},{"start":{"row":53,"column":0},"end":{"row":53,"column":2},"action":"insert","lines":["# "]},{"start":{"row":54,"column":0},"end":{"row":54,"column":2},"action":"insert","lines":["# "]},{"start":{"row":56,"column":0},"end":{"row":56,"column":2},"action":"insert","lines":["# "]},{"start":{"row":57,"column":0},"end":{"row":57,"column":2},"action":"insert","lines":["# "]},{"start":{"row":59,"column":0},"end":{"row":59,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":2},"action":"remove","lines":["# "],"id":1514},{"start":{"row":22,"column":0},"end":{"row":22,"column":2},"action":"remove","lines":["# "]},{"start":{"row":24,"column":0},"end":{"row":24,"column":2},"action":"remove","lines":["# "]},{"start":{"row":25,"column":0},"end":{"row":25,"column":2},"action":"remove","lines":["# "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":2},"action":"remove","lines":["# "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":2},"action":"remove","lines":["# "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":2},"action":"remove","lines":["# "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":2},"action":"remove","lines":["# "]},{"start":{"row":33,"column":0},"end":{"row":33,"column":2},"action":"remove","lines":["# "]},{"start":{"row":35,"column":0},"end":{"row":35,"column":2},"action":"remove","lines":["# "]},{"start":{"row":37,"column":0},"end":{"row":37,"column":2},"action":"remove","lines":["# "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":2},"action":"remove","lines":["# "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":2},"action":"remove","lines":["# "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":2},"action":"remove","lines":["# "]},{"start":{"row":43,"column":0},"end":{"row":43,"column":2},"action":"remove","lines":["# "]},{"start":{"row":45,"column":0},"end":{"row":45,"column":2},"action":"remove","lines":["# "]},{"start":{"row":46,"column":0},"end":{"row":46,"column":2},"action":"remove","lines":["# "]},{"start":{"row":48,"column":0},"end":{"row":48,"column":2},"action":"remove","lines":["# "]},{"start":{"row":49,"column":0},"end":{"row":49,"column":2},"action":"remove","lines":["# "]},{"start":{"row":51,"column":0},"end":{"row":51,"column":2},"action":"remove","lines":["# "]},{"start":{"row":53,"column":0},"end":{"row":53,"column":2},"action":"remove","lines":["# "]},{"start":{"row":54,"column":0},"end":{"row":54,"column":2},"action":"remove","lines":["# "]},{"start":{"row":56,"column":0},"end":{"row":56,"column":2},"action":"remove","lines":["# "]},{"start":{"row":57,"column":0},"end":{"row":57,"column":2},"action":"remove","lines":["# "]},{"start":{"row":59,"column":0},"end":{"row":59,"column":2},"action":"remove","lines":["# "]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":2,"column":5},"end":{"row":2,"column":18},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1568104576855,"hash":"9f4ab718070d9007b943944fbae82a95ade7987a"}