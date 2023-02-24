import inquirer
import os
import json
import random

xaeroData = "XaeroWaypoints"
journeyData = "journeymap/data/sp"

list = os.listdir(xaeroData)
list.remove('backup')

questions = [
    inquirer.List(
        'instance',
        message="Which instance's Waypoints should be Converted?",
        choices=list
    )
]
answers = inquirer.prompt(questions)
instance = answers.get("instance")
xaeroData = xaeroData + "/" + instance
journeyData = journeyData + "/" + instance + "/waypoints"
dims = {"dim%0", "dim%-1", "dim%1"}
dimsClear = dict()
dimsClear["dim%0"] = "overworld"
dimsClear["dim%-1"] = "the_nether"
dimsClear["dim%1"] = "the_end"

for dim in dims:
    if os.path.exists(xaeroData + "/" + dim + "/waypoints.txt"):
        xaeroWaypoints = open(
            xaeroData + "/" + dim + "/waypoints.txt").read().split('\n')
        xaeroWaypoints = [x for x in xaeroWaypoints if not x.startswith('#')]
        for waypoint in xaeroWaypoints:
            if waypoint.startswith("waypoint"):
                waypointData = waypoint.split(":")
                waypointFileContent = {
                    "id": waypointData[1] + "_" + waypointData[3].removeprefix("-") + "-" + waypointData[4].removeprefix("-") + "-" + waypointData[5].removeprefix("-") + ".json",
                    "name": waypointData[1],
                    "icon": "journeymap:ui/img/waypoint-icon.png",
                    "colorizedIcon": "fake:color--5111554-waypoint-icon.png",
                    "x": int(waypointData[3]),
                    "y": int(waypointData[4]),
                    "z": int(waypointData[5]),
                    "r": random.randint(0, 255),
                    "g": random.randint(0, 255),
                    "b": random.randint(0, 255),
                    "enable": True,
                    "type": "Normal",
                    "origin": "journeymap",
                    "dimensions": [
                        "minecraft:" + dimsClear[dim]
                    ],
                    "persistent": True,
                    "showDeviation": False,
                    "iconColor": -1,
                    "customIconColor": False
                }
                jsonObject = json.dumps(waypointFileContent, indent=2)
                with open(journeyData + "/" + waypointData[1] + "_" + waypointData[3].removeprefix("-") + "-" + waypointData[4].removeprefix("-") + "-" + waypointData[5].removeprefix("-") + ".json", "w") as waypointFile:
                    waypointFile.write(jsonObject)
